class Solution1:
    def reverseBits(self, n: int) -> int:
        # convert and padding
        inv = bin(n)[2:]
        while len(inv) < 32:
            inv = '0' + inv
        inv = list(inv)

        ret = ''
        while inv:
            ret += inv.pop()
        return int(ret, 2)


class Solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        # convert & padding
        n = bin(n)[2:]
        n = '0' * (32 - len(n)) + n

        def rev(s):
            l = len(s)
            if l == 2:
                return s[1] + s[0]
            return rev(s[l // 2:]) + rev(s[:l // 2])
        
        return int(rev(n), 2)