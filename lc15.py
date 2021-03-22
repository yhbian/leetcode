class Solution:
    def threeSum(self, nums):
        ret = []
        l = len(nums)

        if l < 3:
            return []

        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if not nums[i] + nums[j] + nums[k]:
                        candidate = sorted([nums[i], nums[j], nums[k]])
                        if candidate not in ret:
                            ret.append(candidate)
        return ret


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        ret = []
        nums = sorted(nums)
        memory = []
        for i in range(len(nums)):
            k = len(nums) - 1
            for j in range(i+1, len(nums)):
                print(i, j, k)
                while k > j:
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j]] != memory:
                            ret.append([nums[i], nums[j], nums[k]])
                            memory = [nums[i], nums[j]]
                        j += 1
        return ret

class Solution:
    def threeSum(self, nums):
        ret = []

        if len(nums) < 3:
            return ret

        nums = sorted(nums)

        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            memory = None
            while k > j:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    if nums[j] != memory:
                        ret.append([nums[i], nums[j], nums[k]])
                        memory = nums[j]
                j += 1
        return ret


if __name__ == '__main__':
    print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))  # [-2,0,1,1,2]
