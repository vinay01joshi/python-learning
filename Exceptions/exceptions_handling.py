try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Please enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thorwn")
print("Program continues")
