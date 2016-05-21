from tkinter import *
from io import StringIO
import code
import sys


class Console():
    def __init__(self, stdout):
        self.console = code.InteractiveConsole()
        self.stdout = stdout
        self.locout = StringIO()

    def set_locout(self):
        self.locout = StringIO()
        sys.stdout = self.locout

    def set_stdout(self):
        sys.stdout = self.stdout
        self.locout.close()

    def get_output(self):
        return self.locout.getvalue()

    def eval_command(self, command):
        self.set_locout()
        self.console.push(command)
        outputstring = self.get_output()
        self.set_stdout()
        return outputstring

    def run_source(self, filename):
        self.console.runsource(filename=filename)

    def flush_console(self):
        self.console = code.InteractiveConsole()
