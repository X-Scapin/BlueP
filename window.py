from tkinter import *
from module_schema import ModuleSchema
from action_bar import ActionBarManager
import sys

print(sys.version)

window = Tk()

schema_frame = Frame(window)
schema_frame.pack(side=RIGHT)

action_frame = Frame(window)
action_frame.pack(side=LEFT)

# bouton = Button(action_frame, text="Toto", command=window.quit)
# bouton.pack()

module_schema = ModuleSchema(schema_frame, width=400, height=400, background='yellow')
module_schema.pack()

action_bar_manager = ActionBarManager(action_frame, module_schema,window)

# firstModule = Module("Toto")
# canvas.addModule(firstModule)
# canvas.displayModules()

#listb = Listbox(root)

window.mainloop()