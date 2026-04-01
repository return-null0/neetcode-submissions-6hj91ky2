class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        windowSize = len(s1)
        left, right = 0, windowSize - 1

        targetMap = {}
        windowMap = {}
        
        # Populate the target map
        for letter in s1:
            targetMap[letter] = targetMap.get(letter, 0) + 1
            
        # Populate the map for the first window
        for i in range(windowSize):
            letter = s2[i]
            windowMap[letter] = windowMap.get(letter, 0) + 1
            
        # Check if the very first window happens to be a match
        if windowMap == targetMap:
            return True
            
        # Slide the window across the rest of the string
        for i in range(len(s2) - len(s1)):
            
            # 1. Remove the leftmost character as the window slides past it
            left_char = s2[left]
            windowMap[left_char] -= 1
            if windowMap[left_char] == 0: 
                del windowMap[left_char]
                
            # physically move the pointers
            left += 1
            right += 1
            
            # 2. Add the new rightmost character that just entered the window
            right_char = s2[right]
            windowMap[right_char] = windowMap.get(right_char, 0) + 1
            
            # Check the newly formed window
            if windowMap == targetMap: 
                return True
                
        return False