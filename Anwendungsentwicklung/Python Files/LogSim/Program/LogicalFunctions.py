# -*- coding: utf8 -*-

__version__ = "1.1"
__author__ = "Astalav"

class LogicalAnd:
	def __init__(self, input0 = None, input1 = None, name = "AND"):
		self.__input0 = input0
		self.__input1 = input1
		self.__output = None
		self.name = name
		self.__execute()

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; input0: " + str(self.input0) + \
				"; input1: " + str(self.input1) + \
				"; output: " + str(self.output) + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		print(str(output))
		return

	def __execute(self):
		if self.__input0 == False or self.__input1 == False:
			self.__output = False
		elif self.__input0 == self.__input1 == True:
			self.__output = True
		else:
			self.__output = None
		return

	@property
	def input0(self):
		return self.__input0

	@input0.setter
	def input0(self, value):
		self.__input0 = value
		self.__execute()

	@property
	def input1(self):
		return self.__input1

	@input1.setter
	def input1(self, value):
		self.__input1 = value
		self.__execute()

	@property
	def output(self):
		return self.__output


class LogicalOr:
	def __init__(self, input0 = None, input1 = None, name = "OR"):
		self.__input0 = input0
		self.__input1 = input1
		self.__output = None
		self.name = name
		self.__execute()

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; input0: " + str(self.input0) + \
				"; input1: " + str(self.input1) + \
				"; output: " + str(self.output) + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		print(str(output))
		return

	def __execute(self):
		if self.__input0 == True:
			self.__output = True
		elif self.__input1 == True:
			self.__output = True
		elif self.__input0 == self.__input1 == False:
			self.__output = False
		else:
			self.__output = None
		return

	@property
	def input0(self):
		return self.__input0

	@input0.setter
	def input0(self, value):
		self.__input0 = value
		self.__execute()

	@property
	def input1(self):
		return self.__input1

	@input1.setter
	def input1(self, value):
		self.__input1 = value
		self.__execute()

	@property
	def output(self):
		return self.__output
