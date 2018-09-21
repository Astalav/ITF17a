# -*- coding: utf8 -*-
from abc import ABC, abstractmethod
#from ShowStrategy import * 
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
			self.name = name
		#self._showClass = ShowEasy()

	def __str__(self):
		return "[class: " + self.__class__.__name__ + \
				"; name: " + str(self.name) + ";]"

	def show(self):
		return self._showClass.show(self)

	@abstractmethod
	def _execute(self):
		pass

	def setInput(self, *bools):
		if len(bools) == 0:
			self.__output = None
			return

		for boolVal in bools:
			if not isinstance(boolVal, bool):
				self.__output = None
				return

		self._input = bools
		#print("Class: " + self.__class__.__name__ + " || Input: " + str(self.getInputList()))
		self._execute()

	def _setOutputInvalid(self):
		self.__output = None

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

class LogicalHalfAdder(LogicalGate):
	def __init__(self, name = None, *bools):
		self.__logXOR = LogicalXor()
		self.__logAND = LogicalAnd()
		super(LogicalHalfAdder, self).__init__(name, *bools)

	def _execute(self):
		self.__logXOR.setInput(self._input[0], self._input[1])
		self.__logAND.setInput(self._input[0], self._input[1])

		self._setOutput(self.__logXOR.getOutput(), self.__logAND.getOutput())

	def setInput(self, *bools):
		if len(bools) == 2:
			super(LogicalHalfAdder, self).setInput(*bools)
		else:
			self._setOutputInvalid()

	def getSum(self):
		return self.getOutput()

	def getCarry(self):
		return self.getOutput(1)

class LogicalFullAdder(LogicalGate):
	def __init__(self, name = None, *bools):
		self.__logHA1 = LogicalHalfAdder()
		self.__logHA2 = LogicalHalfAdder()
		self.__logOR = LogicalOr()
		super(LogicalFullAdder, self).__init__(name, *bools)

	def _execute(self):
		self.__logHA1.setInput(self._input[0], self._input[1])
		self.__logHA2.setInput(self.__logHA1.getSum(), self._input[2])
		self.__logOR.setInput(self.__logHA1.getCarry(), self.__logHA2.getCarry())

		self._setOutput(self.__logHA2.getSum(), self.__logOR.getOutput())

	def setInput(self, *bools):
		if len(bools) == 3:
			super(LogicalFullAdder, self).setInput(*bools)
		else:
			self._setOutputInvalid()

	def getSum(self):
		return self.getOutput()

	def getCarry(self):
		return self.getOutput(1)

class Logical4BitAdder(LogicalGate):
	def __init__(self, name = None, *bools):
		self.__carryIn = False

		self.__logFA1 = LogicalFullAdder()
		self.__logFA2 = LogicalFullAdder()
		self.__logFA3 = LogicalFullAdder()
		self.__logFA4 = LogicalFullAdder()

		super(Logical4BitAdder, self).__init__(name, *bools)

	def _execute(self):
		self.__logFA1.setInput(self.__carryIn, self._input[0], self._input[4])
		self.__logFA2.setInput(self.__logFA1.getCarry(), self._input[1], self._input[5])
		self.__logFA3.setInput(self.__logFA2.getCarry(), self._input[2], self._input[6])
		self.__logFA4.setInput(self.__logFA3.getCarry(), self._input[3], self._input[7])

		self._setOutput(self.__logFA4.getSum(),
						self.__logFA3.getSum(),
						self.__logFA2.getSum(),
						self.__logFA1.getSum(),
						self.__logFA4.getCarry())

	def setInput(self, *bools):
		if len(bools) == 8:
			super(Logical4BitAdder, self).setInput(*bools)
		elif len(bools) == 9:
			self.__carryIn = bools[8]
			super(Logical4BitAdder, self).setInput(*bools)
		else:
			self._setOutputInvalid()

	def getSum(self, getAt = 0):
		if getAt <= 3 and getAt >= 0:
			return self.getOutput(getAt)
		return None

	def getCarry(self):
		return self.getOutput(4)

class Logical8BitAdder(LogicalGate):
	def __init__(self, name = None, *bools):
		self.__carryIn = False
		self.__log4BA1 = Logical4BitAdder()
		self.__log4BA2 = Logical4BitAdder()

		super(Logical8BitAdder, self).__init__(name, *bools)

	def _execute(self):
		self.__log4BA1.setInput(self._input[15], 
								 self._input[14], 
								 self._input[13], 
								 self._input[12], 
								 self._input[7],
								 self._input[6], 
								 self._input[5], 
								 self._input[4],
								 self.__carryIn)

		self.__log4BA2.setInput(self._input[11], 
								 self._input[10], 
								 self._input[9], 
								 self._input[8], 
								 self._input[3],
								 self._input[2], 
								 self._input[1], 
								 self._input[0],
								 self.__log4BA1.getCarry())
								 
		

		self._setOutput(self.__log4BA2.getSum(0),
						self.__log4BA2.getSum(1),
						self.__log4BA2.getSum(2),
						self.__log4BA2.getSum(3),
						self.__log4BA1.getSum(0),
						self.__log4BA1.getSum(1),
						self.__log4BA1.getSum(2),
						self.__log4BA1.getSum(3),
						self.__log4BA2.getCarry())

	def setInput(self, *bools):
		if len(bools) == 16:
			super(Logical8BitAdder, self).setInput(*bools)
		elif len(bools) == 17:
			self.__carryIn = bools[16]
			super(Logical8BitAdder, self).setInput(*bools)
		else:
			self._setOutputInvalid()

	def getSum(self, getAt = 0):
		if getAt <= 15 and getAt >= 0:
			return self.getOutput(getAt)
		return None

	def getCarry(self):
		return self.getOutput(8)