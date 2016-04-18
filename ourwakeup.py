def main():
	print """This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""
	
	n0 = raw_input("n0: ")
	n1 = raw_input("n1: ")
	n2 = raw_input("n2: ")
	n3 = raw_input("n3: ")
	n4 = raw_input("n4: ")

output()
def calculation(n0, n1, n3, n4):
	if raw_input(n0) > 10:
		print float(raw_input(n0)) + "is out of range"
	elif raw_input(n0) < 0:
		print float(raw_input(n0)) + "is out of range"
	if raw_input(n1) > 10:
		print float(raw_input(n1)) + "is out of range"
	elif raw_input(n1) < 0:
		print float(raw_input(n1)) + "is out of range"
	if raw_input(n2) > 10:
		print float(raw_input(n2)) + "is out of range"
	elif raw_input(n2) < 0:
		print float(raw_input(n2)) + "is out of range"
	if raw_input(n3) > 10:
		print float(raw_input(n3)) + "is out of range"
	elif raw_input(n3) < 0:
		print float(raw_input(n3)) + "is out of range"
	if raw_input(n4) > 10:
		print float(raw_input(n4)) + "is out of range"
	elif raw_input(n4) < 0:
		print float(raw_input(n4)) + "is out of range"
	average = (float(n0)+float(n1)+float(n2)+float(n3)+float(n4))/5

def output():
	"The average is" + average
	"The integer part of the average is" + int(average)
	"The integer part is {}.".format(even, odd)
	if average == 2 or 4 or 6 or 8
		.format() = even
	
