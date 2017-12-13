# -*- coding: utf8 -*-

from decimal import *
import locale

def run():
	welcomeMessage(20)

	locale.setlocale(locale.LC_ALL, '')

	creditSum = getUserDecimalInput("Please enter your credit sum", minValue=0)
	if creditSum == Decimal("NaN"):
		return

	interest = getUserDecimalInput("Please enter your interest in %", minValue=0, maxValue=10, maxAsWarning=True)
	if interest == Decimal("NaN"):
		return
	else:
		interest = interest/Decimal(100)

	time = getUserDecimalInput("Please enter the time your credit runs in years", minValue=0, maxValue=50, maxAsWarning=True)
	if time == Decimal("NaN"):
		return
	
	print(locale.currency(calcAnnuDarlehen(creditSum, interest, time), grouping=True))
	return calcAnnuDarlehen(creditSum, interest, time)


def calcAnnuDarlehen(creditSum, interest, time):
	annu = creditSum * ((((1+interest)**time)*interest) / (((1+interest)**time)-1))
	return annu

def getUserDecimalInput(inputString, minValue=Decimal("-Infinity"), minAsWarning=False, maxValue=Decimal("Infinity"), maxAsWarning=False):
	userInputDecimal = input(inputString+":")
	try:
		userInputDecimal = int(userInputDecimal)       
	except ValueError:
		print("Error: Your imput was not a number! Please enter a number next time!")
		return Decimal("NaN")

	if userInputDecimal <= minValue:
		if minAsWarning:
			print("Warning: Your input was smaller than or equal to %s!"% minValue)
			return Decimal(userInputDecimal)
		else:
			print("Error: Your input was smaller than or equal to %s! Please enter a valid number next time!"% minValue)
			return Decimal("NaN")

	if userInputDecimal >= maxValue:
		if maxAsWarning:
			print("Warning: Your input was greater than or equal to %s!"% str(maxValue))
			return Decimal(userInputDecimal)
		else:
			print("Error: Your input was greater than or equal to %s! Please enter a valid number next time!"% maxValue)
			return Decimal(NaN)

	return Decimal(userInputDecimal)


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

run()