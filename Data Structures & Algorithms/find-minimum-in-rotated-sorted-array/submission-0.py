class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # We are on the high segment, minimum is strictly to the right
                left = mid + 1
            else:
                # We are on the low segment, minimum is at mid or to the left
                right = mid
                
        # left and right converge on the exact minimum element
        return nums[left]