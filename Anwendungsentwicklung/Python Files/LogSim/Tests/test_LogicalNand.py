# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalNand
import pytest

print("bla")

def testInit():
	myAnd = LogicalNand(True, True, "FunnyName")
	assert myAnd.input0 == True
	assert myAnd.input1 == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalNand(False, False, "FunnyName")
	assert myAnd.output == True

def testOutput01():
	myAnd = LogicalNand(False, True, "FunnyName")
	assert myAnd.output == True

def testOutput10():
	myAnd = LogicalNand(True, False, "FunnyName")
	assert myAnd.output == True

def testOutput11():
	myAnd = LogicalNand(True, True, "FunnyName")
	assert myAnd.output == False

def testOutputNone():
	myAnd = LogicalNand(True, "blöblö", "FunnyName")
	assert myAnd.output is None

def testLogicalAndToString():
	myAnd = LogicalNand(True, False, "FunnyName")
	assert "[class: LogicalNand; input0: True; input1: False; output: True; name: FunnyName;]" == str(myAnd)