class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        maxLength = 1

        matrix = [ [ True if i == j else False for i in range(n) ] for j in range(n) ]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                start = i
                matrix[i][i + 1] = True
                maxLength = 2

        for k in range(3, n + 1):
            for i in range(n - k + 1):
                j = i + k - 1
            
                if matrix[i + 1][j - 1] == True and s[i] == s[j]:
                    matrix[i][j] = True
                    if k > maxLength:
                        start = i
                        maxLength = k

        return s[start:start+maxLength]
