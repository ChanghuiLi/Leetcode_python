import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.mini_stack = -1
    def push(self, value:int) -> None:
        self.stack.append(value)
        if value <= self.mini_stack:
            self.mini_stack = value
    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack == self.mini_stack[-1]:
                self.mini_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1]

