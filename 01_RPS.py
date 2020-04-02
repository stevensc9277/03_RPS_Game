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
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


computer = ["rock", "paper", "scissors"]
rounds = num_check("How many rounds do you want to play? ")
rounds_played = 0
win = 0
lose = 0
draw = 0
start = 1
choice = random.choice(computer)
while rounds_played < rounds:
    user = ""
    start_round = rps_statement("### Round {} of {} ###".format(start, rounds), "#")
    start += 1

    while user != choice:

        user = input("Please choose rock (r), paper (p) or scissors (s): ")

        if rounds >= 1:

            if user == "paper" and choice == "scissors":
                lost = rps_statement("<< User: {}   |   Computer: {}   |   Result: You lost  <<".format(user, choice),
                                     "<")
                lose += 1

            elif user == "paper" and choice == "rock":
                won = rps_statement("^^ User: {}   |   Computer:{}   |   Result: You won  ^^".format(user, choice), "^")
                win += 1

        if user == choice:
            drawn = rps_statement("!! User: {}   |   Computer: {}   |   Result: It's a tie !!".format(user, choice),
                                  "!")
            draw += 1
    print("Won: {} \t | \t Lost: {} \t | \t Draws: {}".format(win, lose, draw))
    rounds_played += 1
    print()
    if rounds_played >= 1:
        choice = random.choice(computer)  # reset computer choice after a round

    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()

print("Thank you for playing the Higher / Lower game. ( ﾟдﾟ)つ Bye~~~")
