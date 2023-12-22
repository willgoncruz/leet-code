class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        mult = 1.0    
        loop = n if n > 0 else -1 * n
        
        if n == 0:
            return 1.0
        
        while loop > 0:
            if loop % 2 == 1:
                mult = mult * x
                loop -= 1
            else:
                x = x * x
                loop = loop / 2
                
        if n < 0:
            mult = 1.0 / mult
            
        return mult
