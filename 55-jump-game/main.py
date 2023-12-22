class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxReach = 0
        for i in range(len(nums)-1):
            if i > maxReach:
                return False
            
            maxReach = max(maxReach, nums[i] + i)
        
        return maxReach >= len(nums) - 1
