class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        print(nums[-k])
        return nums[-k]









nums=[3,2,3,1,2,4,5,5,6]
k = 4
s=Solution()
s.findKthLargest(nums, k)
