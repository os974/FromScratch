from app.main import main
from app.modules.mon_module import addition, multiplication


def test_addition():
    assert addition(3, 5) == 8


def test_multiplication():
    assert multiplication(3, 5) == 15


def test_addition_negatif():
    assert addition(-2, 5) == 3


def test_multiplication_zero():
    assert multiplication(0, 99) == 0


def test_main():
    result_add, result_mul = main()
    assert result_add == 8
    assert result_mul == 15
