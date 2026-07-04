def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b   # advance the pair by one step
    return a              # nth Fibonacci number


if __name__ == "__main__":
    print(fibonacci(0))   # 0
    print(fibonacci(1))   # 1
    print(fibonacci(10))  # 55
