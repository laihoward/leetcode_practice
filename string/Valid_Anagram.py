
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        countS = Counter(s)
        countT =Counter(t)
        if countS ==countT:
            return True
        else:
            return False



s = "anagram"
t = "nagaram"
s2 = "rat"
t2 = "car"
so=Solution()
print(so.isAnagram(s,t))
print(so.isAnagram(s2,t2))