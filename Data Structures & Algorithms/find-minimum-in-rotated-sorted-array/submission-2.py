class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right) // 2 
            l, m, r = nums[left], nums[mid], nums[right]
            if m < r:
                right = mid
            else:
                left = mid + 1
        return nums[right]
                