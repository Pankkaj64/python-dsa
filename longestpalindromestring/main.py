def longestPalindrome(s):

    max_substring = ""

    for left in range(len(s)):
        for right in range(left, len(s)):

            substring = s[left:right + 1]
            if substring == substring[::-1]:
                if len(substring) > len(max_substring):
                    max_substring = substring

    return max_substring
            


            