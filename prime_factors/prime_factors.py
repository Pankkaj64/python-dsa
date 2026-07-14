def prime_factors(n):
    """Return the prime factorization of n as a sorted list of primes."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    examples = [1, 2, 3, 4, 12, 100, 13195]
    for value in examples:
        print(f"{value}: {prime_factors(value)}")
