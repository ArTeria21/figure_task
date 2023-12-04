import pytest

from figures import Square, Triangle

TEST_SQUARE_PERIMETER = (
    (Square([1, 2, 2, 1]), 6),
    (Square([1, 1, 4, 4]), 10),
    (Square([6, 7, 7, 6]), 26),
)

@pytest.mark.parametrize('square, expected', TEST_SQUARE_PERIMETER)
def test_square_perimeter(square: Square, expected: int | float) -> None:
    assert square.get_perimeter() == expected


TEST_SQUARE_AREA = (
    (Square([1, 2, 2, 1]), 2),
    (Square([1, 1, 4, 4]), 4),
    (Square([6, 7, 7, 6]), 42),
)

@pytest.mark.parametrize('square, expected', TEST_SQUARE_AREA)
def test_square_area(square: Square, expected: int | float) -> None:
    assert square.get_area() == expected


TEST_TRIANGLE_AREA = (
    (Triangle([3, 4, 5]), 6),
    (Triangle([5, 5, 6]), 12),
    (Triangle([5, 5, 8]), 12),
)

@pytest.mark.parametrize('triangle, expected', TEST_TRIANGLE_AREA)
def test_triangle_area(triangle: Triangle, expected: int | float) -> None:
    assert triangle.get_area() == expected

TEST_TRIANGLE_PERIMETER = (
    (Triangle([3, 4, 5]), 12),
    (Triangle([5, 5, 6]), 16),
    (Triangle([5, 5, 8]), 18),
)

@pytest.mark.parametrize('triangle, expected', TEST_TRIANGLE_PERIMETER)
def test_triangle_perimeter(triangle: Triangle, expected: int | float) -> None:
    assert triangle.get_perimeter() == expected
