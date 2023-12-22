class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1

        results = []
        trios = set()

        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            
            while (i < j):
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == 0:
                    r = [nums[i], nums[j], nums[k]]
                    r.sort()
                    pos = (r[0], r[1], r[2])
                    if (i != j and j != k and i != k and not pos in trios):
                        results.append(r)
                        trios.add(pos)

                if sum < 0:
                    i += 1
                else:
                    j -= 1

        
        return results
