import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/.."))
from Program import darlehen

def testEnfaelligesDarlehenGesamt():
	assert 125000 == darlehen.calcEndfaehigesDarlehenGesamt(100000, 5, 0.05)