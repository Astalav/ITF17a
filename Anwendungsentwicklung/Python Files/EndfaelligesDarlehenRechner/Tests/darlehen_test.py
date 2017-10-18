import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/.."))
from Program import darlehen

def test():
	assert 2 == darlehen.calcEndfaehigesDarlehenGesamt(1, 1, 1)