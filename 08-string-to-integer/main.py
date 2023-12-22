class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        result = 0
        i = 0
        signal = 1
        
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        while (s[i] == ' '):
            i += 1
            if i >= len(s):
                return result
        
        if (s[i] == '-'):
            signal = -1
            i += 1
        elif (s[i] == '+'):
            i += 1
            
        while i < len(s):
            if s[i] in digits:
                result = result * 10 + int(s[i])
                i += 1
            else:
                break
            
        final = result * signal
        final = max(final, -2147483648)
        final = min(final, 2147483647)
        
        return final

