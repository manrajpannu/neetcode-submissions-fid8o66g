class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique = {}

        res = 0
        left, right = 0, 0

        while right <= len(s) -1 and left<= len(s) - 1:

            if len(unique.values()) > 1:
                extra = (right-left) - max(unique.values())
            else:
                extra = 0
                
         

            if extra > k :
                unique[s[left]] -= 1
                left += 1
            else:
                unique[s[right]] = unique.get(s[right], 0) + 1
                res = max(res, right-left)
                right+=1

     
        if len(unique.values()) > 1:
                extra = (right-left) - max(unique.values())
        else:
            extra = 0

        if not extra > k :
            res = max(res, right-left)
           
        # res = max(res, right-left)
        return res
                


        