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
    # Using a generator with any() ensures all lines are executed even when the range is empty (e.g., n=2)
    return not any(n % d == 0 for d in range(2, int(n ** 0.5) + 1))
