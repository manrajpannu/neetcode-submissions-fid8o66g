class MinStack:

    def __init__(self):
        self.stack = []
        # self.curr_min = float("-inf")

    def push(self, val: int) -> None:
        # self.curr_min = min(self.curr_min, val)
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))

        else:
            self.stack.append((val,val))


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][-1]
        
