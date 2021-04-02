class Solution:
    @staticmethod
    def left_boundary(nums, target):
        if nums[0] == target:
            return 0
        l, r = 1, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == l or mid == r:
                if nums[l] == target and nums[l-1] < target:
                    return l
                if nums[r] == target and nums[r-1] < target:
                    return r
                return -1
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target or (nums[mid] == target and nums[mid-1] == target):
                r = mid
            else:
                return mid
        return -1
    
    @staticmethod
    def right_boundary(nums, target):
        if nums[-1] == target:
            return len(nums) - 1
        l, r = 0, len(nums) - 2
        while l <= r:
            mid = (l + r) // 2
            if l == mid or r == mid:
                if nums[l] == target and nums[l+1] > target:
                    return l
                if nums[r] == target and nums[r+1] > target:
                    return r
                return -1
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target or (nums[mid] == target and nums[mid+1] == target):
                l = mid
            else:
                return mid
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # --- FLOW ---
        # we can done the dichonomy as usual, but the criterion will be more complicated
        # 1. lb ---> lb > 0 & (nums[lb-1] < target & nums[lb] == target) or lb == 0 & nums[lb] == target
        # 2. rb ---> rb < len(nums) - 1 & (nums[rb] == target & nums[rb+1] == target) or rb == len(nums) - 1 & nums[rb] == target
        if not nums:
            return [-1, -1]

        return [self.left_boundary(nums, target), self.right_boundary(nums, target)]  


        
            
