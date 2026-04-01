class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursToEat(piles, rate):
            hourCount = 0
            for pile in piles:
        # Check if the pile divides perfectly
                if pile % rate == 0:
                    hourCount += pile // rate
                else:
            # There are leftovers, so we add 1 extra hour to the base time
                    hourCount += (pile // rate) + 1
            return hourCount

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            if left == right: return left

            if hoursToEat(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
