from tkinter import *


class NewModuleDialog(object):

    def __init__(self, parent):
        self.dialog = Toplevel(parent)
        self.dialog.title = "Choose new module name"
        field_frame = Frame(self.dialog)
        field_frame.pack(side=TOP)

        button_frame = Frame(self.dialog)
        button_frame.pack(side=BOTTOM)

        label = Label(field_frame, text="module name")
        label.pack(side=LEFT)

        self.entry = Entry(field_frame, width=50)
        self.entry.pack(side=RIGHT)

        ok_button = Button(button_frame, text="OK", command=self.ok_action)
        ok_button.pack(side=LEFT)

        cancel_button = Button(button_frame, text="cancel",
                               command=self.cancel_action)
        cancel_button.pack(side=RIGHT)

        self.new_name = None

    def ok_action(self):
        self.new_name = self.entry.get()
        self.dialog.destroy()

    def cancel_action(self):
        self.dialog.destroy()
