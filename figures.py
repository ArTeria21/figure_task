from main import Figure

class Square(Figure):
    hash_table = {}
    amount_of_sides: int = 4

    def __init__(self, sides: list[int | float]) -> None:
        super().__init__(sides)

    def get_area(self):
        [first, second] = list(set(self.sides))

        return first * second


class Triangle(Figure):
    hash_table = {}
    amount_of_sides: int = 3

    def __init__(self, sides: list[int | float]) -> None:
        super().__init__(sides)

    def get_area(self):
        [first, second, third] = self.sides
        half_p = self.get_perimeter() / 2

        return (half_p * (half_p - first) * (half_p - second) * (half_p - third)) * 0.5

