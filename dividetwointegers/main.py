def divide(dividend: int, divisor: int) -> int:
    """
    Divide two integers without using multiplication,
    division, or modulo operators.
    """

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if divisor == 0:
        raise ZeroDivisionError("Division by zero")

    # Handle overflow case
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0

    while dividend >= divisor:
        temp = divisor
        multiple = 1

        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1

        dividend -= temp
        quotient += multiple

    return -quotient if negative else quotient