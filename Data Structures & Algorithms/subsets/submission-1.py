class Solution:

    def recurse(self, index, curr, nums):
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.ans.append(curr.copy())
            Solution.recurse(self, i+1, curr, nums)
            curr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        curr = []
        Solution.recurse(self, 0, curr, nums)
        return self.ans
        