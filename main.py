# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
# from unittest import main

rect = shape_calculator.Rectangle(51, 51)
rect.set_height(3)
rect.set_width(5)

sq = shape_calculator.Square(9)
sq.set_side(4)

rect.get_picture()
sq.get_picture()

print(rect.get_amount_inside(sq))

