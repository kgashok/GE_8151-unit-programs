
# Guess A Number 
<img src="./img/GuessGame.png" style="width:400px;" class="center"/>


## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)

## Problem Statement

Shankar and Vijay are playing a game of integers. Shankar chooses an integer of his choice in his mind. It can be any integer value within the range of **`1 to 100`**.  Now, Vijay had to find that integer through some guesses.

Shankar can provides 3 hints to Vijay, each hint can be one of the below types:
* Type 1 : Guess is Low
* Type 2 : Guess is High
* Type 3 : You guessed my number!

Now Vijay has to make some guesses in order to find Shankar's integer.

**Note:**  Vijay is given only 10 chances to guess the number. If Vijay wins the game, then return `True` otherwise return `False`.


## Python Code
```python
"""Guess the Number Try to guess the secret number based on hints."""

import random

def ask_for_guess():
    '''returns an integer number as guessed by the user'''
    while True:
        guess = input('> ')  # Enter the guess.

        if guess.isdecimal():
            return int(guess)  # Convert string guess to an integer.
        print('Please enter a number between 1 and 100.')

print('*** Guess the Number ***')
print()
secretNumber = random.randint(1, 100)  # Select a random number.
print('I am thinking of a number between 1 and 100.')

for i in range(10):  # Give the player 10 guesses.
    print('You have {} guesses left. Take a guess.'.format(10 - i))

    guess = ask_for_guess()
    if guess == secretNumber:
        break  # Break out of the for loop if the guess is correct.

    # Offer a hint:
    if guess < secretNumber:
        print('Your guess is too low.')
    if guess > secretNumber:
        print('Your guess is too high.')

# Reveal the results:
if guess == secretNumber:
    print('Yay! You guessed my number!')
else:
    print('Game over. The number I was thinking of was', secretNumber)
```

## Sample Output
<img src="./img/OPGuessANumber.JPG" style="width:400px;"/>


## Replit Link
https://cutt.ly/GuessANumberGame

<img src="./img/GuessGameRepl.png" style="width:100px;"/>


## PythonTutor Link

https://cutt.ly/GuessANumberGameVisualization

<img src="./img/GuessGameVisual.png" style="width:100px;"/>

