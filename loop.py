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
	sum = 0
	if n > 0:
		print "its positive"
		while n > 0:
			if n % 2 == 1:
				sum += n
			n -= 1
	elif n < 0:
		print "its negative"
		while n < 0:
			if n % 2 == 1:
				sum += n
			n += 1
	print sum
#addodds(20)

def grid(w, h):
	a = "."*w
	while h != 0:
		print a
		h = 1
#grid(10, 10)

def grid2(w, h):
	out = ""
	x = 0
	while x < w:
		out += "."
		x += 1
	while x < h:
		out += "."
		x += 1
	print x
grid2(10, 10)
	 

