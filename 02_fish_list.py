market = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory",
          "red cod"]

new_list = []
for fish in market:
    letters = list(fish)
    new_list.append(letters)

for i in new_list:
    print([i][0][0])

print("-----------")

for i in new_list:
    print([i][0][0])
    print([i][0][1])
    print([i][0][2])

print("-----------")

lengths = []
for i in new_list:
    num = len(i)
    lengths.append(num)
    longest = lengths.index(max(lengths))
print(market[longest])

print("-----------")

two = []
for i in new_list:
    if " " in i:
        two.append(new_list.index(i))

for i in two:
    print(market[i])

print("-----------")

for fish in market:
    if "cod" in fish:
        print(fish)
