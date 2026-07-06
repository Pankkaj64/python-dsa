def fizzbuzz(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n % 15 == 0:          # divisible by both 3 and 5
        return "FizzBuzz"
    if n % 3 == 0:           # divisible by 3
        return "Fizz"
    if n % 5 == 0:           # divisible by 5
        return "Buzz"
    return str(n)            # otherwise the number itself


if __name__ == "__main__":
    for i in range(1, 16):
        print(fizzbuzz(i))   # 1 2 Fizz 4 Buzz ... FizzBuzz
