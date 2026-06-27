def countvowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:   # .lower() so "A" counts too
            count += 1
    return count                     # <-- return the number, don't just print


if __name__ == "__main__":
    print(countvowels("hello"))      # 2
