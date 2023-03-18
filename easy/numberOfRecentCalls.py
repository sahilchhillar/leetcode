class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        # low, high = t-3000, t
        # count = 0
        # for ping in self.pings:
        #     if ping >= low and ping <= high:
        #         count += 1
        # return count
        while self.pings[0] < t-3000:
            self.pings.pop(0)
        return len(self.pings)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))