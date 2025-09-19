# src/arithmetic/arithmetic.py

def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def factorial(n: int) -> int:
    """Compute n! for a non-negative integer n.

    Raises:
        ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3
    if n % 2 == 0:
        return False
    # check odd divisors up to sqrt(n)
    i = 3
    limit = int(n**0.5) + 1
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True
