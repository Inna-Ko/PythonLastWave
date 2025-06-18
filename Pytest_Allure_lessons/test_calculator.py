import pytest
from calculator import add, subtract, multiply, divide


class TestCalculator:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -3, -8),
        (10.5, 2.5, 13.0),
        (100, 200, 300)
    ])
    def test_add(self, a, b, expected):
        assert add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),
        (0, 0, 0),
        (1, -1, 2),
        (-5, -3, -2),
        (10.5, 2.5, 8.0),
        (100, 50, 50)
    ])
    def test_subtract(self, a, b, expected):
        assert subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 3, -6),
        (-4, -5, 20),
        (2.5, 4, 10.0),
        (10, 10, 100)
    ])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 2, 3.0),
        (10, 5, 2.0),
        (-8, 2, -4.0),
        (-12, -3, 4.0),
        (7.5, 2.5, 3.0),
        (100, 4, 25.0)
    ])
    def test_divide(self, a, b, expected):
        assert divide(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        (5, 0),
        (0, 0),
        (-10, 0),
        (3.14, 0)
    ])
    def test_divide_by_zero(self, a, b):
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            divide(a, b)
