from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # [1,2,1,2,3]
        #  [1] n=1, [1,2] [2]
        #  [1,2,1,2,3]=3, [1,2,1,2]=2 [1,2,1]=2 [1,2]=2 [1]=1 
        # 
        # if arrau is good, i can remove as many subarray 
        # if array is bad, i can remove


        # 121212121
        def atMost(k):
            counter = defaultdict(int)
            res = 0
            l = 0
            for r in range(len(nums)):
                counter[nums[r]]+=1
                while len(counter) > k:
                    counter[nums[l]]-=1
                    if counter[nums[l]] == 0:
                        del counter[nums[l]]
                    l+=1
                res += r-l+1
            return res
        
        print(atMost(k), atMost(k-1))
        return atMost(k) - atMost(k-1)