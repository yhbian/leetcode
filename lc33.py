class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0

        if target > nums[0]:
            i = 1
            while i < len(nums) and nums[i] - nums[i-1] > 0:
                if target == nums[i]:
                    return i
                i += 1
        if target < nums[0]:
            if target > nums[-1]:
                return -1
            if target == nums[-1]:
                return len(nums) - 1
            i = -2
            while i > -len(nums) and nums[i] - nums[i+1] < 0:
                if target == nums[i]:
                    return len(nums) + i
                i -= 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # --- FLOW ---
        # we can still apply the dichotomy to this half-sorted array
        # 1. we divided the cur_array into [l, m-1], [m, r], m = (l - r) / 2
        #   1.1 [l, m-1] is sorted, we can directly judge if target in it -> update pointers
        #   1.2 [m, r] is sorted ...
        if len(nums) == 1:
            return 0 * (nums[0] == target) + -1 * (nums[0] != target)

        # --- init ---
        l, r = 0, len(nums) - 1

        # ---update---
        while l < r:
            mid = (r + l) // 2
            if mid == l or mid == r:
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                else:
                    return -1

            if nums[mid] == target:
                return mid
            # case 1: left part is sorted
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            # case 2: right part is sorted
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        return -1




"""
Notes:

1. The dichotomy leads to O(log(N)) time complexity

    1.1 SORTED is the key attribute of dichotomy. if we check if target in a list num by num, we 
    need O(log(N)) complexity since we have to compare the element in list with target one by one
    However, the sorted property ensures us to accelerate this case with only O(1) times (head and
    tail). 

    1.2 We can preprocess the list with sorting to utilize dichotomy

    1.3 For HALF-SORTED case, we can still accelerate the decline of search domain. For instance, 
    although the list provided in this problem is not totally sorted, however, we know AT LEAST ONE
    OF THEM IS SORTED! The sorted sub-list can be useful.
"""



