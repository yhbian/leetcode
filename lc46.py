class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(state, loc): # 
            if loc == len(nums):
                ret.append(state)
                return 

            nxt = nums[loc + 1]
            for i in range(state+1):
                state.insert(i, nxt)
                backtrack(state, loc+1)
                del state[i]

        backtrack([], 0)
        return ret
            
ßßß