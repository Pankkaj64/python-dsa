def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral to an integer.

    Args:
        s (str): Roman numeral made of the symbols I, V, X, L, C, D and M.

    Returns:
        int: Integer value of the numeral.
    """

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    if not s or any(char not in values for char in s):
        raise ValueError("Invalid Roman numeral")

    total = 0

    for i, char in enumerate(s):
        value = values[char]

        # A smaller symbol before a larger one is subtracted (IV = 4, CM = 900)
        if i + 1 < len(s) and value < values[s[i + 1]]:
            total -= value
        else:
            total += value

    return total
