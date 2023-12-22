class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
                
        n = len(grid[0])
        m = len(grid)
        
        sums = [ [ 0 for i in range(n) ] for j in range(m) ]
        sums[0][0] = grid[0][0]
    
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                if i == 0:
                    sums[i][j] = sums[i][j - 1] + grid[i][j]
                elif j == 0:
                    sums[i][j] = sums[i - 1][j] + grid[i][j]
                else:
                    top = sums[i - 1][j]
                    left = sums[i][j - 1]
                    sums[i][j] = min(top, left) + grid[i][j]
                
        return sums[m - 1][n - 1]
