# To do

# Get user input

import random

def num_check(question, low=None, high=None):
    # sets up error messages
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


def rps_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


keep_going = ""
while keep_going == "":
    play = ["rock", "paper", "scissors"]
    choice = random.choice(play)
    user_play = input("Choose either rock(r), paper(p) or scissors(s): ").lower()

    if user_play == "paper":
        if choice == "scissors":
            lose = rps_statement("<< User: {}   |   Computer: {}   |   Result: You lost >>".format(user_play, choice), "<")
        elif choice == "rock":
            win = rps_statement("** User: {}   |   Computer: {}   |   Result: You won **".format(user_play, choice),
                                "*")
        else:
            draw = rps_statement("!! User: {}   |   Computer: {}   |   Result: It's a tie !!".format(user_play, choice),
                                 "!")
    elif user_play == "rock":
        if choice == "scissors":
            win = rps_statement("** User: {}   |   Computer: {}   |   Result: You won **".format(user_play, choice),
                                "*")
        elif choice == "rock":
            draw = rps_statement("!! User: {}   |   Computer: {}   |   Result: It's a tie !!".format(user_play, choice),
                                 "!")
        else:
            lose = rps_statement("<< User: {}   |   Computer: {}   |   Result: You lost >>".format(user_play, choice),
                                 "<")
    else:
        if choice == "scissors":
            draw = rps_statement("!! User: {}   |   Computer: {}   |   Result: It's a tie !!".format(user_play, choice),
                                 "!")
        elif choice == "rock":
            lose = rps_statement("<< User: {}   |   Computer: {}   |   Result: You lost >>".format(user_play, choice),
                                 "<")
        else:
            win = rps_statement("** User: {}   |   Computer: {}   |   Result: You won **".format(user_play, choice),
                                "*")
