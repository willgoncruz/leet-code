class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        amount = [ 0 for i in range(len(nums)) ]
        amount[0] = nums[0]
        
        maxValue = 0
        
        for i in range(len(nums)):
            if i < 2:
                maxValue = max(nums[i], maxValue)
                amount[i] = maxValue
                continue
                
            lastNonAdjacent = i - 2
            possible = amount[lastNonAdjacent] + nums[i]
            
            maxValue = max(possible, maxValue)
            amount[i] = maxValue
            
        return maxValue
