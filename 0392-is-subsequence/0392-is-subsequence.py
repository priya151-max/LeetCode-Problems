class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for both strings
        i, j = 0, 0
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            # If characters match, move the pointer for 's'
            if s[i] == t[j]:
                i += 1
            # Always move the pointer for 't'
            j += 1
            
        # If 'i' reached the end of 's', all characters were found in order
        return i == len(s)
