class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = {}

        def make_edge(a, b):
            if not a or not b:
                return
            
            nodes = graph.get(a, [])
            nodes.append(b)
            graph[a] = nodes

        chars = set()
        for word in words:
            for char in word:
                chars.add(char)

        for i in range(n-1):
            word1, word2 = words[i], words[i+1]

            minL = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minL] == word2[:minL]:
                return ""
            
            l = 0
            while l < minL and word1[l] == word2[l]:
                l+=1
            
            if l == minL:
                continue
            
            make_edge(word1[l], word2[l])
        
        # topological sort
        res = []
        cycle = set()
        visit = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for next_node in graph.get(node, []):
                if not dfs(next_node):
                    return False
            
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        chars_list = sorted(list(chars), reverse=True)
        for char in chars_list:
            if not dfs(char):
                return ""
        
        return "".join(res[::-1])