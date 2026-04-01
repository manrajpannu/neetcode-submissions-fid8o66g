"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        def s_f(interval):
            return interval.start
        intervals.sort(key=s_f) #O(nlogn)
        heap = []
        res = 0
        for interval in intervals: # O(n)
            while heap and heap[0] <= interval.start: # O(logn)
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end) #O(logn)
            res = max(res, len(heap))# O(1)


        return res