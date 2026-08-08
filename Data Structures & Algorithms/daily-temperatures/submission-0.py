class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                oldIndex = stack[-1]
                result[oldIndex] = i - oldIndex
                stack.pop()
            stack.append(i)
        return result