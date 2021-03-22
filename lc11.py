
# solution 1: double indices, O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        ret = 0
        while i < j:
            if height[i] < height[j]:
                cur_area = height[i] * (j - i)
                i += 1
            else:
                cur_area = height[j] * (j - i)
                j -= 1
            if cur_area > ret:
                ret = cur_area
        return ret

# solution 2: bisection method, O(NlogN)
class Solution:
    def maxArea(self, height: List[int]) -> int:

        for i in range(len(height)):
            j = len(height) - 1



