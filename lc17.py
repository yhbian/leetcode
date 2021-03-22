class Solution:
    def __init__(self):
        self.ref = {'2': 'abc', 
                    '3': 'def', 
                    '4': 'ghi', 
                    '5': 'jkl', 
                    '6': 'mno', 
                    '7': 'pqrs', 
                    '8': 'tuv', 
                    '9': 'wxyz'
                    }

    def decorate(self, ret, num):
        decorated_ret = []
        while ret:
            element = ret.pop()
            for u in self.ref[num]:
                decorated_ret.append(element + u)
        return decorated_ret

    def letterCombinations(self, digits):
        ret = []
        if not digits:
            return ret

        ret = [u for u in self.ref[digits[0]]]
        if len(digits) == 1:
            return ret

        for num in digits[1:]:
            ret = self.decorate(ret, num)

        return ret


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == '__main__':
    print(Solution().letterCombinations('22'))