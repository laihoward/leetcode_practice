class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return 
        if len(nums)==1:
            return nums
        count =0
        i=0
        while i<len(nums):
            if nums[i]==0:
                count+=1
                nums.pop(i)              
            else:
                i+=1
            
        for i in range(count):
            nums.append(0)
        print(nums)
        return nums


arr =[0]
array = [0,1,0,3,12]  
s =Solution()
s.moveZeroes(arr)