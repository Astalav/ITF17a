# -*- coding: utf8 -*-
from abc import ABC, abstractmethod

__version__ = "1.1"
__author__ = "Astalav"

class LogicalGate(ABC):
	def __init__(self, input0 = None, input1 = None, name = None):
		self.__input0 = input0 	# bool
		self.__input1 = input1 	# bool
		self._output = None 	# bool

		if name == None:
			self.name = self.__class__.__name__
		else:
			self.name = name # string

		self._execute()

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; input0: " + str(self.__input0) + \
				"; input1: " + str(self.__input1) + \
				"; output: " + str(self._output) + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		print(str(output))
		return

	@abstractmethod
	def _execute(self):
		pass

	@property
	def input0(self):
		return self.__input0

	@input0.setter
	def input0(self, value):
		self.__input0 = value
		self._execute()

	@property
	def input1(self):
		return self.__input1

	@input1.setter
	def input1(self, value):
		self.__input1 = value
		self._execute()

	@property
	def output(self):
		return self._output


class LogicalAnd(LogicalGate):
	def _execute(self):
		if self.input0 == False or self.input1 == False:
			self._output = False
		elif self.input0 == self.input1 == True:
			self._output = True
		else:
			self._output = None
		return


class LogicalOr(LogicalGate):
	def _execute(self):
		if self.input0 == True:
			self._output = True
		elif self.input1 == True:
			self._output = True
		elif self.input0 == self.input1 == False:
			self._output = False
		else:
			self._output = None
		return

class LogicalXor(LogicalGate):
	def _execute(self):
		if (self.input0 == True  and self.input1 == False) \
		or (self.input0 == False and self.input1 == True):
			self._output = True
		elif (self.input1 == self.input0 == True) \
		or   (self.input1 == self.input0 == False):
			self._output = False
		else:
			self._output = None
		return

class LogicalNand(LogicalGate):
	def _execute(self):
		if self.input0 == False or self.input1 == False:
			self._output = True
		elif self.input0 == self.input1 == True:
			self._output = False
		else:
			self._output = None
		return