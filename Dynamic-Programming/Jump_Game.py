class Solution(object):
    def canJump(self, nums):
        res=0
        for index,val in enumerate(nums):
            if index>res:
                return False
            res = max(res,val+index)
        return True
nums=[1,1,2,2,0,1,1]
a=[2,3,1,1,4]
b=[3,2,1,0,4]
s=Solution()
print(s.canJump(nums))
print(s.canJump(a))
print(s.canJump(b))