letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [0, 2], [0, 3]]

# Repeat the item in list
zeros = [0] * 5

# Combine the list
combine = zeros + letters

# numbers in list
numbers = list(range(20))
chars = list("Vinay Joshi")
print(len(chars))

# Accessing Items in list

letters[0] = "A"
print(letters[0])
print(letters[-1])
print(letters[0:3])
# copy of list
print(letters[:])
# every iterativ item from list
print(letters[::2])
print(letters)

number = list(range(20))
print(number[::2])
print(number[::-1])

# UnPacking numbers in List
num = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, thrid, *others = num
first, *other, last = num
print(first)
print(second)
print(thrid)
print(others)
print(last)

# Iteration list
for letter in letters:
    print(letter)

# enumerate return touples here
for letter in enumerate(letters):
    print(letter[0], letter[1])

# unpacking veraible in for loop
for index, letter in enumerate(letters):
    print(index, letter)
