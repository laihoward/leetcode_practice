class Solution(object):
    def rotate(self, nums, k):
        if not nums:
            return 
        k = k%len(nums) #處理k>len(nums)的情況
        nums[:] = nums[-k:]+nums[:-k] #使用nums[:]即可原地翻转
        print(nums)
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
s.rotate(nums,k)