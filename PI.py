import math
import random
from mpmath import *
import os
import sys

mp.dps = 20000

#Definite integrals

def confirm(pi):
	pi = str(pi)
	length = len(pi)
	file = open("confirm.txt")
	with open("confirm.txt") as f:
  		for i in range(length):
		  	c = f.read(1)
			if c != pi[i]:
				print "confirmed up to digit: " + str(i)
				string = ""
				for j in range(i):
					string += pi[j]
				print string
				return 0
    		if not c:
      			return "End of file"
      			
   
	return "confirmed"

def clear():
	os.system("clear") 

def fx(x):
	return math.sqrt(1 - x**2)

def definiteIntegral(a, b, n):
	Sum = 0
	x = a
	deltax = float(b - a)/n
	
	for i in range(n):
		Sum += fx(x) * deltax 
		x += deltax
	return Sum

def distance(pos1, pos2):
	return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1]) ** 2)
	
def monteCarlo(k):
	square = 0
	circle = 0
	for i in range (k):
		pass

def multiply(x, y):
	x = str(x)
	y = str(y)
	carryover = 0
	
	result = ""
	
	for i in range(len(x)):
		for j in range(len(y)):
			temp = str((int(x[i]) * int(y[j])) + carryover)
			result += temp[len(temp) - 1]
			carryover = int(temp[len(temp) - 2])
	return result 

def pow(x, y):
	result = 0
	for i in range(y):
		result = multiply(result, x)
	
	return result 


#print multiply(1000, 2000)

def chudnovsky(k):
	Sum = 0
	for i in range(k):
		if i % 2 == 0:
			Sum += mpf((math.factorial((6) * i) * ((545140134) * i + 13591409)/(math.factorial(3 * i) * (math.factorial(i)**(3)) * (mpf(262537412640768000)) ** (i + 1/mpf(2)))))
		else:
			Sum += mpf(-1 * (math.factorial((6) * i) * ((545140134) * i + 13591409)/(math.factorial(3 * i) * (math.factorial(i)**(3)) * (mpf(262537412640768000)) ** (i + 1/(2.0)))))
		clear()
		print "Iteration" + " " + str(i) + "/" + str(k)
		
	return 1/(12 * Sum)
	
#print definiteIntegral(-1, 1, 1000000) * 2
pi = chudnovsky(2000)
print pi
print " "
print confirm(pi)
	
