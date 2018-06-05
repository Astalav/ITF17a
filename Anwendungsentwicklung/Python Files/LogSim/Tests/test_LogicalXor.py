# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalXor
import pytest

def testInit():
	myAnd = LogicalXor("FunnyName", True, True)
	assert myAnd.getInput(0) == True
	assert myAnd.getInput(1) == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalXor("FunnyName", False, False)
	assert myAnd.getOutput() == False

def testOutput01():
	myAnd = LogicalXor("FunnyName", False, True)
	assert myAnd.getOutput() == True

def testOutput10():
	myAnd = LogicalXor("FunnyName", True, False)
	assert myAnd.getOutput() == True

def testOutput11():
	myAnd = LogicalXor("FunnyName", True, True)
	assert myAnd.getOutput() == False

def testOutputNone():
	myAnd = LogicalXor("FunnyName", "vlöpdiböp", "blöblö")
	assert myAnd.getOutput() is None

def testOutput5InputsTrue():
	myAnd = LogicalXor("FunnyName", True, True, True, True, True)
	assert myAnd.getOutput() == True

def testOutput5InputsFalse():
	myAnd = LogicalXor("FunnyName", True, False, True, False, False)
	assert myAnd.getOutput() == False

def testLogicalAndToString():
	myAnd = LogicalXor("FunnyName", True, False)
	assert "[class: LogicalXor; name: FunnyName;]" == str(myAnd)