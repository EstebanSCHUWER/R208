class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("La largeur ne peut pas être négative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("La hauteur ne peut pas être négative")
        self._height = value

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Trop grand pour faire une image"
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Carree(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def side(self):
        return self.width

    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

    def set_side(self, side):
        self.side = side

    def __str__(self):
        return f"Carree(side={self.width})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.height = 3
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
sq = Carree(9)
print(sq.get_area())
sq.side = 4
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.height = 8
rect.width = 16
print(rect.get_amount_inside(sq))