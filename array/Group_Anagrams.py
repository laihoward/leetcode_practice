from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
        return res.values()
        








strs = ["eat","tea","tan","ate","nat","bat"]
s=Solution()
print(s.groupAnagrams(strs))