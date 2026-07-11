def is_armstrong(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    
    n = abs(n)  # armstrong numbers are defined on magnitude
    digits = str(n)
    num_digits = len(digits)
    
    total = sum(int(digit) ** num_digits for digit in digits)
    
    return total == n


if __name__ == "__main__":
    numbers = [153, 370, 371, 407, 1634, 8208, 9474, 9, 10, 100]
    for num in numbers:
        result = "is" if is_armstrong(num) else "is not"
        print(f"{num} {result} an Armstrong number")
