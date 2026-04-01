class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        # intervals.sort()
        # sort by start_time, then smallest to largest interval

        result = []
        n = len(intervals)
        print(intervals)
        h = {}
        for i in range(n):
            left, right = intervals[i]
            size = right - left + 1
            for j in range(left, right+1):
                if j in h:
                    if h[j] >= size:
                        h[j] = size
                else:
                    h[j] = size

            
        for query in queries:
            if query in h:
                result.append(h[query])
            else:
                result.append(-1)

        return result
