# To do
import random
# Get user input


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
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()


keep_going = ""
while keep_going == "":

    computer = ["rock", "paper", "scissors"]
    chosen = random.choice(computer)
    rounds = num_check("How many rounds do you want to play? ")
    rock = 1
    paper = 2
    scissors = 3
    start = 1
    num_won = 0
    rounds_played = 0
    lost = "You lose"
    won = "You won"
    while rounds_played < rounds:
        choice = ""
        start_round = rps_statement("### Round {} of {} ###".format(start, rounds), "#")
        start += 1

    # Compare with computer
        while choice != chosen:
            choice = input("Please choose either rock (r), paper (p), or scissors (s): ").lower

            if choice == rock:
                if chosen == paper:
                    lose = rps_statement(" User: rock   |   Computer: {}   |   Result: {}".format(chosen, lost),
                                         "-")
                elif chosen == scissors:
                    win = rps_statement(" User: rock   |   Computer: {}   |   Result:{}".format(choice, chosen, won), "*")
                else:
                    draw = rps_statement("User: rock   |   Computer: {}   |   Result: It's a draw".format(chosen),
                                         "'")

            elif choice == paper:
                if chosen == scissors:
                    lose = rps_statement(" User: paper   |   Computer: {}   |   Result: {}".format(choice, chosen, lost),
                                         "-")
                elif chosen == rock:
                    win = rps_statement(" User: paper   |   Computer: {}   |   Result:{}".format(choice, chosen, won), "*")
                else:
                    draw = rps_statement("User: paper   |   Computer: {}   |   Result: It's a draw".format(choice, chosen),
                                         "'")
            else:
                if chosen == rock:
                    lose = rps_statement(" User: scissors   |   Computer: {}   |   Result: {}".format(chosen, lost),
                                         "-")
                elif chosen == paper:
                    win = rps_statement(" User: scissors   |   Computer: {}   |   Result:{}".format(chosen, won), "*")
                else:
                    draw = rps_statement("User: scissors   |   Computer: {}   |   Result: It's a draw".format(chosen),
                                         "'")

    keep_going = input("Press <enter> to play again or any key to quit. ")
    # Print results
print("Thank you for playing.")
