class Solution(object):
    def toString(self, matrix):
        result = ''
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != '':
                    result += matrix[i][j]
        
        return result
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        matrix = [ [ '' for i in range(len(s)) ] for j in range(numRows) ]
        
        i = 0
        column = 0
        
        while i < len(s):
            for k in range(numRows):
                matrix[k][column] = s[i]
                i += 1
                
                if i >= len(s):
                    return self.toString(matrix)
                
            k = numRows - 2
            column += 1
            while k > 0:
                matrix[k][column] = s[i]
                i += 1
                column += 1
                k -= 1
                
                if i >= len(s):
                    return self.toString(matrix)
                
        return self.toString(matrix)
