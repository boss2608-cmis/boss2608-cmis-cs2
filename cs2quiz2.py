#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) relational operators
#b) logical operators
#c) boolean values
#
#2) What does 'return' do?
# Return spits out the input in a function
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) In a function, anything that is indented after the funtion definition is part of the funtion
#b) 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) 1.732 (sqrt of 3)
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) Flase
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def Comparison(A, B, C):
	print """Type in 3 different numbers (decimals are OK!)"""

def output():
     if int(A) > int(B) and int(A) > int(C):
        print "The largest numbe was " + int(A)
	elif int(B) > int(A) and int(B) > int(C):
        print "The largest numbe was " + int(B)
	elif int(C) > int(A) and int(C) > int(B):
		print "The largest numbe was " + int(C)
	else:
		print """you didn't follow directions"""


def main():
	print """Type in 3 different numbers (decimals are OK!)"""
    A = int(raw_input("A "))
    B = int(raw_input("B "))
	C = int(raw_input("C "))
    return output()

