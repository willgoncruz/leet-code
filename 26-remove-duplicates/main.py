class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        k = 0
        lastPos = i
        
        while i < len(nums):    
            
            while i < len(nums) and nums[i] == nums[lastPos]:
                i += 1
            
            if i != lastPos + 1 and i < len(nums):
                nums[lastPos + 1] = nums[i]
            
            lastPos = lastPos + 1
            k += 1
            
        return k
