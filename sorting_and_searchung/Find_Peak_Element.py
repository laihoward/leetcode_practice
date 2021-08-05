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
        return start


        

nums = [1,2,1,3,5,6,4]
s=Solution()
print(s.findPeakElement(nums))
