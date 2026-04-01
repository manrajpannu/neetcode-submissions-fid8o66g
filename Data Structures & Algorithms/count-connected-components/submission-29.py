class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = list(range(n))

        def find_parent(node):
            if node == parents[node]:
                return node
            else:
                true_parent = find_parent(parents[node]) 
                parents[node] = true_parent
                return true_parent
            
        for start, end in edges:
            parent_start = find_parent(start)
            parent_end   = find_parent(end)

            parents[parent_start] = min(parent_start, parent_end)
            parents[parent_end]   = min(parent_start, parent_end)
        
        for i in range(n):
            find_parent(i)
        # print(parents)
        return len(set(parents))