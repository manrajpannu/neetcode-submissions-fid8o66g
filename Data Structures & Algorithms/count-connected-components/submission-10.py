class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        visited = set()

        adj_list = [ [0] * n for i in range(n)]

        for a, b in edges:
            adj_list[a][b] = 1 
            adj_list[b][a] = 1 

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            for i in range(n):
                if adj_list[node][i]:
                    dfs(i)

            return True



        res = 0
        for node in range(n):
            if node not in visited:
                res+=1
                dfs(node)
        
        return res
