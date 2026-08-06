class Solution:

    def evenCenter(self, center, s):
        if center < 0 or center >= len(s) - 1: 
            return 0
        
        left = center 
        right = center + 1
        high = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            high = max(high, (right - left) + 1 )
            left -= 1
            right += 1

        return high

    def oddCenter(self, center, s):
        if center < 0 or center >= len(s): 
            return 0
        
        high = 1
        left = center 
        right = center
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            high = max(high, (right - left) + 1 )

            left -= 1
            right += 1
            
        return high

    def longestPalindrome(self, s: str) -> str:
        high = 0
        isEvenCenter = True
        
        best_center = 0

        for i in range(len(s)):
            odd = self.oddCenter(i, s)
            
            even = self.evenCenter(i, s)
            
            if odd > high:
                high = odd
                isEvenCenter = False
                best_center = i
                
            if even > high:
                high = even
                isEvenCenter = True
                best_center = i
                
        ans = ""
        
        if isEvenCenter:

            half = high // 2
            
            ans = s[(best_center - (half - 1)): (best_center + half) + 1]
        else:
            half = (high - 1) // 2
            ans = s[(best_center - half): (best_center + half) + 1]

        return ans