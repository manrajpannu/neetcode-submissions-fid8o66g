class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        p = []
        s = []
        a = 1
        b = 1


        for i in range(len(nums)):
            a = nums[i] * a
            b = nums[len(nums)-1-i] * b
            p.append(a)
            s.insert(0,b)



        res = []
        for i in range(len(nums)):
            if 0 <= i - 1 <= len(nums) - 1:
                x = p[i - 1]
            else:
                x = 1

            if 0 <= i + 1 <= len(nums) - 1:
                y = s[i + 1]
            else:
                y = 1
            print(x,y)
            res.append(x*y)

        
        return res