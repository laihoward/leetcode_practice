class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        res=0
        for i in range(0,len(nums),2) :
            res+=nums[i]
        print(res)
        return res


nums = [6,2,6,5,1,2]
s=Solution()
s.arrayPairSum(nums)