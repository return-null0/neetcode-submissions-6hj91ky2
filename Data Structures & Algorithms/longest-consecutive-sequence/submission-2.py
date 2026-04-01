class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxseq = 0
        if len(nums) >= 1: maxseq = 1
        seen = set()
        for num in nums:
            seen.add(num)
        for num in seen:
            if num - 1 in seen:
                continue
            consec = 1
            i = 1

            while num + i in seen:
                consec = consec + 1
                i = i + 1
                if consec > maxseq: maxseq = consec
        return maxseq