class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (not nums1) and (not nums2):
            return None
        nums = []
        if not nums1:
            nums = nums2
        elif not nums2:
            nums = nums1
        else:
            i, j = 0, 0
            while (i < len(nums1)) and (j < len(nums2)):
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            if i < len(nums1):
                nums.extend(nums1[i:])
            else:
                nums.extend(nums2[j:])
        l = len(nums)
        if l % 2:
            return nums[(l-1)//2]
        else:
            return (nums[l//2 -1] + nums[l//2])/2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))


