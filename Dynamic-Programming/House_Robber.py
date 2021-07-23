
#use recursive spend o(2^n)

class Solution(object):
    def rob(self, nums):
        if not nums :
            return 0
        return self.recur_rob(nums,len(nums)-1)
    def recur_rob(self,nums,i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0],nums[1])
        return max(self.recur_rob(nums,i-1),self.recur_rob(nums,i-2)+nums[i])

#use Dynamic Programming

class Solution(object):
    def rob(self, nums):
        l = len(nums)
        if not nums :
            return 0
        roblist=[0]*(l+1)
        roblist[1]=nums[0]
        for i in range(1,l-1):
            roblist[i+1]=max(roblist[i],roblist[i-1]+nums[i])
        return roblist[-1]

class Solution(object):
    def rob(self, nums):
        rob1, rob2 = 0, 0 
        
        for n in nums:
            temp = max(rob1 + n, rob2) 
            rob1 = rob2 
            rob2 = temp 
        return rob2 
            