from collections import Counter 
class Solution(object):
    def firstUniqChar(self, s):
        count=Counter(s)
        for i,j in enumerate(s):
            if count[j] ==1:
                return i
        return -1
string = "leetcode"
s=Solution()
s.firstUniqChar(string)