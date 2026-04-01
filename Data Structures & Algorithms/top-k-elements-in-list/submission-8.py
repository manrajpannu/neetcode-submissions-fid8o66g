class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = 1 + hash.get(i,0)
        print(hash)

        kfreq = {}

        for key in hash.keys():
            val = hash[key]
            kfreq[val] = kfreq.get(val,[]) + [key]

        print(kfreq)

        count = 0
        i = len(nums)
        res = []
        while count < k or i > 0:
            if i in kfreq:
                res+=kfreq[i]
                count+=len(kfreq[i])
            i-=1
        
        return res[0:k]
            