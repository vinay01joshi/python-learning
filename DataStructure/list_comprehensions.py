
items = [
    ("Product2", 8),
    ("Product3", 77),
    ("Product4", 14),
    ("Product1", 3),
    ("Product5", 15),
    ("Product6", 55),
    ("Product8", 2)
]
prices = list(map(lambda item: item[1], items))
# cophrehencive way
prices = [item[1] for item in items]

filtedred = list(filter(lambda item: item[1] >= 20, items))
# cophrehencive way
filtedred = [item for item in items if item[1] >= 20]
print(prices)
print(filtedred)
