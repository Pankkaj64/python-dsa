def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):    # multiply 2 * 3 * ... * n
        result *= i
    return result                # 0! and 1! both give 1


if __name__ == "__main__":
    for i in range(6):
        print(f"{i}! = {factorial(i)}")   # 0! = 1 ... 5! = 120
