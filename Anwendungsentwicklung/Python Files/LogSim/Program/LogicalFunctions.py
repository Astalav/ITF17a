# -*- coding: utf8 -*-
from abc import ABC, abstractmethod

__version__ = "1.1"
__author__ = "Astalav"

class LogicalGate(ABC):
	def __init__(self, input0 = None, input1 = None, name = None):
		self._input0 = input0
		self._input1 = input1
		self._output = None
		
		if name == None:
			self.name = self.__class__.__name__
		else:
			self.name = name

		self._execute()

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; input0: " + str(self._input0) + \
				"; input1: " + str(self._input1) + \
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
		return self._input0

	@input0.setter
	def input0(self, value):
		self._input0 = value
		self._execute()

	@property
	def input1(self):
		return self._input1

	@input1.setter
	def input1(self, value):
		self._input1 = value
		self._execute()

	@property
	def output(self):
		return self._output


class LogicalAnd(LogicalGate):
	def _execute(self):
		if self._input0 == False or self._input1 == False:
			self._output = False
		elif self._input0 == self._input1 == True:
			self._output = True
		else:
			self._output = None
		return


class LogicalOr(LogicalGate):
	def _execute(self):
		if self._input0 == True:
			self._output = True
		elif self._input1 == True:
			self._output = True
		elif self._input0 == self._input1 == False:
			self._output = False
		else:
			self._output = None
		return

class LogicalXor(LogicalGate):
	def _execute(self):
		if (self._input0 == True and self._input1 == False) or (self._input0 == False and self._input1 == True):
			self._output = True
		elif (self._input1 == self._input0 == True) or (self._input1 == self._input0 == False):
			self._output = False
		else:
			self._output = None
		return
