def is_prime(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 2:                       # 0, 1 and negatives are not prime
        return False
    if n % 2 == 0:                  # 2 is the only even prime
        return n == 2
    i = 3
    while i * i <= n:               # only test up to sqrt(n)
        if n % i == 0:
            return False
        i += 2                      # skip even divisors
    return True


if __name__ == "__main__":
    for i in range(20):
        print(f"{i} is prime: {is_prime(i)}")
