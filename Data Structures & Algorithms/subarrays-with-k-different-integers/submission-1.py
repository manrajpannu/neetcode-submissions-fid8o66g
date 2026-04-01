from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      
        counter = defaultdict(int)
        res = 0
        far = 0
        close = 0
        for r in range(len(nums)):
            counter[nums[r]]+=1
            while len(counter) > k: # shrink both far and close
                counter[nums[close]]-=1
                if counter[nums[close]] == 0:
                    del counter[nums[close]]
                close+=1
                far = close

            while counter[nums[close]] > 1: # shrink close as much as possible
                counter[nums[close]] -= 1
                close+=1
            

            
            if len(counter) == k:
                print(far, close, r)
                print(close-far+1)
                print()
                res += close-far+1
        
        return res
        