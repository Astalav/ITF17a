import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/.."))
from Program import annuDarlehen

def testAnnuDarlehen():
	assert 21835.457140057595 == annuDarlehen.calcAnnuDarlehen(100000, 0.03, 5)