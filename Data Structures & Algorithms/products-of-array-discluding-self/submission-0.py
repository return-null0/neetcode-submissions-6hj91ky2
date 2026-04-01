class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[len(nums)-1] = nums[len(nums)-1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]


        ans = [0] * len(nums)
        ans[0] = suffix[1]
        ans[len(nums)-1] = prefix[len(nums)-2]

        for i in range(1, len(nums)-1):
            ans[i] = prefix[i-1] * suffix[i+1]

        return ans