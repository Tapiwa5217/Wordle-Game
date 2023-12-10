import random
import sys


def main():
    # Get a random word.
    answer = getRandomWord()

    attempts = 0
    max_attempts = select_difficulty()

    while attempts < max_attempts:
        guess = ''
        while len(guess) != 5:
            guess = input('Guess a 5 letter word: ').lower()

        printGuessColors(guess, answer)

        if guess == answer:
            print('You won!')
            break

        attempts += 1

    if guess != answer:
        print('You didn\'t win.')

    # select a difficulty
def select_difficulty():
    choice = 0

    while choice != 1 and choice != 2:
        print('select difficulty:')
        print('1. Easy')
        print('2. Hard')

        choice = int(input(''))

    if choice == 1:
        max_attempts = 6
    else:
        max_attempts = 5

    return max_attempts


# A helper method that prints the guess with the
# correct colors to the console.
def printGuessColors(guess, answer):
    for i in range(len(guess)):
        color = letterColor(i, guess, answer)
        end = "\033[0m"
        print(f'{color} {guess[i]} {end}')


# A helper method that determines the color
# of the letter in the guess.
def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return "\033[0;42m"  # green
    elif guess[index] not in answer:
        return "\033[0;41m"  # red
    else:
        return "\033[1;43m"  # yellow


# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()