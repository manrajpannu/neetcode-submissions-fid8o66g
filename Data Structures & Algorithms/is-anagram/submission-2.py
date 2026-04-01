class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        f = {}
        d = {}

        for i in s:
            print(i,f)
            f[i] = 1 + f.get(i, 0)
        for i in t:
            d[i] = 1 + d.get(i, 0)

        return f == d