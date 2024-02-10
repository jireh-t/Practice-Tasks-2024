"""Practice task problem 7 - sandwich maker"""
import easygui


# Function to ask user what bread
def bread_menu():
    bread_select = easygui.buttonbox("Please select your bread:\n"
                                     "Wholemeal $1\n "
                                     "White $0.80\n"
                                     "Cheesy White $1.20\n"
                                     "Gluten Free $1.40",
                                     "OPTIONS",
                                     choices=["Wholemeal", "White",
                                              "Cheesy White",
                                              "Gluten Free"])
    return bread_select


# Function to ask user what meat

def meat_menu():
    # List of meats
    meats = ["Chicken", "Beef", "Salami", "Vegan Slice"]
    selected_meat = []  # List of meats user has selected

    # Allow user to select multiple meats
    while True:
        meat_select = easygui.buttonbox("Please select your meat:\n"
                                        "Chicken $2.69\n"
                                        " Beef $3 \n"
                                        "Salami $4 \n"
                                        "Vegan Slice $3.30",
                                        "OPTIONS", meats)
        selected_meat.append(meat_select)  # Add meat to list

        # Remove option so user cannot select again
        meats.remove(meat_select)
        more = easygui.buttonbox("Would you like another meat?\n",
                                 "More?",
                                 choices=["Yes", "No"])
        if more == "No":
            break
    return selected_meat


# Function to ask user what garnish
def garnish_menu():
    # List of garnishes
    garnishes = ["Onion", "Tomato", "Lettuce", "Cheese"]
    selected_garnish = []  # List of garnishes user has selected

    # Allow user to select multiple garnishes
    while True:
        garnish_select = easygui.buttonbox("Please select your garnish:\n"
                                           "Onion $1.69\n"
                                           "Tomato $1\n"
                                           "Lettuce $2\n"
                                           "Cheese $2.50",
                                           "OPTIONS", garnishes)
        selected_garnish.append(garnish_select)  # Add garnish to list

        # Remove option so user cannot select again
        garnishes.remove(garnish_select)
        more = easygui.buttonbox("Would you like another garnish?\n",
                                 "More?",
                                 choices=["Yes", "No"])
        if more == "No":
            break
    return selected_garnish


# Function to calculate prices
def calculate(bread, meat, garnish):
    bread_prices = {"Wholemeal": 1,
                    "White": 0.8,
                    "Cheesy White": 1.2,
                    "Gluten Free": 1.4}

    meat_prices = {"Chicken": 2.69,
                   "Beef": 3,
                   "Salami": 4,
                   "Vegan Slice": 3.3}

    garnish_prices = {"Onion": 1.69,
                      "Tomato": 1,
                      "Lettuce": 2,
                      "Cheese": 2.5}

    total = 0
    total += bread_prices[bread]
    for i in meat:
        total += meat_prices[i]
    for i in garnish:
        total += garnish_prices[i]

    return f"${total}"


# Function to confirm or change
def confirm(bread, meat, garnish):
    bread_prices = {"Wholemeal": 1,
                    "White": 0.8,
                    "Cheesy White": 1.2,
                    "Gluten Free": 1.4}

    meat_prices = {"Chicken": 2.69,
                   "Beef": 3,
                   "Salami": 4,
                   "Vegan Slice": 3.3}

    garnish_prices = {"Onion": 1.69,
                      "Tomato": 1,
                      "Lettuce": 2,
                      "Cheese": 2.5}

    order = ""
    for i in meat:
        order += i

    easygui.buttonbox(f"Your order is:\n"
                      f"Bread: {bread} {bread_prices[bread]}\n"
                      f"")


# Main Routine


b = bread_menu()
m = meat_menu()
g = garnish_menu()
cost = calculate(b, m, g)
print(b)
print(m)
print(g)
print(cost)
