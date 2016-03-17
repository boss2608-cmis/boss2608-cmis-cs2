import random
def numberRange(minino, maxino):
    return random.randint(minino, maxino)

def output(result, PlayersGuess, wrong):
    if result == PlayersGuess:
        print """The target was {}
Your guess was {}
That's correct! You must be a psychic!""".format(result, PlayersGuess)
    else:
        print """The target was {}
Your guess was {}
{}""".format(result, PlayersGuess, wrong)

def PlayerResult(result, PlayersGuess):
    if result > PlayersGuess:
        sub = abs(PlayersGuess - result)
        return "That is under by {}".format(sub)
    else:
        add = abs(PlayersGuess - result)
        return "That is over by {}".format(add)

def main():
    minino = int(raw_input("What is the minimum number? "))
    maxino = int(raw_input("What is the maximum number? "))
    print "Im thinking of a number from {} to {}".format(minino, maxino)
    PlayersGuess = int(raw_input("What do you think it is?: "))
    result = int(numberRange(minino, maxino))
    wrong = PlayerResult(result, PlayersGuess)
    return output(result, PlayersGuess, wrong)

main()

