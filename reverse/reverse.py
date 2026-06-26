# ::1 ---  start stop step
# step -- move backward one by one

# strings are immutable so we convert into list

# s = "helloWorld"
# reverse_string = s[::-1]
# # print(reverse_string)

# print("==============")

# # string = "helloWorld"
# result = ""
# for char in s:
#     result = char + result  # put each char in front.  "h" + "", "e" + "h" ....
# # print(result)


# two pointer swap
# strings are immutable so we convert into list
def reverse(string):
    chars = list(string)
    print(chars)

    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)

if __name__ == "__main__":
    print(reverse("hello"))


