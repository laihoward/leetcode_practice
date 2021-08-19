from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        res = 0
        even = 0
        for i in count:
            if count[i]%2==0:
                res+=count[i]
            else:
                even=1
                res+=count[i]-1
        res+=even
        print(res)
        return res


            
        




s = "AaBBBb"
sol=Solution()
sol.longestPalindrome(s)