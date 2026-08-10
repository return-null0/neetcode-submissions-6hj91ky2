class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxSeen = 0
        ans = 0
        for i in range(len(height)):
            
            if i ==0: 
                maxSeen = height[i]
                maxLeft[i] = 0
                continue
            maxLeft[i] = maxSeen 
            maxSeen = max(maxSeen, height[i])

        maxSeen = 0
        for i in reversed(range((len(height)))):
            if i == len(height) - 1:
                maxSeen = height[i]
                maxRight[i] = 0
                continue
            maxRight[i] = maxSeen
            maxSeen = max(maxSeen, height[i])

        # water count at i == min(maxLeft, maxRight) - height[i]
        for i in range(len(height)):
            value = min(maxLeft[i], maxRight[i]) - height[i]
            if value <= 0:
                ans += 0
            else:
                ans += value
        return ans
        


