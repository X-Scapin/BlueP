from front.module import Module

class Edge():

    def __init__(self, source, target):
        self.module_source = source
        self.module_target = target

    def get_source_point(self):
        return [self.module_source.x + Module.width /2, self.module_source.y + Module.height]

    def get_target_point(self):
        return [self.module_source.x + Module.width /2, self.module_source.y]
