from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        count = Counter(nums)
        for n in count:
            print(count[n])
            if count[n]>=2:
                return True
            else:
                return False
            
    def containsDuplicate(self, nums):
        if len(set(nums))!=len(nums) :
            return True
        else:
            return False
        
s=Solution()
nums =[1,2,3,1]
print(s.containsDuplicate(nums))