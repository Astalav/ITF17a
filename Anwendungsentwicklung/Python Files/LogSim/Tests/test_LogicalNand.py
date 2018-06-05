# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalNand
import pytest

def testInit():
	myAnd = LogicalNand("FunnyName", True, True)
	assert myAnd.getInput(0) == True
	assert myAnd.getInput(1) == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalNand("FunnyName",False, False)
	assert myAnd.getOutput() == True

def testOutput01():
	myAnd = LogicalNand("FunnyName",False, True)
	assert myAnd.getOutput() == True

def testOutput10():
	myAnd = LogicalNand("FunnyName",True, False)
	assert myAnd.getOutput() == True

def testOutput11():
	myAnd = LogicalNand("FunnyName",True, True)
	assert myAnd.getOutput() == False

def testOutputNone():
	myAnd = LogicalNand("FunnyName",True, "blöblö")
	assert myAnd.getOutput() is None

def testOutput5InputsTrue():
	myAnd = LogicalNand("FunnyName", True, False, True, False, True)
	assert myAnd.getOutput() == True

def testOutput5InputsFalse():
	myAnd = LogicalNand("FunnyName", True, True, True, True, True)
	assert myAnd.getOutput() == False

def testLogicalAndToString():
	myAnd = LogicalNand("FunnyName", True, False)
	assert "[class: LogicalNand; name: FunnyName;]" == str(myAnd)