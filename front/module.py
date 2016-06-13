import os
import re
from string import Template

CLASS_TEMPLATE = os.getcwd() + "/resources/class.template"


class Module():
    """Create with its module title or main class name"""
    width = 130
    height = 100
    # Arbitrary max for text display
    max_characters = 14

    def __init__(self, directory, title=None, main_class=None):
        if title is not None and main_class is None:
            if(title[-3:] == ".py"):
                title = title[:-3]
            self.title = title.lower()
            self.classname = Module.classname_from_title(self.title)
        elif title is None and main_class is not None:
            self.classname = main_class
            self.title = Module.modulename_from_classname(main_class)
        else:
            if(title[-3:] == ".py"):
                title = title[:-3]
            self.title = title
            self.classname = main_class

        self.x = 15
        self.y = 50
        self.py_file = None
        self.attributes = None
        self.parent_classes = list()
        self.directory = directory
        self.compute_python_path()

    def compute_python_path(self):
        # TODO check .py
        self.py_file = self.directory + "/" + self.title + ".py"

    def contains(self, x, y):
        if(x > self.x and x < self.x + Module.width):
            if(y > self.y and y < self.y + Module.height):
                return True
        return False

    def create_python_module(self):
        open(self.py_file, 'a').close()

    def init_file_module(self):
        """Fill file module with default class and methods"""
        template_file = open(CLASS_TEMPLATE)
        template_content = Template(template_file.read())
        subs_map = {'classname': self.classname,
                    'classinstance':
                    Module.modulename_from_classname(self.classname)}

        module_content = template_content.substitute(subs_map)
        module_file = open(self.py_file, 'w')
        module_file.write(module_content)

        template_file.close()
        module_file.close()

    def classname_from_title(title):
        split_title = title.split('_')
        classname = ""
        for part in split_title:
            part = part[0].upper() + part[1:]
            classname += part

        return classname

    def modulename_from_classname(classname):
        split_classname = re.findall('[A-Z][^A-Z]*', classname)
        modulename = split_classname[0].lower()
        for part in split_classname[1:]:
            modulename += "_" + part.lower()

        return modulename

    def get_instance_attributes(file):
        # [(att, value)]
        attributes = []
        try:
            module = open(file, 'r')
            module_lines = module.readlines()

            in_zone = False
            for line in module_lines:
                if re.search("^\s*def\s+__init__.*", line) is not None:
                    in_zone = True

                if in_zone is True:
                    att_search = re.search("^\s*self.(.+)\s*=\s*(.*)", line)
                    if att_search is not None:
                        attribute = (att_search.group(1), att_search.group(2))
                        attributes.append(attribute)

                if re.search("^\s*def\s+(?!__init__).*", line):
                    in_zone = False

            module.close()
        except FileNotFoundError:
            print("File not found " + file)

        return attributes

    def get_first_classname(file):
        first_classname = None
        try:
            module = open(file, 'r')
            module_content = module.read()
            match = re.search("^class (.+)\(.*\)\s*:",
                              module_content, re.MULTILINE)
            if match is not None:
                first_classname = match.group(1)
            module.close()

        except FileNotFoundError:
            print("File not found " + file)

        return first_classname

    def get_parent_classes(file):
        parent_classes = list()
        try:
            module = open(file, 'r')
            module_content = module.read()
            match = re.search("^class .+\((.*)\)\s*:",
                              module_content, re.MULTILINE)
            if match is not None:
                print(match.group(0))
                classes = match.group(1)
                split_classes = classes.replace(" ", "").split(",")
                parent_classes = split_classes
            module.close()

        except FileNotFoundError:
            print("File not found " + file)

        return parent_classes
