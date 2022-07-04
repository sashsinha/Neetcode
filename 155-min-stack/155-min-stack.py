from dataclasses import dataclass

@dataclass(frozen=True)
class StackElement:
    element: int
    stack_min: int

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.getMin() if self.stack else val
        self.stack.append(StackElement(val, val if val < curr_min else curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].element

    def getMin(self) -> int:
        return self.stack[-1].stack_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()