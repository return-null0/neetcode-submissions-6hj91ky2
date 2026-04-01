class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        closedBrackets = dict()
        closedBrackets["}"] = "{"
        closedBrackets[']'] = '['
        closedBrackets[')'] = '('
        for ele in s:
            if ele in closedBrackets and len(openStack) == 0:
                return False
            if ele in closedBrackets and openStack[-1] != closedBrackets[ele]:
                return False
            if ele in closedBrackets and openStack[-1] == closedBrackets[ele]:
                openStack.pop()
                continue

            if not ele in closedBrackets: 
                openStack.append(ele)
        return len(openStack) == 0
            
