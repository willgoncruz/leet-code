class Solution(object):
    def minimumTotal(self, triangle):
        i = len(triangle) - 2
        while i > -1:
            for j in range(0, len(triangle[i])):
                n = triangle[i][j]
                leftSum = n + triangle[i+1][j]
                rightSum = n + triangle[i+1][j + 1]
                triangle[i][j] = min(leftSum, rightSum)
            i -= 1
        
        return triangle[0][0]
