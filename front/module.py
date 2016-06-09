
class Module():

    width = 75
    height = 100

    def __init__(self, title, directory):
        if(title[-3:] == ".py"):
            title = title[:-3]
        self.title = title.lower()
        self.classname = Module.classname_from_title(self.title)
        self.x = 15
        self.y = 50
        self.py_file = None
        self.directory = directory
        self.compute_python_path()

    def compute_python_path(self):
        #TODO check .py
        self.py_file = self.directory + "/" + self.title + ".py"

    def contains(self, x, y):
        if(x > self.x and x < self.x + Module.width):
            if(y > self.y and y < self.y + Module.height):
                return True
        return False

    def classname_from_title(title):
        split_title = title.split('_')
        classname = ""
        for part in split_title:
            part = part[0].upper() + part[1:]
            classname += part

        return classname
