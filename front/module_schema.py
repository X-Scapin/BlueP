import os
import subprocess
from tkinter import Canvas
from front.module import Module


class ModuleSchema(Canvas):
    def __init__(self, frame, workspace, background):
        Canvas.__init__(self, frame, background=background)
        self.module_list = list()
        self.bind("<Double-Button-1>", self.double_click)
        self.workspace = workspace
        self.load_existing_modules()

    def load_existing_modules(self):
        for(dirpath, dirnames, filenames) in os.walk(self.workspace):
            for file in filenames:
                print(file[-2:])
                if(file[-2:] == "py"):
                    print(file)
                    new_module = Module(file, self.workspace)
                    self.add_module(new_module)
                    self.refresh()

            break

    def add_module(self, module):
        self.new_module_placement(module)
        self.module_list.append(module)

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
        self.create_text(module.x + Module.width / 2,
                         module.y + 10, text=module.title)

    def refresh(self):
        # TODO clear
        self.display_modules()

    def double_click(self, event):
        for module in self.module_list:
            if(ModuleSchema.hit_module(module, event.x, event.y)):
                ModuleSchema.edit_file(module)

    def hit_module(module, x, y):
        return module.contains(x, y)

    def edit_file(module):
        if(os.name is "nt"):
            os.system(module.py_file)
        elif(os.name is "posix"):
            subprocess.call(["xdg-open", module.py_file])
        else:
            print("Unsupported os")
