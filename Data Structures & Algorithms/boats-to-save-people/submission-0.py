class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        # time: n log n + n
        # space O(1)

        people.sort()
        l, r = 0, len(people) - 1

        n_boats = 0
        while l <= r:
            
            if people[l] + people[r] <= limit:
                n_boats += 1
                l += 1
                r -= 1
            else:
                n_boats+=1
                r -= 1
        
        return n_boats
