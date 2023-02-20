class MyStack:
    def __init__(self):
        self.stack = []
        self.length = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.length += 1
        
    def pop(self) -> int:
        if not self.empty():
            data = self.stack.pop(self.length)
            self.length -= 1
            return data

    def top(self) -> int:
        if not self.empty():
            return self.stack[self.length]

    def empty(self) -> bool:
        if self.length == -1:
            return True
        return False