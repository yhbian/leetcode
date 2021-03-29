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

