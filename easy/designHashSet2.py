class MyHashMap:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        found = False
        for m in self.map:
            if m[0] == key:
                m[1] = value
                found = True
                break
        
        if not found:
            self.map.append([key, value])

    def get(self, key: int) -> int:
        for m in self.map:
            if m[0] == key:
                return m[1]
        return -1

    def remove(self, key: int) -> None:
        for i, m in enumerate(self.map):
            if m[0] == key:
                self.map.pop(i)
                return