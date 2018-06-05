# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalOr
import pytest

def testInit():
	myAnd = LogicalOr("FunnyName", True, True)
	assert myAnd.getInput(0) == True
	assert myAnd.getInput(1) == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalOr("FunnyName", False, False)
	assert myAnd.getOutput() == False

def testOutput01():
	myAnd = LogicalOr("FunnyName", False, True)
	assert myAnd.getOutput() == True

def testOutput10():
	myAnd = LogicalOr("FunnyName", True, False)
	assert myAnd.getOutput() == True

def testOutput11():
	myAnd = LogicalOr("FunnyName", True, True)
	assert myAnd.getOutput() == True

def testOutputNone():
	myAnd = LogicalOr("FunnyName", "vlöpdiböp", "blöblö")
	assert myAnd.getOutput() is None

def testOutput5InputsTrue():
	myAnd = LogicalOr("FunnyName", True, True, False, True, False)
	assert myAnd.getOutput() == True

def testOutput5InputsFalse():
	myAnd = LogicalOr("FunnyName", False, False, False, False, False)
	assert myAnd.getOutput() == False

def testLogicalAndToString():
	myAnd = LogicalOr("FunnyName", True, False)
	assert "[class: LogicalOr; name: FunnyName;]" == str(myAnd)