class Point:

    # self is the refrence of current point class object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic Mthods
    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
print(point)
