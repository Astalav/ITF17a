# -*- coding: utf8 -*-

from decimal import *
import locale

def startupPrint(size):
	startEndStars = 2 * "* "
	
	if size < 16:
		size = 16

	line1n7 = startEndStars + size * "* " + startEndStars
	line2n6 = startEndStars + size * "  " + startEndStars

	line3   = startEndStars + ("{:^" + str(size*2) + "}").format("Willkommen zum Darlehensrechner ") + startEndStars
	line4   = startEndStars + ("{:^" + str(size*2) + "}").format("Version: 0.1 vom 07.09.2017     ") + startEndStars
	line5   = startEndStars + ("{:^" + str(size*2) + "}").format("Fehler bitte an david@tbs1.de   ") + startEndStars

	print(line1n7)
	print(line2n6)
	print(line3)
	print(line4)
	print(line5)
	print(line2n6)
	print(line1n7)

def calcEndfaehigesDarlehenGesamt(Leihbetrag, Jahre, ZinsAsFloat):
	return (Leihbetrag + calcEndfaehigesDarlehenZins(Leihbetrag, Jahre, ZinsAsFloat))

def calcEndfaehigesDarlehenZins(Leihbetrag, Jahre, ZinsAsFloat):
	return (Jahre * (Leihbetrag * ZinsAsFloat))

def darlehensrechner():
	locale.setlocale(locale.LC_ALL, '')
	startupPrint(50)

	leihbetrag = Decimal(input("Bitte Leihbetrag eingeben: "))
	zins = Decimal(input("Bitte Zinssatz in % eingeben: "))/Decimal(100)
	laufzeit = Decimal(input("Bitte Laufzeit in Jahren eingeben "))
	
	print(locale.currency(calcEndfaehigesDarlehenGesamt(leihbetrag,laufzeit,zins), grouping=True))