# Component 05 - Find the selling price from information given by user

# Functions go here


# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)

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

# main routine

# set up empty list
printout = []
total_list = []

# find the charity goal for the user
what_goal = get_goal()

how_many = not_blank("How many items are you selling: ",
                     "Please enter how many items are going to be sold in total")

# start of loop for item input
stop = ""
while stop != "xxx":
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'xxx' to quit")

    if get_product == "xxx":
        break

    get_cost = num_check("Cost: $")

    get_amount = num_check("Amount: ")

    printout.append("{:.0f} {}, ${:.2f} ".format(get_amount, get_product, get_cost))

    # calculate the cost of a product from the amount they are buying
    if get_cost > 0:
        total = get_cost * get_amount
    else:
        continue

    # append the calculate total cost of the individual products
    total_list.append(total)

# calculate the total cost of all items
total_cost = sum(total_list)


# print out lines
print()
print("Amount , Item, Cost")
for item in printout:
    print(item)
print()
print("Total Cost: ")
print("${:.2f}".format(total_cost))
