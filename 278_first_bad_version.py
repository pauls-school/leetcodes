# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minimum = 1
        maximum = n
        mid = (minimum + maximum) / 2
        print(mid)
        while isBadVersion(mid) != True and isBadVersion(mid - 1) != False:
            if isBadVersion(mid) == False:
                minimum = mid
            else:
                maximum = mid
            mid = (minimum + maximum) // 2
        return mid
