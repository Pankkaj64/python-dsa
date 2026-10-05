def int_to_roman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.

    Args:
        num (int): Integer between 1 and 3999.

    Returns:
        str: Roman numeral representation.
    """

    if num < 1 or num > 3999:
        raise ValueError("Number must be between 1 and 3999")

    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    result = []

    for value, symbol in zip(values, symbols):
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)