from math import *
import math

def Num2IEEE(value):
	if value > 0:
		exp = int(math.log(value, 2))
		real = math.pow(2, (math.log(value, 2) - exp))
	else:
		exp = int(math.log(-value, 2))
		real = math.pow(2, (math.log(-value, 2) - exp))
	mantis = real - 1

	return  exp, mantis

def serie(value):
	result = 0
	for i in range(50):
		result = result + (
		    (((-1)**i) * factorial(2 * i)) /
		    ((1 - 2 * i) * (factorial(i)**2) * (4**i))
		) * value**i
	return result

def ieeQuad(value):
	exp, mantis = Num2IEEE(value)
	return 2**((exp - 1) / 2) * serie(mantis) * math.sqrt(2)

if __name__ == '__main__':
	print(ieeQuad(float(input())))