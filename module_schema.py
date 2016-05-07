from tkinter import Canvas
from module import Module

class ModuleSchema(Canvas):
	def __init__(self, frame, width, height, background):
		Canvas.__init__(self, frame, width=width, height=height, background=background)
		self.moduleList = list()

	def printToto(self):
		print(self.moduleList[0])

	def addModule(self, module):
		self.new_module_placement(module)
		self.moduleList.append(module)

	def new_module_placement(self, module):
		max_x = 15
		for cur_module in self.moduleList:
			if max_x<cur_module.x+Module.width:
				max_x=cur_module.x+Module.width+15
		module.x=max_x


	def displayModules(self):
		for module in self.moduleList:
			self.drawModule(module)

	def drawModule(self, module):
		self.create_rectangle(module.x, module.y, module.x + Module.width, module.y + Module.height)
		self.create_text(module.x+Module.width/2, module.y+10, text=module.title)

	def refresh(self):
		#clear
		self.displayModules()