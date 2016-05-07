from tkinter import Button
from module import Module
from new_module_dialog import NewModuleDialog


class ActionBarManager():
    def __init__(self, frame, schema_module, window):
        self.frame = frame
        self.schema_module = schema_module
        self.create_buttons()
        self.window = window

    def create_buttons(self):
        new_module_but = Button(self.frame, text="New Module ...",
                                command=self.new_module_action)
        new_module_but.pack()

    def new_module_action(self):
        new_module_dialog = NewModuleDialog(self.window)

        self.window.wait_window(new_module_dialog.dialog)

        if new_module_dialog.new_name is not None:
            new_module = Module(new_module_dialog.new_name)
            self.schema_module.add_module(new_module)
            self.schema_module.refresh()
