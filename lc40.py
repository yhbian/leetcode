class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        def backtrack(state1, state2, location):
            """
            state1: the current trace
            state2: the current sum
            location: the current node
            """
            if state2 > target or len(state1) > len(candidates):
                return
            if state2 == target:
                ret.append(state1[:])

            k = loc
            while k < len(candidates):
                x = candidates[k]
                backtrack(state1 + [x], state2 + x, k+1)
                while k < len(candidates) and candidates[k] == x:
                    k += 1
        backtrack([], 0, 0)
        return ret
            
    
        