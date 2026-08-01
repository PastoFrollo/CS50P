import random
import sys

def main():
    max = level()
    number = random.randint(1, max)
    guess(number)


def level():
    while True:
        try: 
            max = int(input("Level: "))
        except ValueError:
            pass
        else:
            if max > 0:
                return max


def guess(number):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            result(guess, number)


def result(guess, number):
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")
    else:
        print("Just right!")
        sys.exit()


main()