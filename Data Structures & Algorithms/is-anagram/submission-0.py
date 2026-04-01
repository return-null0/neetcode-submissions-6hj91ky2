class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        sCount = [0] * 26
        tCount = [0] * 26
        for i in range(len(s)):
            sIndex = ord(s[i]) - ord('a')
            tIndex = ord(t[i]) - ord('a')
            sCount[sIndex] = sCount[sIndex] + 1
            tCount[tIndex] = tCount[tIndex] + 1
        
        for i in range(26):
            if sCount[i] != tCount[i]:
                return False
        return True

