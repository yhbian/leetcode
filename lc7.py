class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0

        if x < 0:
            negative = 1
            x = -x
        else:
            negative = 0
        s = str(x)
        l = len(s)
        i = -1
        while not s[i]:
            i -= 1
        l = l + i + 1

        num = 0
        for idx in range(l):
            num += int(s[l-idx-1]) * (10 ** (l-idx-1))
            if (negative and num > 2 ** 31) or (not negative and num > 2 ** 31 -1) :
                return 0
        if negative:
            num = -num
        return num

if __name__ == '__main__':
    print(Solution().reverse(x=1563847412) > 2 ** 31)
