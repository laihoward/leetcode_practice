class Solution(object):
    def removeDuplicates(self, nums):
        count =0
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
                i-=1
            i+=1
        count =  len(nums)
        print(nums)
        print(count)
        return count

    def removeDuplicates2(self, nums):
        count =0
        i = 0
        while i < len(nums):
            if nums[i]!=nums[count]:
                count+=1
                nums[count] = nums[i]
            i+=1
        count+=1
        print(nums)
        print(count)
        return count





s=Solution()
array = [1,1,2]
array2 = [0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(array)
s.removeDuplicates2(array2)
