
class Solution(object):
    def majorityElement(self, nums):
        res=nums[0]
        count =1
        l = len(nums)
        for i in range(1,l):
            if nums[i]==res:
                count+=1
            elif count>0:
                count-=1
            else:
                res = nums[i]
        return res


    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        