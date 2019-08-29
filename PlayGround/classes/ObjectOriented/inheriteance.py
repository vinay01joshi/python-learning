class Animal:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal : Parent or Base class
# Mamel  : Child or  Sub  Class


class Mamel(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mamel()
m.eat()
print(isinstance(m, Animal))
print(issubclass(Mamel, Animal))
