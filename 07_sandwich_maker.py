"""Practice task problem 7 - sandwich maker"""
import easygui


# Function to ask user what bread
def bread_menu():
    bread_select = easygui.buttonbox("Please select your bread:\n\n"
                                     "Wholemeal $1.00\n "
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
    limit = 0  # User cannot choose more if they have selected everything

    # Allow user to select multiple meats
    while True:
        meat_select = easygui.buttonbox("Please select your meat:\n\n"
                                        "Chicken $2.69\n"
                                        "Beef $3.00 \n"
                                        "Salami $4.00 \n"
                                        "Vegan Slice $3.30",
                                        "OPTIONS", meats)
        selected_meat.append(meat_select)  # Add meat to list
        limit += 1
        # Remove option so user cannot select again
        meats.remove(meat_select)
        # If all options have been selected, move on
        if limit == 4:
            break

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
    limit = 0  # User cannot choose more if they have selected everything

    # Allow user to select multiple garnishes
    while True:
        garnish_select = easygui.buttonbox("Please select your garnish:\n\n"
                                           "Onion $1.69\n"
                                           "Tomato $1.00\n"
                                           "Lettuce $2.00\n"
                                           "Cheese $2.50",
                                           "OPTIONS", garnishes)
        selected_garnish.append(garnish_select)  # Add garnish to list
        limit += 1

        # Remove option so user cannot select again
        garnishes.remove(garnish_select)
        # If all options have been selected, move on
        if limit == 4:
            break

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

    return f"${total:.2f}"


# Function to confirm or change
def confirm(bread, meat, garnish, total):
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

    meat_order = ""
    for i in meat:
        meat_order += f"{i} ${meat_prices[i]:.2f}\n"

    garnish_order = ""
    for i in garnish:
        garnish_order += f"{i} ${garnish_prices[i]:.2f}\n"

    correct = easygui.buttonbox(f"Your order is:\n\n"
                                f"Bread- {bread} ${bread_prices[bread]:.2f}\n\n"
                                f"Meat- {meat_order}\n"
                                f"Garnish - {garnish_order}\n"
                                f"Total - {total}",
                                "CONFIRM",
                                choices=["Confirm", "Make a change"])

    if correct == "Make a change":
        component = easygui.buttonbox("What would you like to change?",
                                      "CHANGE", choices=["Bread", "Meat",
                                                         "Garnish"])
        if component == "Bread":
            bread_menu()

        elif component == "Meat":
            meat_menu()

        elif component == "Garnish":
            garnish_menu()

    elif correct == "Confirm":
        easygui.msgbox("ENJOY!")


# Main Routine
easygui.msgbox("Welcome to sandwich maker!")
bread_chosen = bread_menu()
meat_chosen = meat_menu()
garnish_chosen = garnish_menu()
cost = calculate(bread_chosen, meat_chosen, garnish_chosen)
confirm(bread_chosen, meat_chosen, garnish_chosen, cost)
