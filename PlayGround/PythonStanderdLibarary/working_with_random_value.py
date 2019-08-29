import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5, 6, 10, 19]))
print(random.choices([1, 2, 3, 4, 5, 6, 10, 19], k=2))

print("".join(random.choices(string.ascii_letters+string.digits, k=4)))

numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
print(numbers)
