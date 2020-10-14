class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_attribute_Rec(self):
        return (self.x, self.y, self.width, self.height)
x = int(input('введите координату х '))
y = int(input('введите координату y '))
width = int(input('введите  ширину '))
height = int(input('введите высоту '))
r1 = Rectangle(x, y, width, height)
print('Rectangle', r1.get_attribute_Rec())