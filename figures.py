from main import figure

class Square(figure):
    amount_of_sides: int = 4

    def get_area(self):
        [first, second] = list(set(self.sides))

        return first * second


class Triangle(figure):
    amount_of_sides: int = 3

    def get_area(self):
        [first, second, third] = self.sides
        half_p = self.get_perimeter() / 2

        return (half_p * (half_p - first) * (half_p - second) * (half_p - third)) * 0.5
