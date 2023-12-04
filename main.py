from abc import ABC, abstractmethod
import hashlib

class Figure(ABC):
    hash_table: dict
    amount_of_sides: int

    @abstractmethod
    def __init__(self, sides: list[int|float]) -> None:
        sides.sort()
        parameters = f"{self.__class__.__name__} {sides}"
        curr_hash = hashlib.md5(parameters.encode()).hexdigest()

        if curr_hash in list(self.hash_table.keys()):
            self = self.hash_table[curr_hash]

        self.sides = sides

        parameters = f"{self.__class__.__name__} {self.sides}"
        self.hash_table[hashlib.md5(parameters.encode()).hexdigest()] = self


    @property
    def sides(self) -> list:
        return self.__sides

    @sides.setter
    def sides(self, new_sides: list[int | float]) -> None:
        if not isinstance(new_sides, list):
            raise TypeError('Sides must be list')
        if len(new_sides) != self.amount_of_sides:
            raise ValueError('Amount of sides is not correct')
        for side in new_sides:
            if not isinstance(side, (int | float)):
                raise TypeError('All sides must be int or float')
            if side <= 0:
                raise ValueError('Side cannot be less or equal than 0')
        self.__sides = new_sides

    def get_perimeter(self):
        return sum(self.sides)

    def get_area(self):
        pass

