class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        packedData = []
        for i in range(len(position)):
            packedData.append( (position[i], speed[i]) )
        packedData.sort(key= lambda datum: datum[0])
        stack = []
    #distance / speed = time
    # if the time for a car behind a fleet is gt then its a new fleet
        for element in reversed(packedData):
            t = (target - element[0])/element[1]
            if not stack or t > stack[-1]:
                stack.append(t)


        return len(stack)
