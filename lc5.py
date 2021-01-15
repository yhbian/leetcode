import time

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        l = len(s)
        if l == 1:
            return s
        palindrome = s[0]
        max_l = 1
        dp = [[False for j in range(l)] for i in range(l)]

        for i in range(l):
            dp[i][i] = True

        for j in range(1, l):
            for i in range(j):
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        this_l = j - i + 1
                        if this_l > max_l:
                            max_l = this_l
                            palindrome = s[i:j+1]
                else:
                    if (s[i] == s[j]) and dp[i+1][j-1]:
                        dp[i][j] = True
                        this_l = j - i + 1
                        if this_l > max_l:
                            max_l = this_l
                            palindrome = s[i:j+1]
        return palindrome


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         if size < 2:
#             return s
#
#         dp = [[False for _ in range(size)] for _ in range(size)]
#
#         max_len = 1
#         start = 0
#
#         for i in range(size):
#             dp[i][i] = True
#
#         for j in range(1, size):
#             for i in range(0, j):
#                 if s[i] == s[j]:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 else:
#                     dp[i][j] = False
#
#                 if dp[i][j]:
#                     cur_len = j - i + 1
#                     if cur_len > max_len:
#                         max_len = cur_len
#                         start = i
#         return s[start:start + max_len]





if __name__ == '__main__':
    time1 = time.time()
    print(Solution().longestPalindrome(s="abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
    # print(Solution().longestPalindrome(s="busislnescsicxpvvysuqgcudefrfjbwwjcchtgqyajdfwvkypfwshnihjdztgmyuuljxgvhdiwphrweyfkbnjgerkmifbirubhseuhrugwrabnjafnbdfjnufdstjbkuwtnpflffaqmjbhssjlnqftgjiglvvequhapasarlkcvbmkwnkuvwktbgfoaxteprobdwswcdyddyvrehvmxrrjiiidatidlpihkbmmruysmhhsncmfdanafdrfpdtfgkglcqpwrrtvacuicohspkounojuziittugpqjyhhkwfnflozbispehrtrnizowrlzcuollagxwtznjwzcumvedjwokueuqktvvouwnsmpxqvvpuwprezrbobrpnwaccwljchdguubjulyilzvmandjjleitweybqkjttschrjjlebnmponvlktzzcdtuybugggcqffkcffpamauvxfbonjrobgpvlyzveiwemmtdvbjciaytvesnocnjrwodtcokgcuoiicxapmrzpkfphjniuvzjrhbnqndfshoduejyktebgdabidxlkstepuwvtrtgbxaeheylicvhrxddijshcvdadxzsccmainyfpfdhqdanfccqkzlmhsfilvoybqojlvbcixjzqpbngdvesuokbxhkomsiqfyukvspqthlzxdnlwthrgaxhtpjzhrugqbfokrdcyurivmzgtynoqfjbafboselxnfupnpqlryvlcxeksirvufepfwczosrrjpudbwqxwldgjyfjhzlzcojxyqjyxxiqvfhjdwtgoqbyeocffnyxhyyiqspnvrpxmrtcnviukrjvpavervvztoxajriuvxqveqsrttjqepvvahywuzwtmgyrzduxfqspeipimyoxmkadrvrdyefekjxcmsmzmtbugyckcbjsrymszftjyllfmoeoylzeahnrxlxpnlvlvzltwnmldi"))
    # print(Solution().longestPalindrome(s='aaa'))
    print(time.time() - time1)
