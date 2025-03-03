# Solution 1:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        expected_len = len(nums) / 2
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            if nums_dict[num] > expected_len:
                return num

# Solution 2:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
