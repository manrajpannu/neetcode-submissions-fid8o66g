class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        parent = list(range(n))
        rank = [1] * n

        res = n

        def find_parent(node):
            if node == parent[node]:
                return node
            else:
                find = find_parent(parent[node])
                parent[node] = find
                return find


        for start, end in edges:
            p1, p2 = find_parent(start), find_parent(end)

            if p1 != p2:

                parent[p1] = min(p1,p2)
                parent[p2] = min(p1,p2)
                res-=1

        print(parent,rank)
        return res
            

