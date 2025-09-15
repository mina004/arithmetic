"""arithmetic functions."""

from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: first integer
        b: second integer

    Returns:
        Sum of a and b.
    """
    raise NotImplementedError


def factorial(n: int) -> int:
    """Compute the factorial of n.

    Args:
        n: non-negative integer

    Returns:
        n! as int

    Raises:
        ValueError: if n is negative
    """
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Check whether n is a prime number.

    A prime number is an integer greater than 1 that has no positive
    divisors other than 1 and itself.

    Args:
        n: integer to test

    Returns:
        True if n is prime; otherwise False.
    """
    raise NotImplementedError
