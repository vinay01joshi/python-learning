try:
    #with operator is just like using keyword in c#
    with open("app.py") as file:
        print("File Opend")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("Please enter a valid age")
else:
    print("No exceptions were thorwn")
