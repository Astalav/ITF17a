# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalFullAdder
import pytest

def testInit():
	myFullAdder = LogicalFullAdder("FunnyName", True, True, True)
	assert myFullAdder.getInput(0) == True
	assert myFullAdder.getInput(1) == True
	assert myFullAdder.getInput(2) == True
	assert myFullAdder.name == "FunnyName"

def testOutput000():
	myFullAdder = LogicalFullAdder("FunnyName", False, False, False)
	assert myFullAdder.getSum() == False
	assert myFullAdder.getCarry() == False

def testOutput010():
	myFullAdder = LogicalFullAdder("FunnyName", False, True, False)
	assert myFullAdder.getSum() == True
	assert myFullAdder.getCarry() == False

def testOutput100():
	myFullAdder = LogicalFullAdder("FunnyName", True, False, False)
	assert myFullAdder.getSum() == True
	assert myFullAdder.getCarry() == False

def testOutput110():
	myFullAdder = LogicalFullAdder("FunnyName", True, True, False)
	assert myFullAdder.getSum() == False
	assert myFullAdder.getCarry() == True

def testOutputInvalidInputCount1():
	myFullAdder = LogicalFullAdder("FunnyName", True, True)
	assert myFullAdder.getSum() == None
	assert myFullAdder.getCarry() == None

def testOutputInvalidInputCount2():
	myFullAdder = LogicalFullAdder("FunnyName", True, True, True, True)
	assert myFullAdder.getSum() == None
	assert myFullAdder.getCarry() == None

def testOutputInvalidInputFormat():
	myFullAdder = LogicalFullAdder("FunnyName", "bla", "bli", "blo")
	assert myFullAdder.getSum() == None
	assert myFullAdder.getCarry() == None

def testLogicalAndToString():
	myFullAdder = LogicalFullAdder("FunnyName", True, False)
	assert "[class: LogicalFullAdder; name: FunnyName;]" == str(myFullAdder)