def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number is a positive integer that equals the sum of its proper divisors.
    Example: 6 is perfect because 1 + 2 + 3 = 6
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    
    if n <= 0:
        return False
    
    # Find sum of proper divisors (all divisors except n itself)
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum == n


if __name__ == "__main__":
    numbers = [6, 28, 496, 8128, 10, 100, 1, 2]
    for num in numbers:
        result = "is" if is_perfect_number(num) else "is not"
        print(f"{num} {result} a perfect number")
