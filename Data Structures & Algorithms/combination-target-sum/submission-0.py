class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def recurse(index, targetLeft, currentSum):

            if not index < len(nums):
                return []
            if targetLeft < 0:
                return []
            if targetLeft == 0:
                return [currentSum.copy()]

            currentSum.append(nums[index])
            s1 = recurse(index, targetLeft - nums[index], currentSum)
            currentSum.pop()

            s2 = recurse(index + 1, targetLeft, currentSum)

            return s1 + s2
        return recurse(0,target, [])
