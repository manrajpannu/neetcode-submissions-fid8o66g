import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Sort intervals by start_time asc
        Sort query asc
        
        loop through each query:
            while (start_time < query)
                add intervals to heap 
            
            while (end_time < query):
                remove
            
            ans is top of heap


        """

        intervals.sort()
        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        queries.sort()
        pq = []
        res = [0] * len(queries)
        i = 0
        for q, orginal_index in queries:
            
            
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(pq, (size, r))
                i+=1
            
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            
            if pq:
                res[orginal_index] = pq[0][0]
            else:
                res[orginal_index] = -1
        
        
        return res


            