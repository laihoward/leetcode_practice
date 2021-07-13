class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        print(s)
        return s
    
    def reverseString2(self, s):
        s[:] = s[::-1]
        return s
s = ["h","e","l","l","o"]
so=Solution()
so.reverseString(s)