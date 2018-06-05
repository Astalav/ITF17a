# -*- coding: utf8 -*-
from abc import ABC, abstractmethod
import types

__version__ = "1.3.1.6"
__author__ = "Astalav"

class LogicalGate(ABC):
	def __init__(self, name = None, *bools):
		self._input = []
		self.setInput(*bools)

		if name == None:
			self.name = self.__class__.__name__
		else:
			self.name = name # string

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		print(str(output))
		return

	@abstractmethod
	def _execute(self):
		pass

	def setInput(self, *bools):
		for boolVal in bools:
			if not isinstance(boolVal, bool):
				self.__output = None
				return

		self._input = bools
		self._execute()

	def _setOutput(self, *bools):
		self.__output = bools

	def getInputList(self):
		return self._input

	def getOutputList(self):
		return self.__output

	def getOutput(self, getAt = 0):
		if not isinstance(self.__output, type(None)):
			return self.__output[getAt]
		return None

	def getInput(self, getAt = 0):
		return self._input[getAt]


class LogicalAnd(LogicalGate):
	def _execute(self):
		output = True
		for boolVal in self._input:
			if boolVal == False:
				output = False
				break

		self._setOutput(output)

class LogicalOr(LogicalGate):
	def _execute(self):
		output = False

		for boolVal in self._input:
			if boolVal == True and output == False:
				output = True
				break

		self._setOutput(output)

class LogicalXor(LogicalGate):
	def _execute(self):
		output = False

		for boolVal in self._input:
			if boolVal == True:
				output = not output

		self._setOutput(output)

class LogicalNand(LogicalGate):
	def _execute(self):
		output = False
		for boolVal in self._input:
			if boolVal == False:
				output = True
				break

		self._setOutput(output)