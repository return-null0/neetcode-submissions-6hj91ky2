class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def recurse(subset, index):
            if not index < len(nums):
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                ans.append(subset.copy())
                recurse(subset, i + 1)
                subset.pop()
        recurse([], 0)
        return ans

