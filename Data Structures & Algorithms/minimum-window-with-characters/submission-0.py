class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have=0

        targetMap = {}
        currentMap = {}
        for letter in t:
            targetMap[letter] = targetMap.get(letter, 0) + 1
        need = len(targetMap.keys())
        #procedure sliding window. expand until have == need
        #then inner loop shrink until that is no longer satisfied
        #then continue expanding but record the minimum indices for ans

        left = 0
        smallest = float("inf")
        bestLeft = -1
        for right in range(len(s)):
            letter = s[right]
            currentMap[letter] = currentMap.get(letter, 0) + 1
            if targetMap.get(letter) is not None and currentMap[letter] == targetMap[letter]:
                have+=1
            
            
            while have == need:
                if right - left + 1 < smallest:
                    bestLeft = left
                    smallest = right - left + 1
                currentMap[s[left]] = currentMap[s[left]] -1
                if targetMap.get(s[left],0) > currentMap.get(s[left],0):
                    have-=1
                left+=1
        return "" if bestLeft==-1 else s[bestLeft:bestLeft+smallest]
                