class Point:
    # class level attribute shared with all instance of claases
    default_color = "red"

    # self is the refrence of current point class object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
point.z = 11
Point.default_color = "Yellow"
point.draw()
print(point.default_color)
print(Point.default_color)

point2 = Point(5, 6)
point2.draw()
