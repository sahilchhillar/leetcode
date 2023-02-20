class MyQueue:

    def __init__(self):
        self.queue = []
        self.length = -1

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        if not self.empty():
            data = self.queue.pop(0)
            self.length -= 1
            return data

    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]

    def empty(self) -> bool:
        if self.length == -1:
            return True
        return False
