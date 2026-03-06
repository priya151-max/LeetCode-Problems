class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        for j in range(len(s)):
            result = ""
            for i in range(j, len(s)):
                if s[i] not in result:
                    result += s[i]
                    num = max(num, len(result))
                else:
                    break
        return num