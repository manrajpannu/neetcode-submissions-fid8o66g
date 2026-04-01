class Solution:


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = n
        par = list(range(n))
        rank = [1] * n

        def find(n):
            if n == par[n]:
                return n
            else:
                true_parent = find(par[n])
                par[n] = true_parent
                return true_parent



        for a, b in edges:
                parent_of_a = find(a)
                parent_of_b = find(b)
                if parent_of_a != parent_of_b:
                    if rank[parent_of_a] >= rank[parent_of_b]: 
                        par[parent_of_b] = parent_of_a
                        rank[parent_of_a] += rank[parent_of_b]
                    else:
                        par[parent_of_a] = parent_of_b
                        rank[parent_of_b] += rank[parent_of_a]
                    res-=1
                
        print(par)
        print(rank)
        return res
