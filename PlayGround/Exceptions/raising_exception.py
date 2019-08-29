from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or Less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("FirstCode :", timeit(code1, number=10000))
print("SecondCode :", timeit(code2, number=10000))
