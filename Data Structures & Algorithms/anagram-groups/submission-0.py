class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = dict()
        for string in strs:
            decomp = [0] * 26
            for letter in string:
                index = ord(letter) - ord('a')
                decomp[index] = decomp[index] + 1
            if tuple(decomp) in grouped:
                grouped[tuple(decomp)].append(string)
            else:
                grouped[tuple(decomp)] = [string]
        return list(grouped.values())