def is_happy(n: int) -> bool:
    """
    Returns True if n is a happy number, otherwise False.

    A happy number eventually reaches 1 when repeatedly
    replacing the number with the sum of the squares
    of its digits.
    """

    seen = set()

    while n != 1:
        if n in seen:
            return False

        seen.add(n)

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return True