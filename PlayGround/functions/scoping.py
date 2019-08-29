# Global Variable
message = "a"


def greet(name):
    # Local variable
    message = "b"


def greet_global(name):
    global message
    message = "b"


greet("Vinay")
# this will retrun value a coz python can treat variable seprately event they are same name
print(message)
greet_global("Vinay")
print(message)
