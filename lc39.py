class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        def backtrack(state, loc):
            if sum(state) == target:
                ret.append(state[:])
            if sum(state) > target:
                return
            
            for k in range(loc, len(candidates)):
                backtrack(state=state + [candidates[k]], loc=k)
        backtrack(state=[], loc=0)
        return ret
        
            

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        def backtrack(state1, state2, loc):
            if state2 == target:
                ret.append(state1[:])
            if state2 > target:
                return
            
            for k in range(loc, len(candidates)): # opened doors
                # update state
                state1 += [candidates[k]]
                state2 += candidates[k]
                backtrack(state1=state1, state2=state2, loc=k)
                # reset
                state1.pop()
                state2 -= candidates[k]
        backtrack(state1=[], state2=0, loc=0)
        return ret


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates = sorted(candidates)
        def backtrack(state1, state2, loc):
            if state2 > target:
                return
            if state2 == target:
                ret.append(state1[:])
            
            for k in range(loc, len(candidates)): # opened doors
                # update state
                backtrack(state1=state1 + [candidates[k]], state2=state2 + candidates[k], loc=k)
        backtrack(state1=[], state2=0, loc=0)
        return ret

        