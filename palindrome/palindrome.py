def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:   # mismatch -> not a palindrome
            return False
        left += 1
        right -= 1
    return True                              # all pairs matched


if __name__ == "__main__":
    print(is_palindrome("racecar"))   # True
    print(is_palindrome("hello"))     # False
