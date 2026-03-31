class Solution:
    def reverse(self, n: int) -> int:
        sign = -1 if n < 0 else 1
        n = abs(n)
        reversed_n = 0
        
        while n > 0:
            digit = n % 10
            reversed_n = (reversed_n * 10) + digit
            n //= 10
            

        if reversed_n > 2**31 - 1:
            return 0
            
        return reversed_n * sign