class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurse(chosenSet, currentPermutation):
            if len(currentPermutation) == len(nums):
                return [currentPermutation.copy()]
            ans = []
            for i in range(len(nums)):
                if i in chosenSet:
                    continue
                else:
                    chosenSet.add(i)
                    currentPermutation.append(nums[i])
                    temp = recurse(chosenSet, currentPermutation)
                    chosenSet.remove(i)
                    currentPermutation.pop()
                    ans = ans + temp
            return ans
        s = set()
        return recurse(s, [])
            