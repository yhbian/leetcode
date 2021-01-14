class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        start = 0  # double pointer
        max_len = 1
        for i in range(1, len(s)):
            j = 1
            while i - j >= start:
                if s[i-j] == s[i]:
                    start = i - j + 1
                    break
                j += 1
            this_len = i - start + 1
            if this_len > max_len:
                max_len = this_len

        return max_len


if __name__ == '__main__':
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
