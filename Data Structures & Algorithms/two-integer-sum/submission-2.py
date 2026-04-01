class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = dict()
        for index, num in enumerate(nums):
            present[num] = index
            
        for index, num in enumerate(nums):
            complement = target - num
            if complement in present and index != present[complement]:
                return [index, present[complement]]

