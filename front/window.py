from tkinter import *
from front.module_schema import ModuleSchema
from front.action_bar import ActionBarManager


class BlueP():
    """ Main class that embed tkinter interface"""

    def __init__(self):
        window = Tk()

        schema_frame = Frame(window)
        schema_frame.pack(side=RIGHT)

        action_frame = Frame(window)
        action_frame.pack(side=LEFT)

        module_schema = ModuleSchema(schema_frame, width=400,
                                     height=400, background='yellow')
        module_schema.pack()

        action_bar_manager = ActionBarManager(action_frame,
                                              module_schema, window)

        window.mainloop()
