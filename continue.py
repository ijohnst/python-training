# Uses the continue statement in a loop
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue  # skips the print function below in this iteration and goes to the top
    print('spam is ' + str(spam))
