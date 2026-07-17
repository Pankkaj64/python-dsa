def hcf(a, b):
    """
    Returns the Highest Common Factor (HCF) of two integers.
    """
    while b:
        a, b = b, a % b
    return abs(a)