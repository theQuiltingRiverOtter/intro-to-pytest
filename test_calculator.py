import calculator
import pytest


# basic function test
def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    assert calculator.calculate(180, 240, "add") == 420
    assert calculator.calculate(-52, -3, "add") == -55
    assert calculator.calculate(-3, 3, "add") == 0
    assert calculator.calculate(3.0, 3, "add") == 6.0
    assert calculator.calculate(-9.5, -2.3, "add") == -11.8


def test_subtract():
    assert calculator.calculate(10, 2, "subtract") == 8
    assert calculator.calculate(1000, 200, "subtract") == 800
    assert calculator.calculate(-3, -5, "subtract") == 2
    assert calculator.calculate(-10, 8, "subtract") == -18
    assert calculator.calculate(10.5, 2.5, "subtract") == 8.0
    assert calculator.calculate(3, 0.5, "subtract") == 2.5


def test_multiply():
    assert calculator.calculate(3, 4, "multiply") == 12
    assert calculator.calculate(32, 85, "multiply") == 2720
    assert calculator.calculate(-3, -5, "multiply") == 15
    assert calculator.calculate(-10, 8, "multiply") == -80
    assert calculator.calculate(2.5, 2.5, "multiply") == 6.25
    assert calculator.calculate(-3, 0.5, "multiply") == -1.5


def test_divide():
    assert calculator.calculate(4, 2, "divide") == 2
    assert calculator.calculate(3000, 20, "divide") == 150
    assert calculator.calculate(-10, -2, "divide") == 5
    assert calculator.calculate(-40, 5, "divide") == -8
    assert calculator.calculate(12, 2.5, "divide") == 4.8
    assert calculator.calculate(-3, 0.5, "divide") == -6
    with pytest.raises(ValueError):
        calculator.calculate(4, 0, "divide")


# test output
def test_terminal_output(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "10", "2", "multiply"])
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: 20.0\n"


def test_argument_passing(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: 3.0\n"


def test_not_enough_arguments(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "3", "2"])
    with pytest.raises(SystemExit) as sample:
        calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Usage: calculator.py <num1> <num2> <operation>\n"
    assert sample.type == SystemExit


def test_not_correct_sys_arg_3(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["calculator.py", "3", "4", "mult"])
    calculator.main()
    captured = capsys.readouterr()
    assert captured.out == "Result: None\n"


def test_sys_args_2_3_not_numbers(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["calculator.py", "three", "4", "add"])
    pytest.raises(TypeError)
