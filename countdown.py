def countdown(n):
	if n > 10:
		print "done"
	else:
		print n
		countdown(n + 1)

def main():
	countdown(0)
	return
main()
