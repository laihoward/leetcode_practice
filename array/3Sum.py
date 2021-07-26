
class Solution(object):
    def threeSum(self, nums):
        l = len(nums)
        if l<3:
            return []
        nums.sort()
        res=[]
        
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k=l-1
            while j<k:
                sum3=nums[i]+nums[j]+nums[k]
                if sum3==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sum3<0:
                    j+=1
                else:
                    k-=1
                
        print(res)
        return res

nums = [-1,0,1,2,-1,-4]
s=Solution()
s.threeSum(nums)