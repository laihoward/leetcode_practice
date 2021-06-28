class Solution(object):
    def sortColors(self, nums):
        i=0
        j=0
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[j]>=nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums

        