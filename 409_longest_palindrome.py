class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dict = {}
        length = 0
        for char in s:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
                if letter_dict[char] % 2 == 0:
                    length += 2
        if length < len(s):
            return length + 1
        else:
            return length
