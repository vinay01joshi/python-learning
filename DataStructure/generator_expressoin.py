from sys import getsizeof

# touple comprehension
values = (x * 2 for x in range(10000))

print("gen:", getsizeof(values))

# values is now a generaor object used for lagre memeory collction to iterage
# print(values)
# for x in values:
#     print(x)
