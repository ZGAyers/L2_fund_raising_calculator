# Component 01 - Get user input on the amount they want to raise for charity (goal)

# Functions go here

# No blank function
# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        # Removed by GK: has_errors = ""

        # Removed by GK: if __name__ == '__main__':
        # If response is blank, question is repeated (loop starts over)
        if response == "":
            print(error)
            continue

        # if response is not blank, program continues
        else:
            return response


# Number Checking Function goes here
def num_check(question):

    error = "Please enter a number that is more than zero"
    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:

                print(error)
            else:
                return response
        except ValueError:

            print(error)


# get goal function
def get_goal():
    valid = False
    while not valid:
        profit_var = not_blank("Would you like to enter your profit goal by percentage or cost? ",
                               "Please fill in this field").lower()

        if profit_var == "$":
            goal = num_check("What is your goal amount to raise for charity? $")
            print("$", goal)
            break

        elif profit_var == "%":
            goal = num_check("What percentage do you want to raise for charity? ")
            print(goal, "%")
            break

        else:
            print("Please enter '%' or '$'")

        return profit_var

what_goal = get_goal()
