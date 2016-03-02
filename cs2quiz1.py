#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The symbol "=", or assignment operator, assigns things to whatever it is assigned to.

#2 3pts) Write a technical definition for 'function'
#A function is a code that spits something out after recieving information, like a vending machine.

#3 1pt) What does the keyword "return" do?
#return returns the value or expression from the function.

#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: String
#		"This is a test"
#	2: Float
#		2.9, 3.7
#	3: Integer
#		50, 21
#	4: Bool
#		True, False
#	5: tuple
#		x = ("I", "Am", "Awesome")
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition defines the function, telling it wat to do, and calling a finction is like using the function

#6 3pts) What are the 3 phases that every computer program has? What happens in each of them
#	1: Recieve information
#	2: Process information
#	3: Returns information
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math
def area(a, b, c):
	pi = math.pi
	D1 = (((sqrt*a)/pi)*2)
	D2 = (((sqrt*b)/pi)*2)
	D3 = (((sqrt*c)/pi)*2)
	Total = D1 + D2 + D3
	return D1
	return D2
	return D3
	return Total

def output(a, b ,c , d):
	return """
Circlepython  Diameter
c1: {}
c2: {}
c3: {}
Totals: {}
""".format(a, b, c, d)

def main():
	a = raw_input("Area of C1: ")
	b = raw_input("Area of C2: ")
	c = raw_input("Area of C3: ")
	d = area(int(a), int(b), int(c))
	print output(a, b, c, d)
main()
