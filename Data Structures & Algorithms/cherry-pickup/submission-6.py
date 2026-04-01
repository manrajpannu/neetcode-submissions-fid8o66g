class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        

        # two guys walking together algo
        n = len(grid)
        dp = [[[[float("-inf")] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
        def dfs(r1=n-1, c1=n-1, r2=n-1, c2=n-1):

            if not (0<= r1 < n and 0 <= c1 < n):
                return float('-inf')
            if not (0 <= r2 < n and 0 <= c2 < n):
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            if dp[r1][c1][r2][c2] != float('-inf'):
                return dp[r1][c1][r2][c2]

            if (r1,c1,r2,c2) == (0,0,0,0):
                return grid[r1][c1]
            else:
                up_up     = dfs(r1-1,c1,r2-1,c2)
                up_left   = dfs(r1-1,c1,r2,c2-1)
                left_up   = dfs(r1,c1-1,r2-1,c2)
                left_left = dfs(r1,c1-1,r2,c2-1)
                res = max([up_up, up_left, left_up, left_left])
                res += grid[r1][c1]

                if r1 != r2 and c1 != c2:
                    res+=grid[r2][c2]

                dp[r1][c1][r2][c2] = res
                return res
        
        return max(0,dfs())

