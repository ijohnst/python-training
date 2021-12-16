# Guessing game to guess a color
import random
print("Hello! I'm thinking of a color \n")
colors = ['red', 'blue', 'yellow', 'green', 'blue',
          'orange', 'purple', 'brown', 'white', 'black']
correctColor = random.choice(colors)
print('\n' + 'DEBUG: ' + correctColor)
print('These are your choices:')
print(*colors, sep="\n")

print('\n' + "Which of the above colors am I thinking of? I'll give you 5 guesses")

# 5 guesses
for numGuesses in range(1, 6):
    guess = input()
    if guess not in colors:
        print("Please guess from the colors above")
        continue

    if guess != correctColor and numGuesses == 4:
        print(guess + " isn't the color I am thinking of. This is your last guess")
    elif guess != correctColor and numGuesses == 5:
        print(guess + " isn't the color I am thinking of.")
    elif guess != correctColor:
        print(guess + " isn't the color I am thinking of. You have " +
              str(5 - numGuesses) + ' guesses left')
    else:
        break

if guess == correctColor:
    print('Congrats! I am thinking of ' + correctColor)
else:
    print('Unfortunately that was your last guess. I was thinking of ' + correctColor)
