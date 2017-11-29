# -*- coding: utf8 -*-

from decimal import *
import locale

def run():
	welcomeMessage(20)

	locale.setlocale(locale.LC_ALL, '')

	creditSum = getUserDecimalInput("Please enter your credit sum:", minValue=0)

	interest = getUserDecimalInput("Please enter your interest in %:", minValue=0, maxValue=10, maxAsWarning=True) # /Decimal(100)

	time = Decimal(input("Please enter the time your credit runs in years:"))
	if time <= 0:
		print("Error: Your entered time is smaller than or equal to 0. Please enter a valid number next time!")
		return
	
	#print(locale.currency(calcEndfaehigesDarlehenGesamt(leihbetrag,laufzeit,zins), grouping=True))



def getUserDecimalInput(inputString, minValue=Decimal(-Infinity), minAsWarning=False, maxValue=Decimal(Infinity), maxAsWarning=False):
	userInputDecimal = Decimal(input(inputString+":"))

	if userInputDecimal <= minValue:
		if minAsWarning:
			print("Warning: Your input was smaller than or equal to %d!", minValue)
			return userInputDecimal
		else:
			print("Error: Your input was smaller than or equal to %d! Please enter a valid number next time!", minValue)
			return Decimal(NaN)

	if userInputDecimal >= maxValue:
		if maxAsWarning:
			print("Warning: Your input was greater than or equal to %d!", maxValue)
			return userInputDecimal
		else:
			print("Error: Your input was greater than or equal to %d! Please enter a valid number next time!", maxValue)
			return Decimal(NaN)

def welcomeMessage(size):
	startEndStars = 2 * "* "
	
	if size < 16:
		size = 16

	line1n7 = startEndStars + size * "* " + startEndStars
	line2n6 = startEndStars + size * "  " + startEndStars

	line3   = startEndStars + ("{:^" + str(size*2) + "}").format("Welcome to this Calculator      ") + startEndStars
	line4   = startEndStars + ("{:^" + str(size*2) + "}").format("Version: 0.1 vom 23.11.2017     ") + startEndStars
	line5   = startEndStars + ("{:^" + str(size*2) + "}").format("Fehler bitte an david@tbs1.de   ") + startEndStars

	print(line1n7)
	print(line2n6)
	print(line3)
	print(line4)
	print(line5)
	print(line2n6)
	print(line1n7)