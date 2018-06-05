# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalAnd
import pytest

def testInit():
	myAnd = LogicalAnd("FunnyName", True, True)
	assert myAnd.getInput(0) == True
	assert myAnd.getInput(1) == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalAnd("FunnyName",False, False)
	assert myAnd.getOutput() == False

def testOutput01():
	myAnd = LogicalAnd("FunnyName", False, True)
	assert myAnd.getOutput() == False

def testOutput10():
	myAnd = LogicalAnd("FunnyName", True, False)
	assert myAnd.getOutput() == False

def testOutput11():
	myAnd = LogicalAnd("FunnyName", True, True)
	assert myAnd.getOutput() == True

def testOutputNone():
	myAnd = LogicalAnd("FunnyName", True, "blöblö")
	assert myAnd.getOutput() is None

def testOutput5InputsTrue():
	myAnd = LogicalAnd("FunnyName", True, True, True, True, True)
	assert myAnd.getOutput() == True

def testOutput5InputsFalse():
	myAnd = LogicalAnd("FunnyName", True, False, True, True, True)
	assert myAnd.getOutput() == False

def testLogicalAndToString():
	myAnd = LogicalAnd("FunnyName", True, False)
	assert "[class: LogicalAnd; name: FunnyName;]" == str(myAnd)