class Solution(object):
    def searchRange(self, nums, target):
        res = set(nums)
        if target not in res:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        while start<=end:
            middle = (start+end)//2
            if nums[middle]<target:
                start = middle+1
            elif nums[middle]>target:
                end = middle-1
            else:
                start=end=middle
                while target==nums[start-1] and start>0:
                    start-=1
                while end<len(nums)-1 and target==nums[end+1] :
                    end+=1
                break
        return [start,end]
        

nums = [1]
target = 1
s=Solution()
print(s.searchRange(nums, target))
