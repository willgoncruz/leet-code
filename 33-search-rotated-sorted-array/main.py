class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(nums: List[int], start: int, end: int) -> int:
            if start > end:
                return -1

            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                return binary(nums, middle + 1, end)
            
            return binary(nums, start, middle - 1)

        k = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                k = i
        
        if k == -1:
            return binary(nums, 0, len(nums) - 1)

        first = binary(nums, 0, k)
        second = binary(nums, k + 1, len(nums) - 1)

        return max(first, second)

