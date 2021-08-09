class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        x=nums.index(target)
        return x






nums=[1]
target  = 1
s=Solution()
print(s.search(nums, target))