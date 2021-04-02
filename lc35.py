class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if l == mid or r == mid:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return l+1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid