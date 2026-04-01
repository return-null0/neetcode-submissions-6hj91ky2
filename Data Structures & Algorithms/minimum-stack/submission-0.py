import heapq
class MinStack:

    def __init__(self):
        self.elementStack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.elementStack.append(val)
        if len(self.minimumStack) == 0:
            self.minimumStack.append(val)
        else: 
            
            if self.minimumStack[len(self.minimumStack) - 1] < val:
                self.minimumStack.append(self.minimumStack[len(self.minimumStack) -1])
            else:
                self.minimumStack.append(val)

    def pop(self) -> None:
        self.minimumStack.pop()
        self.elementStack.pop()

    def top(self) -> int:
        return self.elementStack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
        
