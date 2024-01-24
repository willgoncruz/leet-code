class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        i = 0
        j = len(nums) - 1

        result = 0
        closest = 2 * 10**4

        for k in range(len(nums)):
            i, j = k + 1, len(nums) - 1
            
            while (i < j):
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(target - sum)

                if diff < closest:
                    closest = diff
                    result = sum

                if sum - target < 0:
                    i += 1
                else:
                    j -= 1

        return result
