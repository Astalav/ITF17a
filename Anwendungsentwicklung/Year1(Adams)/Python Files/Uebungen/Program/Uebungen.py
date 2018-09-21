# -*- coding: utf8 -*-

from decimal import *
import locale
import math

locale.setlocale(locale.LC_ALL, '')

def fibonacci(zahl):
	if zahl <= 0:
		return 0
	elif zahl == 1:
		return 1
	else:
		return fibonacci(zahl - 1) + fibonacci(zahl - 2)

def collatz(number):
	print(number)

	if number <= 1:
		return 
	elif (number % 2) == 0:
		return collatz(number/2)
	else:
		return collatz((3*number) + 1)

def collatz(number, stream):
	stream.write(str(number) + '\n')

	if number <= 1:
		return 
	elif (number % 2) == 0:
		return collatz(number/2, stream)
	else:
		return collatz((3*number) + 1, stream)

def collatz_writer(number):
	stream = open("Collatznumbers/Collatz" + str(number) + ".txt", "w")

	collatz(number, stream)

	stream.close()

def collatz_loop():
	for i in range(4, 1001):
		collatz_writer(i)

def collatzCallCounter(number, calls = 0):
	calls = calls + 1

	if number <= 1:
		return calls
	elif (number % 2) == 0:
		return collatzCallCounter(number/2, calls)
	else:
		return collatzCallCounter((3*number) + 1, calls)

def collatzCallCounterLoop():
	stream = open("CollatzCount.txt", "w")
	for i in range(4, 1001):
		stream.write(str(collatzCallCounter(i)) + '\n')

def binarySearchIntern(array, value, first, last):
	mid = (first + last)//2

	if array[mid] == value:
		return mid
	elif array[mid] > value:
		return binarySearchIntern(array, value, first, (mid-1))
	elif array[mid] < value:
		return binarySearchIntern(array, value, (mid+1), last)

def binarySearch(array, value):
	return binarySearchIntern(array, value, 0, (len(array)-1))