# -*- coding: utf8 -*-

__version__ = "1.0"
__author__ = "Astalav"

class LogicalAnd:
	def __init__(self, input0 = False, input1 = False, name = "AND"):
		self.input0 = input0
		self.input1 = input1
		self.output = None
		self.name = name

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; input0: " + str(self.input0) + \
				"; input1: " + str(self.input1) + \
				"; output: " + str(self.output) + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		print(str(output))
		return

	def execute(self):
		if self.input0 == False or self.input1 == False:
			self.output = False
		elif self.input0 == self.input1 == True:
			self.output = True
		else:
			self.output = None
		return

