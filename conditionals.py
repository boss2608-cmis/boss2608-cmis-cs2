#This text based game will be a surival game where you have to survive through the night.

import random
def story():
	print "you have been stuck in a forest for a certan amount of days"
	answer1 = raw_input("How many days have you been in the forest: ")
	answer2 = raw_input("do you have any survival skills? ") 
	if answer1 > 365 and answer2 == yes:
		print "you survive long enough to make it out alive, but this experience will haunt you forever..."
	elif answer1 > 365 and answer2 != yes:
		print "you must've been lucky, but your luck is over. You accidentally eat a poisonous berry and die."
	elif answer1 < m65 and answer2 != yes:
		print "you dont last long in the forest and die of starvation"
	elif answer1 < 365 and answer2 == yes:
		print "you are most likey to find your way out soon, but you are far from civilization, you are suddenly chased by a bear"
		answer3 = raw_input("do you run or fight: ")
		if answer3 == "fight":
			print "you get knocked over the head, hit a rock, and die... you fool..."
		elif answer3 == "run":
			print "you manage to run long enough to lose the bear, but you are further away from civilzation than you were before"
story()


	
