class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        pathsCount = [[ 0 for i in range(n + 1) ]] * (m + 1)
        pathsCount[1][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pathsCount[i][j] = pathsCount[i - 1][j] + pathsCount[i][j - 1]

        return pathsCount[m][n]
