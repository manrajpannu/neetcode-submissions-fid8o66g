class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right) // 2 
            # print(nums[left:right])
            # print(nums[left],nums[mid], nums[right])
            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[left] > nums[mid] < nums[right]:
                if nums[left] > nums[right]:
                    right = mid
                    left+=1
                else:
                    left = mid
                    right+=1
                
            else:
                if nums[left] > nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        
        print(left, right)

        return nums[left]
                