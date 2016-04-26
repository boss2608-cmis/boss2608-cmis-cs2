#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) relational operators
#b) logical operators
#c) boolean values
#
#2 + 1) What does 'return' do?
# Return spits out the input in a function
#
#
#
#3 + 2) What are 2 ways indentation is important in python code?
#a) In a function, anything that is indented after the funtion definition is part of the funtion
#b) 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) 1.732 (sqrt of 3)
#problem1_c +1) 0
#problem1_d +1) -5
#
#problem2_a +1) True
#problem2_b +1) False
#problem2_c +1) Flase
#problem2_d) False
#
#problem3_a +1) 0.3
#problem3_b +1) 0.5
#problem3_c +1) 0.5
#problem3_d +1) 0.5
#
#problem4_a +1) 7
#problem4_b +1) 5
#problem4_c +1) 0.125
#problem4_d +1) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)
#Q23+1
def Comparison(A, B, C):
	print """Type in 3 different numbers (decimals are OK!)"""
#Q25+1
#Q26+1
def output():
     if int(A) > int(B) and int(A) > int(C):
        print "The largest numbe was " + int(A)
	elif int(B) > int(A) and int(B) > int(C):
        print "The largest numbe was " + int(B)
	elif int(C) > int(A) and int(C) > int(B):
		print "The largest numbe was " + int(C)
	else:
		print """you didn't follow directions"""

#Q30+1
#Q31+1
def main():
	print """Type in 3 different numbers (decimals are OK!)"""
    A = int(raw_input("A "))
    B = int(raw_input("B "))
	C = int(raw_input("C "))
    return output()

