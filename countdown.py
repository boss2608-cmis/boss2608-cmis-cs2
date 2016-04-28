#def countdown(start, stop):
#	if start < stop:
#		print start
#		print"done"
#	else:
#		print start
#		countdown(start-1, stop)

#def main():
#	start = int(raw_input("start: "))
#	stop = int(raw_input("stop: "))
#	countdown(start, stop)
#main()

def adder(running_total = 0):
	print "The running total is {}".format(running_total)
	n0 = raw_input("next number: ")
	if n0 == "":
		print "The sum is {}".format(running_total)
	else:
		running_total += float(n0)

		adder(running_total)
adder()

def Bigger():
	n0 = raw_input("Next: ")
	
		Bigger()
Bigger()




