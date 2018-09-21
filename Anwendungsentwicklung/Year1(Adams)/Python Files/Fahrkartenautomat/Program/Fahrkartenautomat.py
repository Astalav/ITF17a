# -*- coding: utf8 -*-

from decimal import *
import locale
import math

locale.setlocale(locale.LC_ALL, '')

class Fahrkartenautomat(object):
	def __init__(self):
		self.currency = [	Decimal(500),
							Decimal(200), 
							Decimal(100), 
							Decimal(50), 
							Decimal(20), 
							Decimal(10), 
							Decimal(5), 
							Decimal(2), 
							Decimal(1), 
							Decimal(0.5), 
							Decimal(0.2), 
							Decimal(0.1), 
							Decimal(0.05), 
							Decimal(0.02), 
							Decimal(0.01)]
		self.currencyCount = [10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
		self.price = Decimal(2.70)
		self.value = Decimal(100)

	def AddCurrency(self):
		pass

	def returnChange(self):
		change = Decimal(self.value) -  Decimal(self.price)

		for i in range(0, len(self.currency)):
			while (self.currencyCount[i] > 0 and self.currency[i] < change):
				change = change - self.currency[i]
				self.currencyCount[i] = self.currencyCount[i] - 1
				print("Folgende Währung wurde ausgegeben: " + str(self.currency[i]))

			if change == 0:
				break
	
		print("")
		print("Übriges Geld: " + str(change))

		pass

fka = Fahrkartenautomat()
fka.returnChange()