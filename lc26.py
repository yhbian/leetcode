class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:  # go to the first next j
                j += 1
            if j < len(nums):  # i+1 <= j < len(nums)
                i += 1
                nums[i] = nums[j]
            else:
                return i + 1