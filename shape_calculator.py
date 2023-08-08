class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        print(f"Rectangle(width={self.width}, height={self.height})")

    def set_height(self, height):
        self.height = height
        print(f"Rectangle(width={self.width}, height={self.height})")

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            rows = []
            for i in range(self.height):
                rows.append("*" * self.width)
            return print('\n'.join(rows))

    def get_amount_inside(self, shape):
        shape_width = shape.width
        shape_height = shape.height

        if self.height >= shape_height and self.width >= shape_width:
            by_height = self.height // shape_height
            by_width = self.width // shape_width
            amount_inside = by_height * by_width
        else:
            amount_inside = 0
        return amount_inside


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        print(f"Square(side={self.side})")

    def set_width(self, width):
        self.side = width
        print(f"Rectangle(width={self.side}")

    def set_height(self, height):
        self.side = height
        print(f"Rectangle(width={self.side})")
