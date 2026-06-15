class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pointer = len(s)-1
        count= 0
        while(pointer>=0):
            if(s[pointer]==" "):
                pointer-=1
            elif(s[pointer].isalpha()):
                count+=1
                pointer-=1
                if(s[pointer]==" "):
                    pointer = -1
        return count
                    
        