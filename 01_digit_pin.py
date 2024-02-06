pin = int(input("Enter your 4-digit secret pin: "))

length = len(str(pin))

while True:
    if length > 4:
        print("Must be 4 digits")
        pin = int(input("Enter your 4-digit secret pin: "))
        length = len(str(pin))

    elif length == 4:
        num = pin
        break

    elif length == 3:
        num = f"0{pin}"
        break

    elif length == 2:
        num = f"00{pin}"
        break

    elif length == 1:
        num = f"000{pin}"
        break

print(f"Your pin is {num}")
