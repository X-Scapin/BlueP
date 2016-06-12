from tkinter import *
from io import StringIO
import subprocess
import code
import sys
import os
import re


class Console():
    end_of_file_command = "print(\"---bluep-end-of-output---\")"

    def __init__(self, workspace):
        self.workspace = workspace
        self.outputfile = None
        self.outputfile_path = "tmp/{!s}.tmp".format(id(self))
        print(self.outputfile_path)
        self.subproc = None
        self.instances = ""

        self.create_file()
        self.init_session()

    def create_file(self):
        try:
            open(self.outputfile_path, "w").close()
            print("Check if file is clear")
        except FileNotFoundError:
            print("could not create file " + self.outputfile_path)

    def init_session(self):
        print("Create python subprocess")
        self.outputfile = open(self.outputfile_path, "w")
        self.subproc = subprocess.Popen("python", stdin=subprocess.PIPE, stdout=self.outputfile, stderr=self.outputfile)
        self.subproc.stdin.write(bytes("print(\"1\")", 'utf-8'))
        self.eval_command("import sys")
        self.eval_command("sys.path.append('" + self.workspace + "')")


    def eval_command(self, command):
        print("Eval command : " + command)
        self.subproc.stdin.write(bytes("print(\"1\")", 'utf-8'))
        self.subproc.stdin.write(Console.encode_string(Console.end_of_file_command))
        outputstring = self.get_output()
        # self.refresh_instance_list()
        return outputstring

    def get_output(self):
        print("Get output")
        output_ready = False
        output = None
        while output_ready is not True:
            print("Check again")
            try:
                outputfile = open(self.outputfile_path, "r")
                lines = outputfile.readlines()
                print(lines)
                for line in lines:
                    if line == Console.end_of_file_command:
                        output = lines
                        output_ready = True
                outputfile.close()
                output_ready = True
            except FileNotFoundError:
                print("Could read file " + self.outputfile_path)

        outputfile = open(self.outputfile_path, "w").close()

        return output

    def flush_console(self):
        os.killpg(os.getpgid(self.subproc.pid), signal.SIGTERM)
        self.subproc = None
        self.outputfile.close()
        self.init_session()

    def refresh_instance_list(self):
        self.console.push("back.interactive_console_utils.compute_instance_list()")
        self.instances = instances_out.getvalue()
        instances_out.close()

    def encode_string(string):
        print("Encode : "+string+"\n")
        return bytes(string + "\n", 'utf-8')
