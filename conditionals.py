#This text based game will be a surival game where you have to survive through the night.

import random
def story():
	print "you have been stuck in a forest for a certan amount of days"
	answer1 = int(raw_input("How many days have you been in the forest: "))
	answer2 = raw_input("do you have any survival skills? ") 
	print "ok, you have been stuck in the forest for {} days...".format(answer1)
	if answer1 > int(365) and answer2 == "yes":
		print "you survive long enough to make it out alive, but this experience will haunt you forever..."
	elif answer1 > int(365) and answer2 != "yes":
		print "you must've been lucky, but your luck is over. You accidentally eat a poisonous berry and die."
	elif answer1 == int(0) and answer2 == "yes" or answer2 == "no":
		print "good job, you're not lost, now go home before you are"
	elif answer1 < int(365) and answer2 != "yes":
		print "you dont last long in the forest and die of starvation"
	elif answer1 < int(365) and answer2 == "yes":
		print "you are most likey to find your way out soon, but you are far from civilization, you are suddenly chased by a bear"
		answer3 = raw_input("do you run, fight, or hide: ")
		if answer3 == "fight":
			print "you pu up a good figh but get knocked over the head, hit a rock, and die..."
		elif answer3 == "hide":
			print "the bear sniffs you out, you try to run but it is too late, it catches you and with one swipe of its paw... it kiils you..."
		elif answer3 == "run":
			print "you manage to run long enough to lose the bear, but you are further away from civilzation than you were before"
			print "you look around but everything looks the same, you hear a sound so you turn around to see a bush shaking, what do you do..."
			answer4 = raw_input("do you look or step away: ")
			hours = int(random.randint(3, 12))
			if answer4 == "look":
				print "you are sprised as it jumps at you, however it was only a squirrel and now it has run off. You think whether or not to turn around and go back but you remember that the bear is still out there so you walk off in the opposite direction... you walk for what feels like {} hours... you hear cars so you start to run, you see a yellow car go by. You made it out alive! You borrow a mans phone to call the police and make it home...".format(hours)
			elif answer4 == "step away":
				print "you step on a twig as you walk back and th bush stops shaking... you start to step away faster and turn around. You run away and run faster as you hear water. You found a river! but there is one slight problem... there are more bears there caching salmon. you take a sip of the water and walk down the river, away from the bears..."

story()

