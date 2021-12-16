# Example of error messages
def divby42(dividedby):
    try:
        return 42 / dividedby
    except ZeroDivisionError:
        print("Error: You tried to divide by zero and that just won't work")


print(divby42(2))
print(divby42(22))
print(divby42(0))
print(divby42(1))
