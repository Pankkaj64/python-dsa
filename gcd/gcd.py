def gcd(a, b):
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (a, b)):
        raise TypeError("a and b must be integers")
    a, b = abs(a), abs(b)            # gcd is defined on magnitudes
    while b:                         # Euclid's algorithm
        a, b = b, a % b
    return a                         # gcd(0, 0) == 0


if __name__ == "__main__":
    pairs = [(12, 18), (48, 36), (17, 5), (0, 9), (100, 25)]
    for a, b in pairs:
        print(f"gcd({a}, {b}) = {gcd(a, b)}")
