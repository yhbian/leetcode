class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 1. try double pointer, left must point to a "("
        # 2. the left must be ")" and sum must be 0
        # 3. left can start from -1, and break once match
        # 4. once match, i.e. [3: 17], return
        if not s or len(s) == 1:
            return 0
        count = 0
        for p in s:
            if p == '(':
                count += 1
            else:
                count -= 1

        ret = 0
        for i in range(len(s)-1):
            if s[i] == ')':
                count += 1
                continue

            j = len(s) - 1
            cur_count = count  # i to end
            while j > i:
                if s[j] == '(':
                    cur_count -= 1
                    j -= 1
                    continue
                else:
                    if cur_count == 0:
                        # add criterion
                        if j - i + 1 > ret:
                            ret = j - i + 1
                        break
                    cur_count += 1
                    j -= 1
            count -= 1
        return ret


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) == 1:
            return 0

        ret = 0
        for i in range(len(s)-1):
            if s[i] == ')':
                continue

            # search for the longest valid one start from i
            j = i+1
            count = 1
            while j < len(s) and count >= 0:
                if s[j] == '(':
                    count += 1
                    j += 1
                    continue
                else:
                    count -= 1
                    if count == 0 and (j - i + 1) > ret:
                        ret = j - i + 1
                j += 1

        return ret

"""
Note 1: This solution is O(N^2), time exceeds
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0

        # --- FLOW ---
        # dp[i] stands for the longest valid parentheses *ended* here
        # bound criterion: (i = 0 or 1)
            # dp[0] = 0, dp[1] = 2 if s[:2] = '()' else 0
        # state transition function: (i >= 2)
            # if s[i] == '('
            # if s[i] == ')':
                ## if s[i-1] = '(' --> dp[i] = dp[i-2] + 2
                ## if s[i-1] = ')' --> dp[i] = dp[i - dp[i-1] - 2] + 2
        
        # --- init & boundary criterion ---
        ret = 0
        dp = [0 for i in range(len(s))]
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
            ret = 2
        
        for i in range(2, len(s)):
            if s[i] == ')':
                # case 1
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    if i - dp[i-1] - 1 >=0 and s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]                
                if dp[i] > ret:
                    ret = dp[i]
        return ret


"""
Note:

1. remember this flexible dp, which takes itself as the index ref
2. when using this kind of complicated index ref, preventing the index out of edge!!!
"""
