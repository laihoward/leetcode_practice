import math

class Solution():
    def __init__(self,digitsnums = 0,count = 0):
        self.digitsnums = digitsnums
        self.count = count

    def findNumbers(self, nums):
        self.count = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                self.digitsnums = int(math.log10(nums[i]))+1
            elif nums[i] == 0:
                self.digitsnums = 1
            if (self.digitsnums%2) == 0 :
                self.count +=1
            i +=1
        print(self.count)
        return self.count



def main():
    s=Solution()
    array = [12,345,2,6,7896]
    array2 = [555,901,482,1771]
    s.findNumbers(array)
    s.findNumbers(array2)
if __name__ == '__main__':
    main()