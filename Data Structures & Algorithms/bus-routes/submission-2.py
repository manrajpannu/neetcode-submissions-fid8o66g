from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        stop_to_bus = defaultdict(list)
        n_busses = len(routes)
        for bus in range(n_busses):
            for route in routes[bus]:
                stop_to_bus[route].append(bus)


        queue = deque()
        for bus in stop_to_bus[source]:
            queue.append(bus)

        visited = set() # (bus)
        hops = 1 
        while queue:
        #     # what stop am i on, what bus am i on, how many busses did it take to get here

            for _ in range(len(queue)):
                bus = queue.popleft()
                print(bus)
                if bus in stop_to_bus[target]:
                    return hops
                print(bus)
                if bus in visited:
                    continue
                
                visited.add(bus)

                for bus_stop in routes[bus]:
                    potential_busses = stop_to_bus[bus_stop]

                    for potential_bus in potential_busses:
                        if not potential_bus in visited:
                            queue.append(potential_bus)
            
            hops+=1

            
                
                    
            

            

        

        return -1

