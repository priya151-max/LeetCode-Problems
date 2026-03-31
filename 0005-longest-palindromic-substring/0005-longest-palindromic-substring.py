class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        start, end = 0, 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return r - l - 1
        for i in range(len(s)):
            length = max(expand(i, i), expand(i, i + 1))
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end+1]