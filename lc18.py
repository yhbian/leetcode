class Solution:
    def fourSum(self, nums, target):
        ret = list()
        if len(nums) < 4:
            return ret

        nums = sorted(nums)
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j-1] = nums[j]:
                    continue
                k, l = j+1, len(nums)-1

                memory = None
                while k < l:

                    if nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                        continue
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if nums[k] != memory:
                            ret.append([nums[i], nums[j], nums[k], nums[l]])
                            memory = nums[k]
                    k += 1
                    
        return ret