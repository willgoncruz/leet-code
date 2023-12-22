import heapq

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        heapq.heapify(nums)
        maxLength = 1
        currentLength = 1
        lastNumber = heapq.heappop(nums)
        
        for _ in range(len(nums)):
            n = heapq.heappop(nums)
            if lastNumber == n:
                continue
                
            if lastNumber + 1 == n:
                currentLength += 1
                maxLength = max(maxLength, currentLength)
            else:
                currentLength = 1
            lastNumber = n
                
        return maxLength
