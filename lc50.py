class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if n == 0:
            return ret

        if n > 0:
            while n:
                ret *= x
                n -= 1

        if n < 0:
            while n:
                ret = ret / x
                n += 1
        return ret

class Solution:
    def myPow(self, x, n):
        # end criterion
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        return self.myPow(x, n // 2) * self.myPow(x, n // 2 + n % 2)


class Solution:
    def myPow(self, x, n):
        # end criterion
        if -1 <= n <= 1:
            return (n == -1) * (1 / x) + (n == 0) * 1 + (n == 1) * x

        half = self.myPow(x, n // 2)
        return half * half if not n % 2 else half * half * x

if __name__ == '__main__':
    print(Solution().myPow(2, 2))


