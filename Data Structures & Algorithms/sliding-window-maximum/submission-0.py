class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []

        for i in range(k):
            while queue and nums[i] > queue[-1][0]:
                queue.pop(-1)

            queue.append((nums[i], i))

        res = []
        for i in range(k,len(nums)):
            res.append(queue[0][0])

            if queue[0][1] == i-k:
                queue.pop(0)
            
            while queue and nums[i] > queue[-1][0]:
                queue.pop(-1)

            queue.append((nums[i], i))
            # print(nums[i])
        # print(queue)
        res.append(queue[0][0])
        return res