class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        # smallest to largest
        # n-1 is going to be the biggest, n-2 -> 2nd biggest
        # approach 1: sort, then return nums[n-k]  nlogn
        # max heap of size k O(nlogk)
        # quick select o(n) avg


        lb, rb = 0, n-1

        while lb <= rb:
            l, r = lb, rb-1
            p = rb
            while l <= r:
                while l <= r and nums[l] <= nums[p]: # skip smaller stuff on left side
                    l+=1

                while l <= r and nums[r] > nums[p]: # skip higher stuff on right side
                    r-=1
                
                print(l,r)
                if l <= r: # if in a valid part, swap!, then increment
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
            
            print(nums)
            p, l = l, p
            nums[p], nums[l] = nums[l], nums[p]
            print(nums)
            if p == n-k:
                return nums[p]
            elif p > n-k:
                rb = p - 1
            else:
                lb = p + 1

            
        print(nums)
            
