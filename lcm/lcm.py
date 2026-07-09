def lcm(a, b):
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (a, b)):
        raise TypeError("a and b must be integers")
    if a == 0 or b == 0:             # lcm involving zero is defined as 0
        return 0
    a, b = abs(a), abs(b)            # lcm is defined on magnitudes
    x, y = a, b
    while y:                         # Euclid's algorithm for gcd
        x, y = y, x % y
    return a // x * b                # divide first to avoid overflow


if __name__ == "__main__":
    pairs = [(4, 6), (12, 18), (7, 5), (0, 9), (21, 6)]
    for a, b in pairs:
        print(f"lcm({a}, {b}) = {lcm(a, b)}")
