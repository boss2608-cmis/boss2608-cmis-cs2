
import random
def check(number,randomNo,rounds):
    if int(number) == randomNo and rounds == 2 or 3:
        randomNo = random.randint(0,100)
        attempts(rounds-1,randomN,tries=5)
    elif rounds <= 0:
        print " Thanks for playing "
    else:
        print " Thanks for playing "

def oneguess(rounds,randomNo,tries):
    number = raw_input(" Guess a number: ")
    if int(number) == randomNo:
        print "Thats Correct You, must be a psychic"
        print "{} rounds remaining".format(rounds)        
        check(number,randomNo,rounds)
    elif int(number) < randomN:
        print " That's too low "
        attempts(rounds,randomNo,tries-1)
    elif int(number) > randomNo:
        print " That's too high "
        attempts(rounds,randomNo,tries-1)
    else:
        print " End"

def attempt(rounds,randomNo,tries):
    if rounds == 0 and tries == 0:
        print "Thanks for playing!"
        exit()
    if tries == 0:
        print "{} rounds remaining".format(rounds)
        tries = 5
        randomNo = random.randint(0,100)
        guess(rounds-1,randomNo,tries)
    else:
        guess(rounds,randomNo,tries)

def main():
    print "Guess a number from 0 to 100 including 0 and 100"
    print "{} rounds remaining".format(3)
    randomNo = random.randint(0,100)
    rounds = 2
    tries = 5
    attempts(rounds,randomNo,tries)
main()
