from tkinter import *
from back.console import Console


class ExecutionFrame(Frame):
    def __init__(self, window, background=None):
        Frame.__init__(self, window, background=background)

        self.instances_part = Frame(self, width=500)
        self.instances_part.pack(side=LEFT, fill=BOTH, expand=1)

        self.console_part = Frame(self)
        self.console_part.pack(side=RIGHT, fill=BOTH, expand=1)

        self.entry = Entry(self.console_part)
        self.entry.pack(fill=BOTH)
        self.entry.bind("<Return>", self.entry_callback)

        scrollbar = Scrollbar(self.console_part)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.text_box = Text(self.console_part, wrap='word', height=8,
                             yscrollcommand=scrollbar.set)
        self.text_box.pack(fill=BOTH, expand=1)

        scrollbar.config(command=self.text_box.yview)

        self.console = Console(sys.stdout, sys.stderr, window.workspace)

    def entry_callback(self, event):
        entry_value = self.entry.get()
        self.text_box.insert(END, self.console.eval_command(entry_value))
        self.text_box.see(END)
        self.entry.delete(0, END)
