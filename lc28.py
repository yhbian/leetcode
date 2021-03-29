class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i: i+len(needle)] == needle:
                return i
            i += 1

        return -1