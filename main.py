import shape_calculator

rect = shape_calculator.Rectangle(5, 3)
print(rect.get_area())
rect.set_width(10)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
#print(sq.get_picture())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
