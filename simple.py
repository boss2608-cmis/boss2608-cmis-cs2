import math
def area(a, b, c):
	A1 = ((4*math.pi)*a**2)
	A2 = ((4*math.pi)*b**2)
	A3 = ((4*math.pi)*c**2)
	Avg = (A1+A2+A3)/3
	return Avg

def output(a, b ,c , d, e):
	return """
Hello there, {}!
equation: ((4*math.pi)*{}**2)((4*math.pi)*{}**2)((4*math.pi)*{}**2)
Calculating average area of three spheres...

the answer is: {} 
""".format(a, b, c, d, e)

def main():
	a = raw_input("Name: ")
	b = raw_input("1st number: ")
	c = raw_input("2nd number: ")
	d = raw_input("3rd number: ")
	e = area(int(b), int(c), int(d))
	print output(a, b, c, d, e)
main()


