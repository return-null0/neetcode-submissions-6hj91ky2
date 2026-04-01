class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = dict()
        distinct = []
        ans = []
        for num in nums:
            if num in frequencyMap:
                frequencyMap[num] = frequencyMap[num] + 1
            else:
                frequencyMap[num] = 1
                distinct.append(num)
        frequencyList = [[] for i in range(len(nums) + 1)]
        for i in distinct:
            frequencyList[frequencyMap[i]].append(i)
        n = len(nums) 
        while n > -1 and len(ans) < k:
            while len(frequencyList[n]) > 0:
                ans.append(frequencyList[n].pop())
            n = n - 1
        return ans
