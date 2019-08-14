

items = [
    ("Product2", 8),
    ("Product3", 77),
    ("Product4", 14),
    ("Product1", 3),
    ("Product5", 15),
    ("Product6", 55),
    ("Product8", 2)
]

items.sort(key=lambda item: item[1])
print(items)
