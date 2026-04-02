import heapq
class MedianFinder:

    def __init__(self):
        self.smaller_half = []
        self.bigger_half  = []
        self.n = 0

    def balance(self):
        if self.n % 2 == 0:
            while len(self.smaller_half) > len(self.bigger_half):
                top = heapq.heappop_max(self.smaller_half)
                heapq.heappush(self.bigger_half, top)
            
            while self.bigger_half and len(self.smaller_half) < len(self.bigger_half):
                top = heapq.heappop(self.bigger_half)
                heapq.heappush_max(self.smaller_half, top) 

        else:
            print("before", self.smaller_half[::-1], self.bigger_half)
            while self.smaller_half and len(self.smaller_half) > len(self.bigger_half) + 1:
                top = heapq.heappop_max(self.smaller_half)
                heapq.heappush(self.bigger_half, top)
            
            while self.bigger_half and len(self.smaller_half) < len(self.bigger_half) + 1:
                top = heapq.heappop(self.bigger_half)
                heapq.heappush_max(self.smaller_half, top) 
            print("after", self.smaller_half[::-1], self.bigger_half)

    def addNum(self, num: int) -> None:
        self.n+=1
        if not self.smaller_half:
            heapq.heappush_max(self.smaller_half, num)
        else:
            smaller = self.smaller_half[0]
            if num > smaller:
                heapq.heappush(self.bigger_half, num)
            else:
                heapq.heappush_max(self.smaller_half, num)

        self.balance()

    def findMedian(self) -> float:
        print(self.smaller_half[::-1], self.bigger_half)
        if self.n % 2 == 0:
            return (self.smaller_half[0] + self.bigger_half[0]) / 2
        else:
            return self.smaller_half[0]
        
        