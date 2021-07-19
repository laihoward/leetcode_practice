#O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return 
        targetlist=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    targetlist = [i,j]
                    print(targetlist)
                    return targetlist
    
#use dictionary O(n)
    def twoSum2(self, nums, target):
        if not nums:
            return 
        map ={}
        for i in range(len(nums)):
            print(map)
            sumnum = target - nums[i]
            if sumnum in map:
                return (map[sumnum], i)
            map[nums[i]] = i
            

nums = [2,7,11,15]
target = 26
s=Solution()
s.twoSum2(nums,target)