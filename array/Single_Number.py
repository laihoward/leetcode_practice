from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        count = Counter(nums)
        for n in count:
            if count[n]==1:
                return n


    def singleNumber2(self, nums):
        res=0
        for num in nums:
            res^=num
            print(res)
        return res

s=Solution()
nums =[4,1,2,1,2]

print(s.singleNumber2(nums))