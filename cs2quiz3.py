#Section 1: Terminology +1
# 1) What is a recursive function?
#A function that calls itself
#
#
# 2) What happens if there is no base case defined in a recursive function? +1
#it will keep calling itself until it has reached a maximum about of times that it can call itself
#
#
# 3) What is the first thing to consider when designing a recursive function?
# The base case and recursion case
#
#
# 4) How do we put data into a function call? +1
# raw input
#
# 
# 5) How do we get data out of a function call? +1
# return
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.
#+3
#a1 = 8
#a2 = 8
#a3 = -1
#+3
#b1 = 2
#b2 = 0
#b3 = 0
#+1
#c1 = 1
#c2 = 4
#c3 = 55
#+2
#d1 = 6
#d2 = 8
#d3 = 5

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def input():
# +2
	question = raw_input("Next: ")
	if question != "":
		input()
#base case +2
	else:
		add = question + question
		print "the total was {}".format(add)
input()
