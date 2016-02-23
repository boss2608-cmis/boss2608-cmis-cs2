import math
def area(r1, r2, r3):
	A1 = ((4*math.pi)r1**2)
	A2 = ((4*math.pi)r2**2)
	A3 = ((4*math.pi)r3**2)
	Avg = (A1+A2+A3)/3

def output(name):
	return """
Hello there, {}!
The average area of these three spheres is:
{} 
""".format(name)

def main():
	name = raw_input("Name: ")
	x = raw_input("1st number: ")
	y = raw_input("2nd number: ")
	z = add(int(x), int(y))
	print output(name, x, y, z)
main()
