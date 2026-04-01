class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxSeen = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > maxSeen: maxSeen = area

            if min(heights[left], heights[right]) == heights[left]:
                left+=1
            else:
                right-=1
        return maxSeen