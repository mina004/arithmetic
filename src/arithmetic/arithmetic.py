"""Arithmetic functions used in the assignment."""

from __future__ import annotations


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def factorial(n: int) -> int:
    """Compute n! for a non-negative integer n.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
