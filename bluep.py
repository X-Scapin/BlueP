import sys
import os
from front.window import MainWindow
from front.dialogs import TextDialog
from front.dialogs import Popup
from back.workspace import Workspace


class BlueP():
    def __init__(self):
        self.workspace = None
        self.define_workspace()

        if self.workspace is not None:
            print(self.workspace.directory)
            self.main_window = MainWindow(self.workspace.directory)

    def define_workspace(self):
        workspace_dialog = TextDialog(None, "Define workspace",
                                      "Workspace path")

        if workspace_dialog.field_value is not None:
            self.workspace = Workspace(workspace_dialog.field_value)
            feed_back = self.workspace.check_workspace()
            if feed_back is not True:
                self.workspace = None
                Popup(None, feed_back)
                self.define_workspace()

if __name__ == '__main__':
    BlueP()
