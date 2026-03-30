class MinStack:

    def __init__(self):
        self.min_num = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_num or val <= self.min_num[-1]:
            self.min_num.append(val)
        

    def pop(self) -> None:
        res = self.stack.pop()
        if res == self.min_num[-1]:
            self.min_num.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
