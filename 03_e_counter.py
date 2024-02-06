sentence = input("Enter your sentence: ")
letters = list(sentence)
counter = 0
for i in letters:
    if i == "e":
        counter += 1

print(f"The letter e appears {counter} times in '{sentence}'")
