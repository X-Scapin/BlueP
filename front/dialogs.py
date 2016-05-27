from tkinter import *


class TextDialog(object):

    def __init__(self, parent, title, field_name):
        self.parent = parent
        if self.parent is None:
            self.dialog = Tk()
        else:
            self.dialog = Toplevel(self.parent)

        self.dialog.title = title
        field_frame = Frame(self.dialog)
        field_frame.pack(side=TOP)

        button_frame = Frame(self.dialog)
        button_frame.pack(side=BOTTOM)

        label = Label(field_frame, text=field_name)
        label.pack(side=LEFT)

        self.entry = Entry(field_frame, width=50)
        self.entry.pack(side=RIGHT)

        ok_button = Button(button_frame, text="OK", command=self.ok_action)
        ok_button.pack(side=LEFT)

        cancel_button = Button(button_frame, text="cancel",
                               command=self.cancel_action)
        cancel_button.pack(side=RIGHT)

        self.field_value = None

        if self.parent is None:
            self.dialog.mainloop()

    def ok_action(self):
        self.field_value = self.entry.get()
        self.dialog.destroy()

    def cancel_action(self):
        self.dialog.destroy()
