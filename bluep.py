import sys
from front.window import MainWindow
from front.dialogs import TextDialog


class BlueP():
    def __init__(self):
        self.workspace = None
        self.define_workspace()

        if self.workspace is not None:
            self.main_window = MainWindow()

    def define_workspace(self):
        workspace_dialog = TextDialog(None, "Define workspace",
                                      "Workspace path")
        self.workspace = workspace_dialog.field_value

        if self.validate_workspace() is False:
            self.define_workspace()

    def validate_workspace(self):
        if self.workspace is "":
            return False
        else:
            return True

BlueP()

# print(sys.version)
