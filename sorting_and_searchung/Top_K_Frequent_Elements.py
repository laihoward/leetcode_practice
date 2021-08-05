


import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        count = collections.Counter(nums)
        res=[]
        ans = []
        for i in count.keys():
            heapq.heappush(res, (count[i], i))
            if len(res)>k:
                heapq.heappop(res)
        for i in range(k):
            ans.append(heapq.heappop(res)[1])
        return ans
        
            


nums=[1,1,1,2,2,3]
k = 2
s=Solution()
s.topKFrequent(nums, k)
x=[i for i in range(5)]
print(x)