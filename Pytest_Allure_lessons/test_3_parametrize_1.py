import pytest

@pytest.mark.parametrize(
	"number",
	[
	    "One", # Тест 1
	    "Two", # Тест 2
	    "Three", # Тест 3
	    "Four", # Тест 4
	    "Five", # Тест 5
	]
)
def test_print_numbers(number):
    print(number)
