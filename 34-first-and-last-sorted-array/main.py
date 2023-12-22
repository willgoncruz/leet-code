class Solution(object):
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            i = left + (right - left) / 2
            
            if nums[i] == target:
                return i
                
            if nums[i] < target:
                left = i + 1
            else:
                right = i - 1
        
        return -1
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        result = [-1, -1]
        
        index = self.binarySearch(nums, target)
            
        if index == -1:
            return result
        
        i = index
        while (i > 0 and nums[i - 1] == target):
            i -= 1
            
        result[0] = i
        
        i = index
        while (i < len(nums) - 1 and nums[i + 1] == target):
            i += 1
                
        result[1] = i
        return result
