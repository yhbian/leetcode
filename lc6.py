class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return s
        if numRows == 1:
            return s
        groups = len(s) // (2 * numRows - 2)
        cols = groups * (1 + numRows - 2) + numRows - 1
        container = [[0 for j in range(cols)] for i in range(numRows)]
        for idx in range(len(s)):
            flag = idx % (2 * numRows - 2)
            group = idx // (2 * numRows - 2)
            if flag < numRows:
                container[flag][group * (1 + numRows - 2)] = s[idx]
            else:
                container[2 * numRows -2 - flag][group * (1 + numRows - 2) + flag - numRows + 1] = s[idx]

        new_s = ''
        for i in range(numRows):
            for j in range(cols):
                if container[i][j]:
                    new_s += container[i][j]
        return new_s


if __name__ == '__main__':
    print(Solution().convert(s="PAYPALISHIRING", numRows=1))
