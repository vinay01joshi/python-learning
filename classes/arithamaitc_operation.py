class Point:

    # self is the refrence of current point class object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(3, 3)
other = Point(7, 7)
combine = point + other
print(combine.x, combine.y)
