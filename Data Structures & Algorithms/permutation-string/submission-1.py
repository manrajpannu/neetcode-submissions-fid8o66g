class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = dict(Counter(s1))
        c2 = {}
        left = 0

        for right in range(len(s2)):
            l_char, r_char = s2[left], s2[right]  
            
            if c1 == c2:
                return True
            
            if r_char in c1:
                c2[r_char] = c2.get(r_char, 0) + 1

                while c2[r_char] > c1[r_char]:
                    l_char = s2[left]
                    if l_char in c2 and c2[l_char] > 0:
                        c2[l_char] -= 1
                    elif l_char in c2 and c2[l_char] == 0:
                        del c2[l_char]
                    left+=1
                    
                    

            else:
                c2 = {}
                left = right
            print(l_char, r_char, c2)
            
            
        return c1 == c2