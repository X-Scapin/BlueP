from tkinter import *
from front.module import Module
from front.dialogs import TextDialog


class ActionBarManager():
    def __init__(self, frame, schema_module, window):
        self.frame = frame
        self.schema_module = schema_module
        self.create_buttons()
        self.window = window

    def create_buttons(self):
        new_module_but = Button(self.frame, text="New Module ...",
                                command=self.new_module_action)
        new_module_but.pack(pady=2, fill=X, expand=1)
        save_button = Button(self.frame, text="Save",
                             command=self.save_action)
        save_button.pack(pady=2, fill=X, expand=1)
        compile_button = Button(self.frame, text="Compile",
                                command=self.compile_action)
        compile_button.pack(pady=2, fill=X, expand=1)

    def new_module_action(self):
        new_module_dialog = TextDialog(self.window,
                                       "Choose new class name", "Class name")

        self.window.wait_window(new_module_dialog.dialog)

        if new_module_dialog.field_value is not None:
            new_module = Module(self.window.workspace,
                                main_class=new_module_dialog.field_value)
            new_module.create_python_module()
            new_module.init_file_module()
            self.schema_module.add_module(new_module)
            self.schema_module.refresh()

    def save_action(self):
        # TODO
        print("TODO")

    def compile_action(self):
        self.window.execution_frame.console.flush_console()
        for module in self.schema_module.module_list:
            self.window.execution_frame.console.eval_command("import " + module.title)
            self.window.execution_frame.console.eval_command("from " + module.title + " import " + module.classname)
            self.window.execution_frame.instance_schema.refresh(self.window.execution_frame.console.instances)
