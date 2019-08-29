class Text(str):
    def dulicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


text = Text("Python")
print(text.lower())
print(text.dulicate())

list = TrackableList()
list.append("1")
print(list)
