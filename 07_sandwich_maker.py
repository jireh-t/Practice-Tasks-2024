"""Practice task problem 7 - sandwich maker"""

import easygui


# Function to ask user what bread
def bread():
    bread_select = easygui.buttonbox("Please select your bread:\n", "OPTIONS",
                                     choices=["Wholemeal", "White",
                                              "Cheesy White",
                                              "Gluten Free"])
    return bread_select


# Function to ask user what meat
def meat():
    meat_select = easygui.buttonbox("Please select your meat:\n", "OPTIONS",
                                    choices=["Chicken", "Beef",
                                             "Salami",
                                             "Vegan Slice"])
    return meat_select


# Function to ask user what garnish
def garnish():
    selected = []
    while True:
        garnish_select = easygui.buttonbox("Please select your garnish:\n",
                                           "OPTIONS",
                                           choices=["Onion", "Tomato",
                                                    "Lettuce",
                                                    "Cheese"])
        selected.append(garnish_select)
        more = easygui.buttonbox("Would you like another garnish?\n",
                                 "More?", choices=["Yes", "No"])
        if more == "No":
            break
    return selected


# Main Routine

breads = {"Wholemeal": 1,
          "White": 0.8,
          "Cheesy White": 1.2,
          "Gluten Free": 1.4}

meats = {"Chicken": 2.69,
         "Beef": 3,
         "Salami": 4,
         "Vegan Slice": 3.3}

garnishes = {"Onion": 1.69,
             "Tomato": 1,
             "Lettuce": 2,
             "Cheese": 2.5}

bread()
meat()
i = garnish()
print(i)

