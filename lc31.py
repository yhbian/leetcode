class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums

        # special case, the last permutate
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                break
            i += 1
        if i == len(nums) - 1:
            for j in range(len(nums) // 2):
                k = nums[j]
                nums[j] = nums[len(nums) - j - 1] 
                nums[len(nums) - j - 1] = k
            return nums
        
        # for other cases, exchange two elements
        i = -1
        while nums[i] <= nums[i-1]:
            i -= 1

        # search for the closest num to num[key1], special case excluded, key1 must be in range
        key1 = i - 1
        temp, key2 = nums[i] - nums[key1], i
        for k in range(-1, i, -1):
            if 0 < nums[k] - nums[key1] < temp:
                temp = nums[k] - nums[key1]
                key2 = k
        # [key1, seq1, key2, seq2] -> [key2, sorted(key1, seq1, seq2)]
        # seq1: i to key2 - 1  -> i + 1 to key2;  seq2 remains
        key2_val = nums[key2]
        nums[key2] = nums[key1]
        nums[key1] = key2_val
        
        # sorted nums[key1+1: -1]
        nums[key1+1:] = sorted(nums[key1+1:])

        