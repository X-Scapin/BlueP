from tkinter import *
from front.module_schema import ModuleSchema
from front.action_bar import ActionBarManager
from front.execution_frame import ExecutionFrame


class MainWindow(Tk):
    def __init__(self, workspace):
        Tk.__init__(self)
        self.workspace = workspace
        graph_frame = Frame(self)
        graph_frame.pack(side=TOP, pady=4)

        self.execution_frame = ExecutionFrame(self, background='green')
        self.execution_frame.pack(side=BOTTOM, pady=4)

        schema_frame = Frame(graph_frame)
        schema_frame.pack(side=RIGHT)

        action_frame = Frame(graph_frame)
        action_frame.pack(side=LEFT)

        module_schema = ModuleSchema(schema_frame, workspace, width=400,
                                     height=400, background='yellow')
        module_schema.pack()

        action_bar_manager = ActionBarManager(action_frame,
                                              module_schema, self)

        self.mainloop()
