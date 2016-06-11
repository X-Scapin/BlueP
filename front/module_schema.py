import os
import sys
import subprocess
from tkinter import Canvas
from front.module import Module
from front.dialogs import Popup
from back.console import Console


class ModuleSchema(Canvas):
    def __init__(self, frame, workspace, background):
        Canvas.__init__(self, frame, background=background)
        self.module_list = list()
        self.bind("<Double-Button-1>", self.double_click)
        self.workspace = workspace
        self.inspect_console = Console(sys.stdout,
                                       sys.stderr, workspace)
        self.load_existing_modules()

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
                        self.add_module(new_module, alert_collision=False)
                        self.refresh()
                    else:
                        print("Can't found class in file " + file)
            break

    def add_module(self, module, alert_collision=True):
        if not self.check_module_existence(module):
            module.attributes = self.inspect_module(module)
            self.new_module_placement(module)
            self.module_list.append(module)
        elif alert_collision:
            Popup(None, "Module " + module.title + " already exists")

    def new_module_placement(self, module):
        max_x = 15
        for cur_module in self.module_list:
            if max_x < cur_module.x + Module.width:
                max_x = cur_module.x + Module.width + 15
        module.x = max_x

    def display_modules(self):
        for module in self.module_list:
            self.draw_module(module)

    def draw_module(self, module):
        self.create_rectangle(module.x, module.y, module.x + Module.width,
                              module.y + Module.height)
        # Arbitrary max classname displayed
        self.create_text(module.x + Module.width / 2,
                         module.y + 10, text=module.classname[0:14] + "...")
        self.draw_attributes(module)

    def draw_attributes(self, module):
        if module.attributes is not None:
            ca = module.attributes['class_attributes']
            ax = module.x + 5
            ay = module.y + 25
            feed_back = False
            for attribute in ca:
                if ay - 20 <= Module.height:
                    self.create_text(ax, ay, text=attribute[0],
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

    def refresh(self):
        # TODO clear
        self.display_modules()

    def double_click(self, event):
        for module in self.module_list:
            if(ModuleSchema.hit_module(module, event.x, event.y)):
                ModuleSchema.edit_file(module)

    def inspect_module(self, module):
        """Flush inspect_console and get module class and object attributes"""

        module_attributes = None
        self.inspect_console.flush_console()
        self.inspect_console.eval_command("import inspect")
        self.inspect_console.eval_command(
            "from " + module.title + " import " + module.classname)

        self.inspect_console.eval_command("attributes = None")
        self.inspect_console.eval_command("""attributes = inspect.getmembers({classname},
                              lambda a:not(inspect.isroutine(a)))
                              """.format(classname=module.classname))
        attributes_exist = self.inspect_console.eval_command(
            """'true' if attributes is not None else 'false'""")

        if eval(attributes_exist) == 'true':
            class_attributes = self.inspect_console.eval_command("""[a for a in attributes if not(a[0].startswith('__')
            and a[0].endswith('__'))]""")

            module_attributes = {'class_attributes': eval(class_attributes)}
            print("TODO get instance attributes")
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
