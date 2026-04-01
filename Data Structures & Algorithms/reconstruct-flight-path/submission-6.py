class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = {frm:[] for frm, to in tickets}

        for frm, to in tickets:
            graph[frm].append(to)
            graph[frm]

        for node in graph:
            graph[node].sort(reverse=True)
            
        n = len(tickets)

        res = []
        flight_path = []
        def dfs(airport, flights=0):
            flight_path.append(airport)

            if flights == n:
                return flight_path.copy()

            for _ in range(len(graph.get(airport, []))):
                destination = graph[airport].pop()
                
                res = dfs(destination, flights+1)
                if res:
                    return res

                graph[airport].insert(0, destination)

            flight_path.pop()
            return False

        
        return dfs("JFK")
