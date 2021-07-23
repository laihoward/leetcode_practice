class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        res = nums[0]
        moveres = nums[0]
        for i in range(1,len(nums)):
            if moveres>0:
                moveres=moveres+nums[i]
            else:
                moveres=nums[i]
            if moveres>res:
                res = moveres
        return res