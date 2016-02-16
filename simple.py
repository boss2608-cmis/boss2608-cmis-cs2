def add(x, y):
	z = x + y
	return z

def output(name, x, y, z):
	return """
Hello there, {}!
Did you know:
{} + {} = {} 
""".format(name, x, y, z)

def main():
	name = raw_input("Name: ")
	x = raw_input("1st number: ")
	y = raw_input("2nd number: ")
	z = add(int(x), int(y))
	print output(name, x, y, z)

main()
