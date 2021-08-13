class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r=len(numbers)-1
        while l<r:
            res = numbers[l]+numbers[r]
            if res==target:
                return [l+1,r+1]
            elif res<target:
                l+=1
            else:
                r-=1
        






numbers = [3,24,50,79,88,150,345]
target = 200
s=Solution()
print(s.twoSum(numbers,target))