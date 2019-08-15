class Point:

    # self is the refrence of current point class object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(3, 3)
other = Point(1, 2)
print(point == other)
print(point > other)

# if we implement __gt__ no need to work with < __lt__ method python will handle this automaticall
print(point < other)
