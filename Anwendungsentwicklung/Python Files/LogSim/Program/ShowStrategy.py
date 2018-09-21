from abc import ABC, abstractmethod
from LogicalFunctions import *

class IShowStrat(ABC):
	"""
	Shall work as an Interface
	"""
	@abstractmethod
	def show(self):
		pass

class ShowEasy(IShowStrat):
	def show(self, obj):
		print(str(obj))
		return str(obj)

class ShowMultiBitAdder(IShowStrat):
	def show(self, obj):
		
		inputList = obj.getInputList()
		outputList = obj.getOutputList()

		inputLen = len(inputList)
		outputLen = len(outputList)

		inputCarry = False
		outputCarry = False

		if (inputLen%2)==1:
			inputLen = inputLen - 1
			inputCarry = True

		if (outputLen%2)==1:
			outputLen = outputLen - 1
			outputCarry = True

		bitNumber1 = []
		bitNumber2 = []
		sumNumber = []

		for i in range(0, int(inputLen/2)):
			bitNumber1.append(inputList[i])
		for i in range(int((inputLen/2)), inputLen):
			bitNumber2.append(inputList[i])
		for i in range(0, outputLen):
			sumNumber.append(outputList[i])


		output = ""

		if inputCarry == True:
			output = output + "CarryIn: " + str(int(inputList[inputLen])) + "\n"

		for a in bitNumber1:
			output = output + str(int(a)) + " "
		output = output + "\n"

		for a in bitNumber2:
			output = output + str(int(a)) + " "
		output = output + "+\n"

		output = output + outputLen*"__" + "_"
		output = output + "\n"

		for a in sumNumber:
			output = output + str(int(a)) + " "
		output = output + "=\n"

		if outputCarry == True:
			output = output + "CarryOut: " + str(int(outputList[outputLen]))

		print(output)


strat = ShowMultiBitAdder()
strat.show(Logical8BitAdder("test", True,False,False,False,True,False,False,False,
									True,False,False,False,True,False,False,False,
									True))