import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)

        projects = []
        for i in range(n):
            projects.append((capital[i], profits[i]))

        pq = []
        projects.sort() 
        res = 0
        j = 0
        print(projects, pq)
        for i in range(k):
            while j < n and projects[j][0] <= w:
                
                heapq.heappush_max(pq, projects[j][1])
                j+=1
            
            if pq:
                w+=heapq.heappop_max(pq)
        
        return w
            