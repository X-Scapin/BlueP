from tkinter import *
from io import StringIO
import code
import sys


class Console():
    def __init__(self, stdout, stderr, workspace):
        self.console = code.InteractiveConsole()
        self.stdout = stdout
        self.stderr = stderr
        self.locout = StringIO()
        self.workspace = workspace
        self.instances = ""
        self.init_session()

    def init_session(self):
        self.eval_command("import os")
        self.eval_command("import sys")
        self.eval_command("import gc")
        self.eval_command("import back.interactive_console_utils")
        self.eval_command("sys.path.append('" + self.workspace + "')")

    def set_locout(self):
        self.locout = StringIO()
        sys.stdout = self.locout
        sys.stderr = self.locout

    def set_stdout(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def get_output(self):
        return self.locout.getvalue()

    def eval_command(self, command):
        self.set_locout()
        self.console.push(command)
        outputstring = self.get_output()
        self.locout.close()
        self.refresh_instance_list()
        self.set_stdout()

        return outputstring

    def run_source(self, filename):
        self.console.runsource(filename=filename)

    def flush_console(self):
        self.eval_command("gc.collect()")
        self.console = code.InteractiveConsole()
        self.init_session()

    def refresh_instance_list(self):
        instances_out = StringIO()
        sys.stdout = instances_out
        sys.stderr = instances_out

        self.console.push("back.interactive_console_utils.compute_instance_list()")
        self.instances = instances_out.getvalue()
        instances_out.close()
