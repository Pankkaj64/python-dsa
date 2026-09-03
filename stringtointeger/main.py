def stringtointeger(s):
    i = 0
    n = len(s)

    # remove extra space
    while i < n and s[i] == " ":
        i += 1

    # check sign
    sign = 1
    if i < n and s[i] == "-":
        sign = -1
        i += 1
    elif i < n and s[i] == "+":
        i += 1

    # convert to digits
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    # check 32 bit 
    if result * sign > 2 ** 31 - 1:
        return 2 ** 31 -1
    if result * sign < -2 ** 31:
        return -2 ** 31

    return result * sign
    