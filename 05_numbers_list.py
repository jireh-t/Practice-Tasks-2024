numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
for number in numbers:
    if number == 353:
        order = numbers.index(number)
        numbers[order] = 53

print(numbers)
