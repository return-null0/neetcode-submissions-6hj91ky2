class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for i in nums:
            if i in numbers:
                return True
            numbers.add(i)
        
        return False

        