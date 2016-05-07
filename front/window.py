from tkinter import *
from front.module_schema import ModuleSchema
from front.action_bar import ActionBarManager


def launch_bluep():
    """ Main method that launch tkinter interface"""
    window = Tk()

    graph_frame = Frame(window)
    graph_frame.pack(side=TOP, pady=4)

    execution_frame = Frame(window, background='yellow')
    execution_frame.pack(side=BOTTOM, pady=4)

    schema_frame = Frame(graph_frame)
    schema_frame.pack(side=RIGHT)

    action_frame = Frame(graph_frame)
    action_frame.pack(side=LEFT)

    test_button = Button(execution_frame, text="CONSOLE")
    test_button.pack(side=RIGHT)

    module_schema = ModuleSchema(schema_frame, width=400,
                                 height=400, background='yellow')
    module_schema.pack()

    action_bar_manager = ActionBarManager(action_frame,
                                          module_schema, window)

    window.mainloop()
