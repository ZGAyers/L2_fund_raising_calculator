# Component 03 - Calculate the total cost of products


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


# set up empty lists
product = []
amount = []
cost = []

# start of loop
stop = ""
while stop != "xxx":
    get_product = not_blank("Product: ",
                            "Please fill in this field or type 'xxx' to quit")

    if get_product == "xxx" and len(product) > 1:
        break
    elif get_product == "xxx" and len(product) < 1:
        print("Please type in a product")
        continue
    else:
        product.append(get_product)

    get_cost = num_check("Cost: $")
    cost.append(get_cost)

    get_amount = num_check("Amount: ")
    amount.append(get_amount)

total_cost_1 = amount * product


for item in product, cost, amount, total_cost_1:
    print(item)
