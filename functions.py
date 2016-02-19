import math

def add(a, b):
	return a+b
x = add(3, 4)
y = add(5, 7)
print x
# this adds a and b

def sub(a, b):
	return a-b
y = sub(5, 3)
y = sub(21, 9)
print y
# this subtracts a and b

def mul(a, b):
	return a*b
w = mul(4, 4)
w = mul(2, 9)
print w
# this multiplies a and b

def div(a, b):
	return a/b
	return float
z = div(2.0, 3)
z = div(9, 3)
print z
# this divides a and b

def hours(a, b, c):
	return a/b/c
H = hours(86400, 60, 60)
H = hours(3600, 60, 60)
print H
# this turns a into hours
def Areacircle(r):
	pi = (math.pi)
	return pi * r**2
s = Areacircle(5)
s = Areacircle(9)
print s
#A function that tells the area of a circle

def Volumesphere(r):
	pi = (math.pi)
	return (((4/3.0)*pi)*r**3)
Volumesphere=(5)

#A function that tells the volume of a sphere

def averagevolume(a,b):
	pi = (math.pi)
	Vol1 = (((4/3.0)*pi)*a**3)
	Vol2 = (((4/3.0)*pi)*b**3)
	return Vol1 + Vol2/2
averagevolume(5,10)
#A function that tells the average voulume of two spheres

def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))
areaoftriangle(1,2,2.5)
#A function that tells the area of a triangle

def right_align(a):
	return (a.rjust(80))
right_align("Hello")
#A function that aligns hello to the right side of python

def center(a):
	return (a.center(40))
center("Hello")
#A function that aligns hello to center of python

def msgbox(a):
	x =    """		  +---------+
		  |  """+"Hello"+"""  |
		  +---------+"""
	print x
	return"""		  +---------------+
		  |  """+a+"""  |
		  +---------------+"""
print msgbox("Life is Fun")

