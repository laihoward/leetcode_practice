class Solution(object):
    def sortArray(self, nums):
        if len(nums)>1:
            r = len(nums)
            middleP = 1+(r-1)//2
            arrayL = nums[:middleP]
            arrayR = nums[middleP:]
            self.sortArray(arrayL)
            self.sortArray(arrayR)


            i=j=k = 0
            while i<len(arrayL) and j<len(arrayR):
                if arrayL[i]<=arrayR[j]:
                    nums[k]=arrayL[i]
                    i+=1
                else:
                    nums[k]=arrayR[j]
                    j+=1
                k+=1

            while i<len(arrayL):
                nums[k]=arrayL[i]
                i+=1
                k +=1

            while j<len(arrayR):
                nums[k]=arrayR[j]
                j+=1
                k +=1
        return nums