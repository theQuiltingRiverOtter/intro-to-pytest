import calculator
import pytest


def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    assert calculator.calculate(180, 240, "add") == 420


def test_subtract():
    assert calculator.calculate(10, 2, "subtract") == 8
    assert calculator.calculate(1000, 200, "subtract") == 800


def test_multiply():
    assert calculator.calculate(3, 4, "multiply") == 12
    assert calculator.calculate(32, 85, "multiply") == 2720


def test_divide():
    assert calculator.calculate(4, 2, "divide") == 2
    assert calculator.calculate(3000, 20, "divide") == 150
    with pytest.raises(ValueError):
        calculator.calculate(4, 0, "divide")
