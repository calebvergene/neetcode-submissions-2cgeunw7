class MinStack:

    def __init__(self):
        self.stack = []

        # so, i need a min stack that uses a stack to track the min element. 
        # the min element will be added each time you find a new min element 
        # then the min element will be removed when you remove that element
        self.min_stack = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
