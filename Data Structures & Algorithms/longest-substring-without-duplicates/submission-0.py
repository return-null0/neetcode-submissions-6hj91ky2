class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        present = set()
        longest = 0
        left = 0
        right = 0
        
        while right < len(s):
            ele = s[right]

            while ele in present:
                present.remove(s[left])
                left += 1
            
            present.add(ele)
            
            current_length = right - left + 1
            if current_length > longest:
                longest = current_length
                
            right += 1
            
        return longest