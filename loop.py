def countdown(x):
	while x >= 0:
		print x
		x -= 1
#countdown(7)

def countup(x):
	while x <= 10:
		print x
		x += 1
#countup(0)

def count(x):
	while x < 0:
		print x
		x += 1
	while x > 0:
		print x
		x -= 1
#count(-5)

def countfrom2(x, y):
	while x < y:
		print x
		x += 1
	while x > y:
		print x
		x -= 1
	while x == y:
		print y
		x -= 1
#countfrom2(5, 0)

def addodds(n):
	n = float(n)
	if n % 2 == 0:
		while n < 0:
			return sum
	elif n % 2 == 0:
		while n > 0:
			return sum
addodds(21)
