
class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None

        ret = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)

        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            j, k = i+1, len(nums)-1
            while k > j:
                cur = nums[i] + nums[j] + nums[k]
                if cur == target:
                    return cur

                if abs(cur - target) < abs(ret - target):
                    ret = cur
    
                if cur < target:
                    j += 1
                if cur > target:
                    k -= 1
        return ret
                

if __name__ == '__main__':
    print(Solution().threeSumClosest(nums = [1,1,-1,-1,3], target = -1))


                
