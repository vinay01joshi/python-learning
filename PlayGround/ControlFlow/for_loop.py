for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

    # Successflly sned a meesage
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful Snet a Message")
        break
else:
    print("Attempated 3 times and its failed")


# Nested Loop
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
