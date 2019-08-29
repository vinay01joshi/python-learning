def greet(name):
    print(f"Hi {name}")

# function 1 - Performa a task
# function 2 - return a value


def get_greeting(name):
    return f"Hi {name}"


mesage = get_greeting("Vinay")
file = open("content.txt", "w")
file.write(mesage)
# print(mesage)
