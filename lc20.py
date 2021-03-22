
# If we use recursion like this, it is hard for us to judge the basic element
class Solution:
    def __init__(self):
        self.mirror = {'(': ')', '[': ']', '{': '}', 
                       ')': '(', ']': '[', '}': '{'}

    def split(self, s):
        idx = 1
        while idx < len(s):
            if s[0] == self.mirror[s[idx]]:
                break
            idx += 1
        return s[:idx+1], s[idx+1:]

    def isSymmetric(self, s):
        if len(s) % 2:
            return False
        i, j = 0, len(s)-1
        while i < j:
            if not s[i] == self.mirror[s[j]]:
                return False
            i += 1
            j -= 1
        return True
            

    def isValid(self, s):
        if s[0] in [')', ']', '}'] or len(s) % 2:
            return False

        if not s or self.isSymmetric(s):
            return True
        
        if len(s) == 2 and not self.isSymmetric(s):
            return False

        u, v = self.split(s)
        return self.isValid(u) and self.isValid(v)

class Solution:
    def isValid(self, s):
        if len(s) % 2:
            return False

        ref = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for element in s:
            if element in ref.keys():
                stack.append(element)
            elif stack and element in ref.values():
                if ref[stack[-1]] == element:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if stack:
            return False
        else:
            return True




if __name__ == '__main__':
    print(Solution().isValid("}{"))