class Point:
    # class level attribute shared with all instance of claases
    default_color = "red"

    # self is the refrence of current point class object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class level method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point.zero()
point.draw()
