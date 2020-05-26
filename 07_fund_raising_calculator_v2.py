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
selling_items = ""

# Bold print out text option
bold = "\033[1m"
reset = "\033[0;0m"

# introduce user to program
print(bold, "**Fund Raising Calculator**", reset)
print("This program is used to enter products that you will buy for a fund raiser.")
print("Then the program will print out the list of the products, the total cost and a suggested selling price")
print()

# Get the users charity goal
goal = num_check("What is your goal amount to raise for charity? $")
print()

# explain product loop
print("Please enter the products you are purchasing for the fund raiser")
print("--------------------------------------")
print("Input '", bold, "exit", reset, "' to stop entering products")
print("--------------------------------------")

# start of loop - get item info
stop = ""
while stop != "exit":
    print()
    product = []
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'exit' to quit")
    product.append(get_product)

    # if user enters exit code break loop
    if get_product == "exit":
        if len(product) != 0:
            break
        else:
            print("Please enter at least one product")

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

        # ask user if they are selling this item
        selling = not_blank("Are you planning on selling this item? ",
                            "Please input <yes> or <no>")

        if selling == "yes":
            selling_items = get_amount
        else:
            continue

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
suggest2 = suggest1 / selling_items


# print out list of information on items and the total cost
print()
print("----------------")
print("Items:")
for item in printout:
    print(item)
print()
print("Total Cost: ${:.2f}".format(total_cost))
print("----------------")
print("Suggested cost: ${:.2f} per item".format(suggest2))
print("----------------")
