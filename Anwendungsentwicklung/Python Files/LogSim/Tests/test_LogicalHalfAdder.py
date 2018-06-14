# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalHalfAdder
import pytest

def testInit():
	myHalfAdder = LogicalHalfAdder("FunnyName", True, True)
	assert myHalfAdder.getInput(0) == True
	assert myHalfAdder.getInput(1) == True
	assert myHalfAdder.name == "FunnyName"

def testOutput00():
	myHalfAdder = LogicalHalfAdder("FunnyName", False, False)
	assert myHalfAdder.getSum() == False
	assert myHalfAdder.getCarry() == False

def testOutput01():
	myHalfAdder = LogicalHalfAdder("FunnyName", False, True)
	assert myHalfAdder.getSum() == True
	assert myHalfAdder.getCarry() == False

def testOutput10():
	myHalfAdder = LogicalHalfAdder("FunnyName", True, False)
	assert myHalfAdder.getSum() == True
	assert myHalfAdder.getCarry() == False

def testOutput11():
	myHalfAdder = LogicalHalfAdder("FunnyName", True, True)
	assert myHalfAdder.getSum() == False
	assert myHalfAdder.getCarry() == True

def testOutputInvalidInputCount1():
	myHalfAdder = LogicalHalfAdder("FunnyName", True)
	assert myHalfAdder.getSum() == None
	assert myHalfAdder.getCarry() == None

def testOutputInvalidInputCount2():
	myHalfAdder = LogicalHalfAdder("FunnyName", True, True, True)
	assert myHalfAdder.getSum() == None
	assert myHalfAdder.getCarry() == None

def testOutputInvalidInputFormat():
	myHalfAdder = LogicalHalfAdder("FunnyName", "bla", "bli")
	assert myHalfAdder.getSum() == None
	assert myHalfAdder.getCarry() == None

def testLogicalAndToString():
	myHalfAdder = LogicalHalfAdder("FunnyName", True, False)
	assert "[class: LogicalHalfAdder; name: FunnyName;]" == str(myHalfAdder)