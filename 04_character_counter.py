character = input("Enter the character you would like to count: ")
if len(character) > 1:
    print("Must enter a single character")
    character = input("Enter the character you would like to count: ")

sentence = input("Enter your sentence to search: ")
letters = list(sentence)
counter = 0
for i in letters:
    if i == character:
        counter += 1

print(f"The letter {character} appears {counter} times in '{sentence}'")
