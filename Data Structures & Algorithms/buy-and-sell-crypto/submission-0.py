class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 101
        bestProfit = 0

        for i in prices:
            if lowestPrice > i:
                lowestPrice = i
            else:
                currProfit = i - lowestPrice
                if bestProfit < currProfit:
                    bestProfit = currProfit
        return bestProfit
        