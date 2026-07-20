def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = ["" for _ in range(num_rows)]
    row, step = 0, 1

    for ch in s:
        rows[row] += ch
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step

    return "".join(rows)


