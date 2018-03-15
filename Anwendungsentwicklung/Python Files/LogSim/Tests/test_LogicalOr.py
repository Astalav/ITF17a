# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalOr
import pytest

def testInit():
	myAnd = LogicalOr(True, True, "FunnyName")
	assert myAnd.input0 == True
	assert myAnd.input1 == True
	assert myAnd.name == "FunnyName"

def testOutputTrue():
	myAnd = LogicalOr(True, True, "FunnyName")
	assert myAnd.output == True

def testOutputFalse():
	myAnd = LogicalOr(True, False, "FunnyName")
	assert myAnd.output == True

#def testOutputNone():
#	myAnd = LogicalOr(True, "blöblö", "FunnyName")
#	assert myAnd.output is None

def testLogicalAndToString():
	myAnd = LogicalOr(True, False, "FunnyName")
	assert "[class: LogicalOr; input0: True; input1: False; output: True; name: FunnyName;]" == str(myAnd)