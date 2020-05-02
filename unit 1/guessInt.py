# Guess a number

from random import randint


def guess():
    myguess = int(input("Enter a number:"))
    if number > myguess:
        print('You guessed less')
    elif number < myguess:
        print('You guess high')
    else:
        print('Great! You guessed right!')


print("Guess a number")
attempt = 10
number = randint(1, 100)
while attempt > 0:
    guess()
    attempt -= 1
print('Good try! Play again!')
