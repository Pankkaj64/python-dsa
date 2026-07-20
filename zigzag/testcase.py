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


# --- tests ---
assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("ABCD", 2) == "ACBD"
assert convert("ABCDE", 1) == "ABCDE"
assert convert("A", 5) == "A"
assert convert("AB", 5) == "AB"
assert convert("", 3) == ""
assert convert("HELLO", 2) == "HLOEL"
print("all passed")