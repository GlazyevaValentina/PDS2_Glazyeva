# Parallelogram to Square
class Parallelogram:
    # Accepting arguments
    def __init__(self, side_length, height):
        self.side_length = side_length
        self.height = height

    # Area calculation of Parallelogram: side length multiply height S = a · h
    def get_area(self):
        return self.side_length * self.height

# Inherited class Area calculation of Square
class Square(Parallelogram):
    # Redefine method
    def get_area(self):
        if self.side_length == self.height:
            return self.height ** 2
        else:
            return "It is not a square"


paraiielogram1 = Parallelogram(9,5)
print(paraiielogram1.get_area())

square1 = Square(8,1)
print(square1.get_area())

square2 = Square(5,5)
print(square2.get_area())
