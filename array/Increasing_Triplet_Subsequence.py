class Solution(object):
    #O(n^3) 
    def increasingTriplet(self, nums):
        x=set(nums)
        if len(x)<3:
            return False
        l = len(nums)
        for start in range(1,l-1):
            left = start-1
            right =start+1
            while left >=0 and right<=l-1:
                if nums[left]<nums[start]<nums[right]:
                    return True
                if nums[start]<=nums[left]:
                    left-=1
                if nums[start]>=nums[right]:
                    right+=1
        return False










        
nums = [2,5,3,4,5]
s=Solution()
print(s.increasingTriplet(nums))