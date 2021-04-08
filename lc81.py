class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # --- FLOW ---
        # apply dichotomy on the partly sorted nums
        # 1. judge the sorted half SH, rest is DSH
        #   1.1 if tar in SH, dichotomy applied
        #   1.2 if not, apply search(DSH) (Realize with recursion?)
        def backtrack(l, r):
            # --- end criterion ---
            if r - l <= 1:
                if nums[l] == target or nums[r] == target:
                    return True
                return False
            # --- go deeper ---
            mid = (l + r) // 2
            if nums[l] < nums[mid] and nums[l] <= target <= nums[mid]:
                ret = backtrack(l, mid)
            elif nums[mid] < nums[r] and nums[mid] <= target <= nums[r]:
                ret = backtrack(mid, r)
            else:
                ret = backtrack(l, mid) or backtrack(mid, r)
            return True if ret else False 
        ret = backtrack(0, len(nums) - 1)
        return ret