class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        s = str(x)

        if len(s) == 1:
            return True

        l = len(s) // 2
        for idx in range(l):
            if x[idx] != x[-1-idx]
                return False

        return True


if __name__ == '__main__':
    pass
