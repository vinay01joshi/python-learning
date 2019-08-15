from pprint import pprint
sentence = "This is most common interview quetion"
chars = {}
for char in sentence:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1

char_sorted = sorted(chars.items(), key=lambda kv: kv[1], reverse=True)
print(char_sorted[0])
#pprint(chars, width=1)
