class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(s):

            return s == "".join(list(reversed(s)))

        n = len(s)
        res = []
        ans = []
        def dfs(i):
            print(s[i:])
            if i == n:
                res.append(ans.copy())
            else:
                for end in range(i, n):
                    if is_palindrome(s[i:end+1]):
                        ans.append(s[i:end+1])
                        dfs(end+1)
                        ans.pop()
            
        dfs(0)
        return res