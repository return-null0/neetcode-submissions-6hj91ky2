class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        def recurse(index, currentSum, targetLeft):
            if targetLeft == 0:
                return [currentSum.copy()]
            if not index < len(candidates):
                return []
            if targetLeft < 0: 
                return []
            
            currentSum.append(candidates[index])
            s1 = recurse(index + 1, currentSum, targetLeft - candidates[index])
            currentSum.pop()


            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            s2 = recurse(index + 1, currentSum, targetLeft)

            return s1 + s2
        return recurse(0,[], target)