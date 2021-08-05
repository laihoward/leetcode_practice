#use Binary Search
class Solution(object):
    def findPeakElement(self, nums):
        start = 0
        end=len(nums)-1
        while start<end:
            middleL=(start+end) // 2
            middleR=middleL+1
            if nums[middleL]<nums[middleR]:
                start=middleR
            else:
                end=middleL
        return middleL

    def findPeakElement2(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left

        

nums = [1,2,1,3,5,6,4]
s=Solution()
print(s.findPeakElement(nums))
print(s.findPeakElement2(nums))