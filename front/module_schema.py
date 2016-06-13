import os
import sys
import subprocess
from tkinter import *
from front.module import Module
from front.edge import Edge
from front.dialogs import Popup
from back.console import Console
import math
import json


class ModuleSchema(Canvas):
    def __init__(self, frame, workspace, background):
        Canvas.__init__(self, frame, background=background, scrollregion=(0,0,1000,1000))
        self.module_list = list()
        self.edge_list = list()
        self.bind("<Double-Button-1>", self.double_click)
        self.bind("<ButtonPress-1>", self.select_instance)
        self.bind("<B1-Motion>", self.drag_move)
        self.bind("<ButtonRelease-1>", self.end_drag)
        self.bind("<ButtonRelease-3>", self.popup)

        self.workspace = workspace
        self.inspect_console = Console(sys.stdout,
                                       sys.stderr, workspace)
        self.load_existing_modules()
        self.selected_module = None
        self.module_to_delete = None
        self.schema_scrollbar()

        self.menu = Menu(self, tearoff=0)
        self.menu.add_command(label="Delete", command=self.delete_module)

    def schema_scrollbar(self):
        hbar = Scrollbar(self, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.xview)
        vbar = Scrollbar(self, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.yview)
        self.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

    def load_existing_modules(self):
        for(dirpath, dirnames, filenames) in os.walk(self.workspace):
            print("load existing modules")
            for file in filenames:
                if(file[-2:] == "py"):
                    abs_path = os.path.abspath(os.path.join(dirpath, file))
                    first_classname = Module.get_first_classname(abs_path)
                    if first_classname is not None:
                        new_module = Module(self.workspace, title=file,
                                            main_class=first_classname)
                        print("module " + new_module.py_file + " / " + new_module.classname)
                        self.add_module(new_module, alert_collision=False)
                    else:
                        print("Can't found class in file " + file)
            break
        self.load_edges()
        self.load_existing_placement()

        self.redraw()

    def load_existing_placement(self):
        bluep_file = open(self.workspace + '/' + 'project.bluep', 'r')
        data = {}
        if os.stat(bluep_file.name).st_size != 0:
            data = json.load(bluep_file)
        bluep_file.close()
        for module in self.module_list:
            if module.classname in data:
                placement = data[module.classname]
                if placement is not None:
                    for x in placement.keys():
                        module.x = int(float(x))
                        module.y = int(float(placement[x]))

    def add_module(self, module, alert_collision=True):
        if not self.check_module_existence(module):
            module.attributes = self.inspect_module(module)
            self.module_list.append(module)
            self.new_module_placement(module)
        elif alert_collision:
            Popup(None, "Module " + module.title + " already exists")

    def new_module_placement(self, module):
        count = self.module_list.__len__() - 1
        column_size = 4
        delta = 30
        module.x = (count % column_size) * (Module.width + delta) + delta
        module.y = math.floor(count / column_size) * (Module.height + delta) + delta

    def display_modules(self):
        for module in self.module_list:
            self.draw_module(module)

    def display_edges(self):
        for edge in self.edge_list:
            source_point = edge.get_source_point()
            target_point = edge.get_target_point()
            self.create_line(source_point[0], source_point[1], target_point[0], target_point[1], arrow=FIRST)

    def draw_module(self, module):
        self.create_rectangle(module.x, module.y, module.x + Module.width,
                              module.y + Module.height, fill='#ffe680')
        classname = module.classname
        if len(classname) > Module.max_characters:
            classname = classname[0:Module.max_characters] + "..."
        self.create_text(module.x + Module.width / 2,
                         module.y + 10, text=classname, font = ("Times", 10, "bold"))
        self.create_text(module.x + Module.width / 2,
                         module.y + Module.height - 10, text=module.title, font = ("Times", 8, "italic"))
        self.draw_attributes(module)

    def draw_attributes(self, module):
        if module.attributes is not None:
            ca = module.attributes['class_attributes']
            ia = module.attributes['instance_attributes']
            ax = module.x + 5
            ay = module.y + 25
            feed_back = False
            for attribute in ca:
                attribute_text = attribute[0]
                if len(attribute_text) > Module.max_characters:
                    attribute_text = attribute_text[0:Module.max_characters] + "..."
                if ay + 25 <= Module.height + module.y:
                    self.create_text(ax, ay, text=attribute_text,
                                     anchor='nw', width=Module.width - 4)
                elif feed_back is False:
                    feed_back = True
                    self.create_text(ax, ay, text="...",
                                     anchor='nw')
                ay += 18

            for attribute in ia:
                attribute_text = "s." + attribute[0]
                if len(attribute_text) > Module.max_characters:
                    attribute_text = attribute_text[0:Module.max_characters] + "..."
                if ay + 25 <= Module.height + module.y:
                    self.create_text(ax, ay, text=attribute_text,
                                     anchor='nw', width=Module.width - 4)
                elif feed_back is False:
                    feed_back = True
                    self.create_text(ax, ay, text="...",
                                     anchor='nw')
                ay += 18

    def check_module_existence(self, module):
        for cur_module in self.module_list:
            if module.title == cur_module.title:
                return True
        return False

    def load_edges(self):
        for module in self.module_list:
            for parent_class in module.parent_classes:
                for cur_module in self.module_list:
                    if cur_module.classname == parent_class:
                        self.edge_list.append(Edge(cur_module, module))

    def redraw(self):
        self.delete("all")
        self.display_modules()
        self.display_edges()

    def refresh(self):
        self.delete("all")
        self.module_list = list()
        self.edge_list = list()
        self.load_existing_modules()

    def double_click(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        for module in self.module_list:
            if(ModuleSchema.hit_module(module, x, y)):
                ModuleSchema.edit_file(module)
                return

    def select_instance(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        for module in self.module_list:
            if(ModuleSchema.hit_module(module, x, y)):
                self.selected_module = module
                return

    def drag_move(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        if self.selected_module is not None:
            self.selected_module.x = x
            self.selected_module.y = y
            self.redraw()

    def end_drag(self, event):
         self.selected_module = None

    def popup(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        for module in self.module_list:
            if(ModuleSchema.hit_module(module, x, y)):
                self.module_to_delete = module
                self.menu.post(int(event.x_root), int(event.y_root))
                return

    def delete_module(self):
        if self.module_to_delete is not None:
            os.remove(self.module_to_delete.py_file)
            self.refresh()

    def inspect_module(self, module):
        """Flush inspect_console, get module class, object attributes and heritage"""

        module_attributes = None
        self.inspect_console.flush_console()
        self.inspect_console.eval_command("import inspect")
        self.inspect_console.eval_command(
            "from " + module.title + " import " + module.classname)

        module.parent_classes = Module.get_parent_classes(module.py_file)

        self.inspect_console.eval_command("attributes = None")
        self.inspect_console.eval_command("""attributes = inspect.getmembers({classname},
                              lambda a:not(inspect.isroutine(a)))
                              """.format(classname=module.classname))
        attributes_exist = self.inspect_console.eval_command(
            """'true' if attributes is not None else 'false'""")

        if eval(attributes_exist) == 'true':
            class_attributes = self.inspect_console.eval_command("""[a for a in attributes if not(a[0].startswith('__')
            and a[0].endswith('__'))]""")

            instance_attributes = Module.get_instance_attributes(
                module.py_file)
            module_attributes = {'class_attributes': eval(class_attributes),
                                 'instance_attributes': instance_attributes}
        else:
            print("Errors in module : " + module.title)

        return module_attributes

    def hit_module(module, x, y):
        return module.contains(x, y)

    def edit_file(module):
        if(os.name is "nt"):
            os.system("start notepad " + module.py_file)
        elif(os.name is "posix"):
            subprocess.call(["xdg-open", module.py_file])
        else:
            print("Unsupported os")
