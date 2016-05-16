#This text based game will be a maze type game where you have to find your way out of the forest without getting more lost or attacked by wild animals.

import random
 
def storypart4():
	if answer5 == "left":
		print "you meet a dead end and have to turn back"
		answer6 = raw_input("do you turn left or straight: ")
		if answer6 == "straight":
			print "you made it out alive, yay!"
		elif answer6 == "left":
			print """... as you walk further into the forest, the road starts to dissapear... you are lost again

...The end..."""
	elif answer5 == "right":
		print "you made it out alive, yay!"
	elif answer5 == "straight":
		print """... as you walk further into the forest, the road starts to dissapear... you are lost again

...The end..."""

def storypart3():
	answer4 = raw_input("do you look or step away: ")
	hours = int(random.randint(3, 12))
	if answer4 == "look":
		print "you are sprised as it jumps at you, however it was only a squirrel and now it has run off. You think whether or not to turn around and go back but you remember that the bear is still out there so you walk off in the opposite direction... you walk for what feels like {} hours... you hear cars so you start to run, you see a yellow car go by. You made it out alive! You borrow a mans phone to call the police and make it home...".format(hours)
	elif answer4 == "step away":
		print "you step on a twig as you walk back and th bush stops shaking... you start to step away faster and turn around. You run away and run faster as you hear water. You found a river! but there is one slight problem... there are more bears there caching salmon. you take a sip of the water and walk down the river, away from the bears... you walk for about an hour and meet an intersection, which way do you turn?"
	return storypart4()

def storypart2():
	answer3 = raw_input("do you run, fight, or hide: ")
	if answer3 == "fight":
		print "you put up a good figh but get knocked over the head, hit a rock, and die..."
	elif answer3 == "hide":
		print "the bear sniffs you out, you try to run but it is too late, it catches you and with one swipe of its paw... it kiils you..."
	else:
		print "you manage to run long enough to lose the bear, but you are further away from civilzation than you were before"
		print "you look around but everything looks the same, you hear a sound so you turn around to see a bush shaking, what do you do..."
	return storypart3()

def main():
	print "you have been stuck in a forest for a certan amount of days"
	answer1 = int(raw_input("How many days have you been in the forest: "))
	answer2 = raw_input("do you have any survival skills? ") 
	print "you have a {} percent chance of living... but you need to make the right choices...".format(random.random())
	if answer1 > int(365) and answer2 == "yes":
		print "you survive long enough to make it out alive, but this experience will haunt you forever..."
	elif answer1 > int(365) and answer1 > int(0) and answer2 != "yes":
		print "you must've been lucky, but your luck is over. You accidentally eat a poisonous berry and die."
	elif answer1 <= int(0) and answer2 == "yes" or answer2 == "no":
		print "good job, you're not lost, now go home before you are"
	elif answer1 < int(365) and answer1 > int(0) and answer2 != "yes":
		print "you dont last long in the forest and die of starvation"
	elif answer1 <= int(365) and answer1 > int(0) and answer2 == "yes":
		print "you are most likey to find your way out soon, but you are far from civilization, you are suddenly chased by a bear"
	return storypart2()

main()

