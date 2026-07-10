def sum_of_digits(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    
    n = abs(n)  # sum of digits is defined on magnitude
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
    
    return total


if __name__ == "__main__":
    numbers = [123, 9876, 0, 505, 999, 1000]
    for num in numbers:
        print(f"sum_of_digits({num}) = {sum_of_digits(num)}")
