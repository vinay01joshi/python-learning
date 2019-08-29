# set is an unorder collection of uniqute item can not conteain duplicate and they are not in squecne

numbers = [1, 2, 3, 3, 3, 4, 4, 5, 5, 1]
first = set(numbers)
second = {9, 2}
# second.add(6)
# second.remove(1)
# print(len(second))
print("First=>", first)
print("Second=>", second)
print("Union=>", first | second)
print("Intrsection=>", first & second)
print("Diffrecence=>", first - second)
print("Symetric Difference", first ^ second)

if 1 in first:
    print("Yes")
