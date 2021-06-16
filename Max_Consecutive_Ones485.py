class Solution(object):
    def __init__(self,count = 0,anser = 0):
        self.count = count
        self.nums = []
        self.anser = anser
    def findMaxConsecutiveOnes(self, nums):
        for i in range(len(nums)):
            if nums[i]==1:
                self.count += 1
            else:
                self.count = 0
            i+=1
            if self.count>self.anser:
                print("ok")
                self.anser = self.count
        print(self.anser)

def main():
    s=Solution()
    array = [1,1,0,1,1,1]
    array2 = [1,0,1,1,0,1]
    s.findMaxConsecutiveOnes(array2)
    s.findMaxConsecutiveOnes(array)
    s.findMaxConsecutiveOnes(array2)
if __name__ == '__main__':
    main()