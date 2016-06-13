from tkinter import Canvas
import math

class InstanceSchema(Canvas):

    width = 100
    height = 50
    column_size = 3
    delta = 15

    def __init__(self, frame, window, background):
        self.window = window
        Canvas.__init__(self, frame, background=background)

    def refresh(self, instances):
        self.delete("all")
        module_names = self.compute_module_names()
        instanceToAdress = instances.split('\n')
        instanceCount = 0
        for i in range(instanceToAdress.__len__() - 1):
            if i % 2 == 0 and any(instanceToAdress[i] == item for item in module_names):
                self.draw_instance(instanceToAdress[i], instanceToAdress[i + 1], instanceCount)
                instanceCount += 1

    def compute_module_names(self):
        module_list = self.window.module_schema.module_list
        module_names = []
        for module in module_list:
            if module_names.__len__() is 0:
                module_names = [module.classname]
            else:
                module_names.append(module.classname)

        return module_names

    def draw_instance(self, name, adress, index):
        x = (index % InstanceSchema.column_size) * (InstanceSchema.width + InstanceSchema.delta) + InstanceSchema.delta
        y = math.floor(index / InstanceSchema.column_size) * (InstanceSchema.height + InstanceSchema.delta) + InstanceSchema.delta
        self.create_rectangle(x, y, x + InstanceSchema.width, y + InstanceSchema.height)
        self.create_text(x + InstanceSchema.width / 2,
                         y + 10, text=name)
        self.create_text(x + InstanceSchema.width / 2,
                         y + 40, text=adress)
