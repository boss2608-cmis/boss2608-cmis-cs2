#My conditionals program will test the player on whether or not he knows some of Shakespeare's most famous quotes.

import random

def game():
	print """We will test how well you know some of Shakespeaer's most famous quotes 

Level 1:"""
	print "To be, or not to be: that is the _____"
	answer = raw_input("What is the missing word: ")
	print "To be, or not to be: that is the {}".format(answer)
	if answer == Question:
		print "Correct, Well Done!"
	else answer != Question:
		print "Wrong!"
game()
	
