class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_len = 0
        length = 0
        for letter in s:
            if letter not in substring:
                substring.append(letter)
                length += 1  
            else:
                substring = substring[substring.index(letter) + 1:]
                substring.append(letter)
                length = len(substring)
            if length > max_len:
                max_len = length      
        return max_len
