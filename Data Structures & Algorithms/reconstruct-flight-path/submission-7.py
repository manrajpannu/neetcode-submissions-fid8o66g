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
        def dfs(airport):
            # flight_path.append(airport)


            for _ in range(len(graph.get(airport, []))):
                if graph[airport]:
                    destination = graph[airport].pop()
                    dfs(destination)

            res.append(airport)            
            return False

        dfs("JFK")
        return res[::-1]
