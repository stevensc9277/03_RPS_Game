# To do

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


choice = "scissors"
rounds = num_check("How many rounds do you want to play? ")
rounds_played = 0
start = 1

while rounds_played < rounds:
    user = ""
    start_round = rps_statement("### Round {} of {} ###".format(start, rounds), "#")
    start += 1

    while user != choice:

        user = input("Please choose rock (r), paper (p) or scissors (s): ").lower()
        while user != choice:
            if user == "paper":
                paper = rps_statement("<< User: {}   |   Computer:{}   |   "
                                      "Result: You lost <<".format(user, choice), "<")
                rounds += 1
                break

            elif user == "rock":
                rock = rps_statement("** User:{}   |   Computer:{}   |   "
                                     "Result: You won! **".format(user, choice), "*")
                rounds += 1
                break

        else:
            if user == choice:
                scissors = rps_statement("!! User:{}   |   Computer:{}   |   "
                                         "Result: It's a tie !!".format(user, choice), "!")
                rounds += 1
                break


