import random
def numberRange(minino, maxino):
	return random.randint(minino, maxino)

def result_from_guess(integer = 0):
	Playersguess = raw_input("your Guess: ")
	if result == Playersguess:
		print "that's correct, you're pretty good!"
	elif integer == 5:
		print "you're not so good are you?"
	elif result > Playersguess:
		print "that's too low"
		integer += 1
		result_from_guess(integer)
	elif result < Playersguess:
		print "That's too high"
		integer += 1
		result_from_guess(integer)
result_from_guess(integer)






