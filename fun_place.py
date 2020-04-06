# This program was created solely for entertainment and testing purposes
# Please do not pay attention to anything here

import random
import math


def num_check(question, low=None, high=None):
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))
            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


keep_going = ""
while keep_going == "":
    user_choice = num_check("Enter a number between 1 and  10: ", 1, 10)

    # To do
    # Add, subtract, divide, multiply, raise to the power of 'numbers'

    computer = random.randint(1, 10)
    addition = user_choice + computer
    subtraction = user_choice - computer
    division = user_choice / computer
    multiplication = user_choice * computer
    exponent = math.pow(user_choice, computer)

    # Print results
    print("{} + {} = {}".format(user_choice, computer, addition))
    print("{} - {} = {}".format(user_choice, computer, subtraction))
    print("{} / {} = {:.2f}".format(user_choice, computer, division))
    print("{} * {} = {}".format(user_choice, computer, multiplication))
    print("{} raised to the power of {} = {:.0f}".format(user_choice, computer, exponent))
    print()
    keep_going = input("Press <enter> to start again or any key to quit. ")
    print()

print("The end...(* ￣︿￣)")
