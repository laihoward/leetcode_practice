class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        x=nums.index(target)
        return x


    def search(self, nums, target):
        left = 0
        right=len(nums)-1
        while left<=right:
            middle =(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[left]<=nums[middle]<target or target<nums[left]<=nums[middle] or nums[middle]<target<=nums[left]:
                left=middle+1
            else:
                right=middle-1
        return -1



nums=[4,5,6,7,0,1,2]
target  = 0
s=Solution()
print(s.search(nums, target))