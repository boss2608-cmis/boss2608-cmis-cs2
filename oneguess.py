import random
def numberRange(number1,number2):
    return random.randint(number1,number2)

def PlayerResult(result,PlayersGuess):
    if result > PlayersGuess:
        sub = abs(PlayersGuess - result)
        return "That is over by {}".format(sub)
    else:
        add = abs(PlayersGuess + result)
        return "That is under by {}".format(add)

def output(result, PlayersGuess, wrong):
    if result == PlayersGuess:
        print """The target was {}
Your guess was {}
That's correct! You must be a psychic!""".format(result, PlayersGuess)
    else:
        print """The target was {}
Your guess was {}
{}""".format(result, PlayersGuess, wrong)


def main():
    number1 = int(raw_input("What is the minimum number?"))
    number2 = int(raw_input("What is the maximum number?"))
    print "Im thinking of a number from {} to {}".format(number1, number2)
    PlayersGuess = int(raw_input("What do you think it is?:"))
    result = int(numberRange(number1, number2))
    wrong = PlayerResult(result, PlayersGuess)
    return output(result, PlayersGuess, wrong)

main()

