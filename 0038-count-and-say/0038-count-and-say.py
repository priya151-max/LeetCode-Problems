class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        res = "1"
        
        # Iteratively build from 2 to n
        for _ in range(n - 1):
            next_str = []
            i = 0
            while i < len(res):
                count = 1
                # Count consecutive identical digits
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                
                # Append "count" followed by the "digit"
                next_str.append(str(count))
                next_str.append(res[i])
                i += 1
            
            res = "".join(next_str)
            
        return res

