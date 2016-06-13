from tkinter import *
from front.module_schema import ModuleSchema
from front.action_bar import ActionBarManager
from front.execution_frame import ExecutionFrame
import back.utils as utils

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

class MainWindow(Tk):
    def __init__(self, workspace):
        Tk.__init__(self)
        self.wm_title("BlueP")

        self.workspace = workspace

        graph_frame = Frame(self)
        graph_frame.pack(side=TOP, pady=4, fill=BOTH, expand=1)

        self.execution_frame = ExecutionFrame(self)
        self.execution_frame.pack(side=BOTTOM, pady=4, fill=BOTH, expand=1)

        action_frame = Frame(graph_frame, width=100,
                             height=500)
        action_frame.pack(side=LEFT, padx=4)

        schema_frame = Frame(graph_frame, width=500, height=500)
        schema_frame.pack(side=RIGHT, fill=BOTH, expand=1)

        self.module_schema = ModuleSchema(schema_frame,
                                     workspace, background='#fff5cc')
        self. module_schema.pack(fill=BOTH, expand=1)

        action_bar_manager = ActionBarManager(action_frame,
                                              self.module_schema, self)

        utils.center_window(self, DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.mainloop()
