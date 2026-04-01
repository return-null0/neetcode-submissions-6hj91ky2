class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        arr[0] = 1
        arr[1] = 2

        if n < 3: return arr[n-1]

        sum = 0
        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n-1]