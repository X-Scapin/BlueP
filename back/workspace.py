import os
# print(os.path.isdir("/home/el"))
# print(os.path.exists("/home/el/myfile.txt"))


class Workspace():
    def __init__(self, directory):
        self.directory = directory
        self.config_file = None
        if directory is not None:
            self.config_file = directory + "/project.bluep"

    def check_workspace(self):
        """Check if workspace dir and workspace config exist
           Create them if not
           Return True if ok, message error if not"""
        feed_back = True

        if self.directory is "":
            feed_back = "Please, specify a directory"
        else:
            try:
                os.makedirs(self.directory, exist_ok=True)
                if not os.path.exists(self.directory):
                    feed_back = "Could not resolve " + self.directory
                else:
                    open(self.config_file, 'a').close()
                    if not os.path.exists(self.config_file):
                        feed_back = "Can't create " + self.config_file

            except PermissionError:
                feed_back = "Can't create " + self.directory

        return feed_back
