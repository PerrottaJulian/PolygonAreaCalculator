class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
    
  def get_perimeter(self):
    return 2*self.width + 2*self.height
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if (self.height > 50 or self.width >50):
      return "Too big for picture."
    else:
      width = "*"*self.width
      rect = (width + "\n")*self.height
      return rect

  def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"




class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)

  def set_side(self, side):
    self.side = side
    self.set_height(side)
    self.set_width(side)

  def set_width(self, width):
    self.side = width
    self.height = width
    self.width = width

  def set_height(self, height):
    self.side = height
    self.height = height
    self.width = height

  def __str__(self):
    return f"Square(side={self.side})"

  