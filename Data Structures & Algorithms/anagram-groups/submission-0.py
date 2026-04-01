class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_len = len(strs)
        big = {}
        for i in range(strs_len):
            
            small = {}
            for j in strs[i]:
                small[j] = 1 + small.get(j, 0)

            key = ""
            for x in range(97,123):
                if chr(x) in small:
                    key += chr(x) + str(small[chr(x)])
            big[key] = big.get(key,[]) + [strs[i]]

        return list(big.values())
