from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        n = len(grid)
        m = len(grid[0])
        visited = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))

        distance = -1
        while queue:
            distance += 1

            for x in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) not in visited and 0 <= i < n and 0 <= j< m and (grid[i][j] == 2147483647 or grid[i][j] == 0):
                    
                    grid[i][j] = distance

                    queue.append((i - 1, j))
                    queue.append((i + 1, j))
                    queue.append((i, j - 1))
                    queue.append((i, j + 1))

                    visited[(i, j)] = 1
