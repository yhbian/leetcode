class Solution1:
    def __init__(self):
        self.ref = {'(': 1, ')': -1}

    def isValid(self, s):
        if not s:
            return True
        count = 0
        for element in s:
            count += self.ref[element]
        return count

    def generateParenthesis(self, n):

        ret = ['']
        idx = 0
        while idx < 2 * n - 1:
            new = []
            while ret:
                c = ret.pop()
                if self.isValid(c + '(')>=0:
                    new.append(c + '(')
                if self.isValid(c + ')')>=0:
                    new.append(c + ')')
            ret = new
            idx += 1
        
        new = []
        while ret:
            c = ret.pop()
            if self.isValid(c + '(') == 0:
                new.append(c + '(')
            if self.isValid(c + ')') == 0:
                new.append(c + ')')
        ret = new
        return ret


class Solution2:
    def generateParenthesis(self, n):
        ret = []
        if n <= 0:
            return ret

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                if left == right:
                    ret.append(s)
                return

            if left == right:
                backtrack(s+'(', left+1, right)
            
            if left > right:
                backtrack(s+'(', left+1, right)
                backtrack(s+')', left, right+1)

        backtrack('', 0, 0)
        return ret                


class Solution3:
    def generateParenthesis(self, n):
        ret = []
        if n <= 0:
            return ret

        def backtrack(s, left, right):
            if left < right:
                return

            if len(s) == 2 * n:
                if left == right:
                    ret.append(s)
                return

            backtrack(s+'(', left+1, right)
            backtrack(s+')', left, right+1)

        backtrack('', 0, 0)
        return ret 

if __name__ == "__main__":
    print(Solution3().generateParenthesis(3))


### Notes

# 1. compared with lc17, two additional arguments is maintained to decide "go deeper or cut & go back"

# 2. as a recursion method, the key argument of backtrack() can be included as:
#   2-1. the goal of the func: start from here and go deeper for what we want
#   2-2. the return criterion: invalid branch or goal reached

# 3. there are two methods to cut:
#   3-1. follow solution2 -> we carefully check whether or not to go deeper
#   3-2. follow solution3 -> we just go deeper and return if the state is not valid


        
        
            
