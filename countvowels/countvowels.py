def countvowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    print(countvowels("hello"))


