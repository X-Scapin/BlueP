from tkinter import *
import back.utils as utils

DIALOG_WIDTH = 400
DIALOG_HEIGHT = 130


class TextDialog(object):

    def __init__(self, parent, title, field_name):
        self.parent = parent
        if self.parent is None:
            self.dialog = Tk()
        else:
            self.dialog = Toplevel(self.parent)

        self.dialog.wm_title(title)

        field_frame = Frame(self.dialog)
        field_frame.pack(side=TOP, fill=Y, expand=1)

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

        self.dialog.bind("<Return>", self.ok_action)
        self.dialog.bind("<Escape>", self.cancel_action)
        utils.center_window(self.dialog, DIALOG_WIDTH, DIALOG_HEIGHT)
        self.entry.focus()

        if self.parent is None:
            self.dialog.mainloop()

    def ok_action(self, event=None):
        self.field_value = self.entry.get()
        self.dialog.destroy()

    def cancel_action(self, event=None):
        self.dialog.destroy()


class Popup():
    """Display basic popup with text
    Set parent to None for independant popup"""

    def __init__(self, parent, text, title="Information"):
        self.parent = parent
        if self.parent is None:
            self.dialog = Tk()
        else:
            self.dialog = Toplevel(self.parent)

        self.dialog.wm_title(title)

        field_frame = Frame(self.dialog)
        field_frame.pack(side=TOP, fill=Y, expand=1)

        button_frame = Frame(self.dialog)
        button_frame.pack(side=BOTTOM)

        label = Label(field_frame, text=text)
        label.pack(side=LEFT)

        ok_button = Button(button_frame, text="OK", command=self.ok_action)
        ok_button.pack(side=LEFT)

        self.dialog.bind("<Return>", self.ok_action)
        self.dialog.bind("<Escape>", self.ok_action)
        utils.center_window(self.dialog, DIALOG_WIDTH, DIALOG_HEIGHT)

        if self.parent is None:
            self.dialog.mainloop()

    def ok_action(self):
        self.dialog.destroy()
