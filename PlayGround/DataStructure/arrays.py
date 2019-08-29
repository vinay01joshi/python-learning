from array import array
numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numbers.append(44)
numbers[0] = 1.0
print(numbers)
