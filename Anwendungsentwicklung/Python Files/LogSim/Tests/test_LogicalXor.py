# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/../Program"))
from LogicalFunctions import LogicalXor
import pytest

def testInit():
	myAnd = LogicalXor(True, True, "FunnyName")
	assert myAnd.input0 == True
	assert myAnd.input1 == True
	assert myAnd.name == "FunnyName"

def testOutput00():
	myAnd = LogicalXor(False, False, "FunnyName")
	assert myAnd.output == False

def testOutput01():
	myAnd = LogicalXor(False, True, "FunnyName")
	assert myAnd.output == True

def testOutput10():
	myAnd = LogicalXor(True, False, "FunnyName")
	assert myAnd.output == True

def testOutput11():
	myAnd = LogicalXor(True, True, "FunnyName")
	assert myAnd.output == False

def testOutputNone():
	myAnd = LogicalXor("vlöpdiböp", "blöblö", "FunnyName")
	assert myAnd.output is None

def testLogicalAndToString():
	myAnd = LogicalXor(True, False, "FunnyName")
	assert "[class: LogicalXor; input0: True; input1: False; output: True; name: FunnyName;]" == str(myAnd)