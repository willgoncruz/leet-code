import numpy

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        i, j = 0, 0
        mult = 1
        maxMult, minMult, result = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            mx = maxMult * nums[i]
            mn = minMult * nums[i]
            
            maxMult = max(nums[i], mx, mn)
            minMult = min(nums[i], mx, mn)
            result = max(maxMult, result)
        
        return result
