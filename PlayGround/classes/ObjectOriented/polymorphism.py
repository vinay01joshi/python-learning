from abc import ABC, abstractclassmethod


class UIControl(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class TextBox(UIControl):

    def draw(self):
        print("Draw Text Box")


class DropDownList(UIControl):
    def draw(self):
        print("Draw Dropdown")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
txtbox = TextBox()
draw([ddl, txtbox])
