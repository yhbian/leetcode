class Solution:
    def hammingWeight(self, n):
        return sum([int(s) for s in bin(n)[2:]])


if __name__ == '__main__':
    print(Solution().hammingWeight(00000000000000000000000010000000))


### Notes:

# variable-precious SWAR Algorithm