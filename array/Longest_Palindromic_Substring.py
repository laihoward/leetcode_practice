class Solution(object):
    def longestPalindrome(self, s):
        res=""
        def moveLR(s,start,end):
            while start>=0 and end<len(s) and s[start]==s[end]:
                start-=1
                end+=1
            return s[start+1:end]
        for i in range(len(s)):
            step1 = moveLR(s,i,i)
            print(step1)
            if len(step1) >len(res):
                res = step1
                
            step2 = moveLR(s,i,i+1)
            print(step2)
            if len(step2) >len(res):
                res = step2     
                
        return res

        

s1 = "babad"
s=Solution()
s.longestPalindrome(s1)