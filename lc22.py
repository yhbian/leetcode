class Solution:
    def decorate(candidates):
        decorated_candidiates = []
        ref = {'(': -1, '': 0, ')': 1}
        for candidate in candidates:


            

    def generateParenthesis(self, n):
        ret = ['()']
        idx = 1
        while idx < n:
            ret = self.decorate(ret)
            idx += 1
        return ret


        
        

        
        
        
            
