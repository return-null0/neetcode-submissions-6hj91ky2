class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        formattedS = ""
        for char in s:
            if char.isalnum():
                formattedS = formattedS + char
        start =0
        end = len(formattedS) - 1
        while start < end: 
            if not formattedS[start] == formattedS[end]:
                return False
            start = start + 1
            end = end - 1
        return True




