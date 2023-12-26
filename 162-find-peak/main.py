class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        left = 0
        right = len(nums)
        negativeMax = -2147483648
        
        while left <= right:
            middle = left + ((right - left) / 2)
            back = nums[middle - 1] if middle > 0 else negativeMax
            forward = nums[middle + 1] if middle < len(nums) - 1 else negativeMax
            
            if nums[middle] > back and nums[middle] > forward:
                return middle
            
            if back > nums[middle]:
                right = middle - 1
            elif forward > nums[middle]:
                left = middle + 1
            
        return middle # Invalid Case (Error)
