class Animal:

    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mamel(Animal):
    def __init__(self):
        super().__init__()
        print("Mamal constructor")
        self.weight = 10

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mamel()
print(m.age)
print(m.weight)
