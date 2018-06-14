# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import Logical8BitAdder
import pytest

def testInit():
	my8BitAdder = Logical8BitAdder("FunnyName", True, False, True, False, True, False, True, False,
												True, False, True, False, True, False, True, False,
												False)
	assert my8BitAdder.getInput(0) == True
	assert my8BitAdder.getInput(1) == False
	assert my8BitAdder.getInput(2) == True
	assert my8BitAdder.getInput(3) == False
	assert my8BitAdder.getInput(4) == True
	assert my8BitAdder.getInput(5) == False
	assert my8BitAdder.getInput(6) == True
	assert my8BitAdder.getInput(7) == False
	assert my8BitAdder.getInput(8) == True
	assert my8BitAdder.getInput(9) == False
	assert my8BitAdder.getInput(10) == True
	assert my8BitAdder.getInput(11) == False
	assert my8BitAdder.getInput(12) == True
	assert my8BitAdder.getInput(13) == False
	assert my8BitAdder.getInput(14) == True
	assert my8BitAdder.getInput(15) == False
	assert my8BitAdder.getInput(16) == False
	assert my8BitAdder.name == "FunnyName"

def testAdd():
	my8BitAdder = Logical8BitAdder("FunnyName", True, True, True, True, True, True, True, True,
												False, False, False, False, False, False, False, False,
												True)
	
	assert my8BitAdder.getCarry() == True
	assert my8BitAdder.getSum(0) == False
	assert my8BitAdder.getSum(1) == False
	assert my8BitAdder.getSum(2) == False
	assert my8BitAdder.getSum(3) == False
	assert my8BitAdder.getSum(4) == False
	assert my8BitAdder.getSum(5) == False
	assert my8BitAdder.getSum(6) == False
	assert my8BitAdder.getSum(7) == False

def testOutputInvalidInputCount1():
	my8BitAdder = Logical8BitAdder("FunnyName", True)
	assert my8BitAdder.getSum() == None
	assert my8BitAdder.getCarry() == None

def testOutputInvalidInputCount2():
	my8BitAdder = Logical8BitAdder("FunnyName", True, True, True)
	assert my8BitAdder.getSum() == None
	assert my8BitAdder.getCarry() == None

def testOutputInvalidInputFormat():
	my8BitAdder = Logical8BitAdder("FunnyName", "bla", "bli")
	assert my8BitAdder.getSum() == None
	assert my8BitAdder.getCarry() == None

def testLogicalAndToString():
	my8BitAdder = Logical8BitAdder("FunnyName", True, False)
	assert "[class: Logical8BitAdder; name: FunnyName;]" == str(my8BitAdder)