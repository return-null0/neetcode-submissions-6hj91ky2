class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            data = abs(nums[i])
            if nums[data-1] < 0:
                return data
            else:
                nums[data-1] = nums[data-1] * -1