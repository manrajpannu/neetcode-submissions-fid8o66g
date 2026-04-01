class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()

        graph = {}

        for edge in edges:
            s,e = edge

            l = graph.get(s, [])
            l.append(e)
            graph[s] = l

            l = graph.get(e, [])
            l.append(s)
            graph[e] = l

        print(graph) 

     
    
        def dfs(curr):
            if curr in visited:
                return

            visited.add(curr)

            for child in graph.get(curr,[]):
                dfs(child)

        res = 0
        for node in range(n):
            print(node,visited,res)
            if node not in visited:
                res+=1
                dfs(node)

        return res

