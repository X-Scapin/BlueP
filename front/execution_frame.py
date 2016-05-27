from tkinter import *
from back.console import Console


class ExecutionFrame(Frame):
    def __init__(self, parent, background):
        Frame.__init__(self, parent, background=background)

        self.entry = Entry(self)
        self.entry.pack(fill=BOTH, expand=1)
        self.entry.bind("<Return>", self.entry_callback)

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.text_box = Text(self, wrap='word', height=8,
                             yscrollcommand=scrollbar.set)
        self.text_box.pack()

        scrollbar.config(command=self.text_box.yview)

        self.console = Console(sys.stdout)

    def entry_callback(self, event):
        entry_value = self.entry.get()
        self.text_box.insert(END, self.console.eval_command(entry_value))
        self.text_box.see(END)
        self.entry.delete(0, END)
