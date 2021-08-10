import bisect
class Solution(object):
    #Time complexity O(n^2) Space complexity O(n)
    def lengthOfLIS(self, nums):
        res = []
        res.append(1)
        
        for i in range(1,len(nums)):
            maxs = 1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    maxs = max(maxs,res[j]+1) 
            res.append(maxs)
        return max(res)

    #use dp+greedy+binary search
    #Time complexity O(nlogn) Space complexity O(n)
    def lengthOfLIS2(self, nums):
        res =[]
        for i in nums:
            index = bisect.bisect_left(res,i)
            if index == len(res):
                res.append(i)
            else:
                res[index]=i
        return len(res)
    


nums = [3,4,1,2,8,5,6]
s=Solution()
s.lengthOfLIS2(nums)

