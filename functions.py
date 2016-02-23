import math

def add(a, b):
	return a+b
x = add(3, 4)
e = add(5, 7)
print x
print e
# this adds a and b

def sub(a, b):
	return a-b
y = sub(5, 3)
f = sub(21, 9)
print y
print f
# this subtracts a and b

def mul(a, b):
	return a*b
w = mul(4, 4)
c = mul(2, 9)
print w
print c
# this multiplies a and b

def div(a, b):
	return a/b
	return float
z = div(2.0, 3)
i = div(9, 3)
print z
print i
# this divides a and b

def hours(a, b, c):
	return a/b/c
H = hours(86400, 60, 60)
q = hours(3600, 60, 60)
print H
print q
# this turns a into hours
def Areacircle(r):
	pi = (math.pi)
	return pi * r**2
s = Areacircle(5)
d = Areacircle(9)
print s
print d
#A function that tells the area of a circle

def Volumesphere(r):
	pi = (math.pi)
	return (((4/3.0)*pi)*r**3)
a = Volumesphere(5)
b = Volumesphere(9)
print a
print b
#A function that tells the volume of a sphere

def averagevolume(a,b):
	pi = (math.pi)
	d1 = a/2
	d2 = b/2
	Vol1 = (((4/3.0)*pi)*d1**3)
	Vol2 = (((4/3.0)*pi)*d2**3)
	return (Vol1 + Vol2)/2
j = averagevolume(10, 20)
k = averagevolume(18, 80)
print j
print k
#A function that tells the average voulume of two spheres

def areaoftriangle(a,b,c):
	p = a+b+c/2.0
	return math.sqrt(p*(p-a)*(p-b)*(p-c))

print areaoftriangle(1,2,2.5)

#A function that tells the area of a triangle

def right_align(a):
	return (a.rjust(80))
g = right_align("Hello")
p = right_align("Bye")
print g
print p
#A function that aligns hello to the right side of python

def center(a):
	return (a.center(40))
w = center("Hello")
x = center("Bye")
print w
print x
#A function that aligns hello to center of python

def msg_box(a):
    return "+" + (len(a) + 4) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + 4) * "-" + "+"
a = msg_box("Hello")
b = msg_box("I eat cats!")
print a
print b
#A funtion that puts a message into a box

print msgbox(str(x))
print msgbox(str(a))
print msgbox(str(a))
