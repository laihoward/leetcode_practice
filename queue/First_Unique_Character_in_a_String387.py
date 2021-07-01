from typing import Collection



class Solution(object):
    def firstUniqChar(self, s):
        count = collections.Counter(s)
        for i,j in enumerate(s):
            if count[j] == 1:
                return i
        return -1
