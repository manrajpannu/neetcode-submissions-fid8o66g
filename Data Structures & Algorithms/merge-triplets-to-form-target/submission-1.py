class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        A, B, C = target
        
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            if a > A or b > B or c > C:
                triplets[i] = (0, 0, 0)
            
        seen_a, seen_b, seen_c = False, False, False
        for i in range(len(triplets)):
            a, b, c = triplets[i]
            if a == A: seen_a = True
            if b == B: seen_b = True
            if c == C: seen_c = True
                
            
        if not (seen_a == True and seen_b == True and seen_c == True):
            return False
        return True