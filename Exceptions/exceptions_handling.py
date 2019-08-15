try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("Please enter a valid age")
else:
    print("No exceptions were thorwn")
