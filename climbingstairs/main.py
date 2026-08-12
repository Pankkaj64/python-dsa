def climb_stairs(n: int) -> int:
    """
    Return the number of distinct ways to climb n stairs.

    You can climb either 1 step or 2 steps at a time.
    """

    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second