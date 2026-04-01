class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        min2Index = 1
        min1Index = 2
        for i in range(3,n+1):
            val = min1Index + min2Index
            min2Index = min1Index
            min1Index = val
        return min1Index

