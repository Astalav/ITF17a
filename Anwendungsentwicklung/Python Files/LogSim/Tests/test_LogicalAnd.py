# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalAnd
import pytest

print("bla")

def testInit():
	myAnd = LogicalAnd(True, True, "FunnyName")
	assert myAnd.input0 == True
	assert myAnd.input1 == True
	assert myAnd.name == "FunnyName"

def testOutputTrue():
	myAnd = LogicalAnd(True, True, "FunnyName")
	assert myAnd.output == True

def testOutputFalse():
	myAnd = LogicalAnd(True, False, "FunnyName")
	assert myAnd.output == False

def testOutputNone():
	myAnd = LogicalAnd(True, "blöblö", "FunnyName")
	assert myAnd.output is None

def testLogicalAndToString():
	myAnd = LogicalAnd(True, False, "FunnyName")
	assert "[class: LogicalAnd; input0: True; input1: False; output: False; name: FunnyName;]" == str(myAnd)