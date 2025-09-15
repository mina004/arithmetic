import pytest

from arithmetic.arithmetic import add_numbers, factorial, is_prime


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)


def test_is_prime():
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(9)
    assert not is_prime(0)
