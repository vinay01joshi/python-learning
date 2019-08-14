

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

prices = []
for item in items:
    prices.append(item[1])

print(items)
print(prices)

# Map function converting from one form to antoher
prices = list(map(lambda item: item[1], items))
print(prices)


# Filter items in list
print(list(filter(lambda item: item[1] >= 20, items)))
