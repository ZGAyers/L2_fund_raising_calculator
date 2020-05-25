# Final program of Fund Raising Calculator - v1


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


# main routine

# set up empty list
printout = []
total_list = []
total_amount_list = []

# Get the users charity goal
goal = num_check("What is your goal amount to raise for charity? $")
# print goal
print("$", goal)


# start of loop - get item info
stop = ""
while stop != "xxx":
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'xxx' to quit")

    # if user enters exit code break loop
    if get_product == "xxx":
        break

    # ask user if they are only buying one of this product
    fixed = not_blank("Do you only buy one of this product? ",
                      "Please enter <yes> or <no>").lower()
    # if yes then set this products amount as 1
    if fixed == "yes":
        get_cost = num_check("Cost: $")
        get_amount = 1

    # if no get the user to enter an amount
    else:
        get_cost = num_check("Cost: $")

        get_amount = num_check("Amount: ")

    # append the information the user entered into a single line of code
    printout.append("{:.0f} {}, ${:.2f} ".format(get_amount, get_product, get_cost))

    # calculate total cost of users expenses
    if get_cost > 0:
        total = get_cost * get_amount
    else:
        continue

    # append into a single list
    total_list.append(total)

    # append amount into a single list
    total_amount_list.append(get_amount)

# calculate totals of costs and amounts
total_cost = sum(total_list)
total_amount = sum(total_amount_list)

# calculate a suggested price for the user
suggest1 = total_cost + goal
suggest2 = suggest1 / total_amount


# print out list of information on items and the total cost
print()
print("Amount , Item, Cost")
for item in printout:
    print(item)
print()
print("Total Cost: ")
print("${:.2f}".format(total_cost))
print("Suggested cost: ${:.2f} per item".format(suggest2))
