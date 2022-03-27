class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):                    # pri str i repr, ma str prednost, stringova reprezentace, repr je vedlejsi,
                                                #popisuje tu vedlejsi funkci
        return f'Rectangle(width={self.width}, height={self.height})'

    def __repr__(self):
        return f'Obdelnik(width={self.width}, height={self.height})'

    def set_width(self, new_width):         #neni tady return, jen nastavuje hodnoty, se kterymi dale pracujeme
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture!"
        return self.height * ('*' * self.width + '\n')


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return f'Delka strany ctverce je {self.side}'

    def set_side(self, new_side):
        self.side = new_side

    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

rect = Rectangle(10, 5)
rect.set_width(5)

ctverec = Square(5)
print(ctverec.get_area())
print(ctverec)
print(ctverec.get_perimeter())
print(ctverec.width)
print(ctverec.height)
print(ctverec.get_picture())

# print(rect)
#
# print(rect.get_diagonal())
# print(rect.get_perimeter())
# print(rect.get_area())
# print(rect.get_picture())