import collections
import queue


class MyStack:
    def __init__(self):
        self.queue = collections.deque()
        self.queue_help = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.queue_help.append(self.queue.popleft())
        self.queue, self.queue_help = self.queue_help, self.queue
        return self.queue_help.popleft()

    def top(self) -> int:
        while len(self.queue) > 0:
            if len(self.queue) != 1:
                self.queue_help.append(self.queue.popleft())
            else:
                return self.queue[0]
        self.queue, self.queue_help = self.queue_help, self.queue

    def empty(self) -> bool:
        if len(self.queue) == 0 and len(self.queue_help) == 0:
            return True
        return False
class Myqueue:
    def __init__(self):
        self.stack = []
        self.stack_help = []
    def push(self, val : int) -> None:
        self.stack.append(val)
    def pop(self) -> int:
        if len(self.stack) == 0:
            if len(self.stack_help) > 0:
                return self.stack_help.pop()
            else:
                return -1
        else:
            while len(self.stack) > 0:
                self.stack_help.append(self.stack.pop())
            return self.stack_help.pop()
    def peek(self) -> None:
        if len(self.stack) == 0:
            if len(self.stack_help) > 0:
                return self.stack_help[-1]
            else:
                return -1
        else:
            while len(self.stack) > 0:
                self.stack_help.append(self.stack.pop())
            return self.stack_help[-1]
    def empty(self) -> bool:
        if len(self.stack) == 0 and len(self.stack_help) == 0:
            return True
        else:
            return False