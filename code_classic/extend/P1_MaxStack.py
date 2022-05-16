import math
class MaxStack:
    def __init__(self):
        self.stack = []
        self.stack_helper = [-math.inf]
    def push(self, val : int) -> None:
        self.stack.append(val)
        if val >= self.stack_helper[-1]:
            self.stack_helper.append(val)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        if self.stack[-1] == self.stack_helper[-1]:
            self.stack_helper.pop()
        return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return -1
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.stack_helper[-1]

    def popMax(self) -> int:
        temp_stack = []
        res = -1
        while self.stack[-1] != self.stack_helper[-1] and len(self.stack) > 0:
            temp_stack.append(self.stack.pop())
            self.stack_helper.pop()
        if self.stack[-1] == self.stack_helper[-1]:
            res = self.stack.pop()
        while len(temp_stack) > 0:
            temp_val = temp_stack.pop()
            self.stack.append(temp_val)
            if temp_val > self.stack_helpe[-1]:
                self.stack_helper.append(temp_val)
        return res