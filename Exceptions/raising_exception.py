def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or Less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
