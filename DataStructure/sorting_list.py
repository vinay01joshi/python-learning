numbers = [3, 5, 7, 2, 9, 1, 0]
# sorting in accending order
numbers.sort()
# sorting in decending order
numbers.sort(reverse=True)

# sorted method
print(sorted(numbers, reverse=True))
print(numbers)


items = [
    ("Product2", 8),
    ("Product3", 77),
    ("Product4", 14),
    ("Product1", 3),
    ("Product5", 15),
    ("Product6", 55),
    ("Product8", 2)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
