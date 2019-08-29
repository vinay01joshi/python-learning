# List unpacking

numbers = [1, 2, 4]
print(*numbers)

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3, 4]
values = [*first, *second]
print(values)

# dictonary unpacking
dict_first = {"x": 1}
dict_second = {"x": 10, "y": 20}
combine = {**dict_first, **dict_second}
print(combine)
