class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        while k>0:
            nums.sort()
            if nums[0]<0:
                k-=1
                nums[0]*=-1
            elif nums[0]==0 :
                k=0
            else:
                if k%2==0:
                    k=0 
                else:
                    nums[0]*=-1
                    k=0
        print(nums)
        return sum(nums)







nums = [2,-3,-1,5,-4]
k = 2
s=Solution()
print(s.largestSumAfterKNegations(nums,k))