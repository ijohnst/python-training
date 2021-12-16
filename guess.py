# Number guesing game

"""
1. Say hello
2. Ask their name
3. Set value of answer
4. Welcome them and tell the user to pick a number between 1 and 20
5. Have user guess the number in 6 tries
6. Track guesses taken
7 & 8. If the number is too high or too low give a message
8. If Correct guess send a message
"""


def guessgame():
    import random

    secretNumber = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20')

    for numGuesses in range(1, 7):
        print('Take a guess!')
        try:
            guess = int(input())
        except ValueError:
            print('Please enter a number')
            continue

        if guess < 0 or guess > 20:
            print('Please enter a number between 1 and 20')
        elif guess > secretNumber:
            print('That is too high, try a lower number')
        elif guess < secretNumber:
            print('That is too low, try something higher')
        else:
            break

    if guess == secretNumber:
        print("Fantastic! You guessed it right in " + str(numGuesses) + ' tries')
    else:
        print('Sorry! I was thinking of ' +
              str(secretNumber) + '. Better luck next time!')


# Ask the players name
print('Hello, What is your name?')
name = input()

# Run the guess game
print('\n'+'Welcome ' + name + '! Lets begin the guess game!')
guessgame()
