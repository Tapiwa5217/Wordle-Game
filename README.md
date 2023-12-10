# Wordle
## Background and Rules

In the game Wordle, the user is trying to guess a secret 5 letter word. The user will type in a 5 letter guess, and the computer will share information about how close the guess is to the actual answer. 

    If a letter in the guess exactly matches a letter in the answer (same letter and correct position), the letter will be marked green.

    If a letter in the guess almost matches a letter in the answer (same letter, but incorrect position), the letter will be marked yellow.

    If a letter in the guess doesn’t match a letter in the answer (guessed letter doesn’t exist in answer), the letter will be marked red. I know the actual game marks the letter gray, but we will mark it red to be super clear.

The user will use this information to then make another guess, and will keep guessing until they guess the answer (they win), or they run out of their 6 guesses (they lose).

For example, if the secret answer is towel and the user guesses lower, the computer should print out:
l - Yellow
o - Green
w - Green
e - Green
r - Red

    The o, w, and e are all green because the user guessed those letters in the correct position.

    The l is yellow because l is the last letter in the answer, but the user guessed it in the first position.

    The r is red because it does not appear in the answer.