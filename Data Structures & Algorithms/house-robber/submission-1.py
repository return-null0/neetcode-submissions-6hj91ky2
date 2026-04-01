class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle edge cases for very short arrays
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        # Correctly initialize the first two maximums
        twoHouseAgoMax = nums[0] 
        oneHouseAgoMax = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # If keeping the previous max is strictly better than robbing this house
            if oneHouseAgoMax > nums[i] + twoHouseAgoMax:
                current_max = oneHouseAgoMax
            # Otherwise, it is better to rob this house and combine it with the older max
            else:
                current_max = nums[i] + twoHouseAgoMax
                
            # Shift the variables forward for the next iteration
            twoHouseAgoMax = oneHouseAgoMax
            oneHouseAgoMax = current_max
            
        return oneHouseAgoMax