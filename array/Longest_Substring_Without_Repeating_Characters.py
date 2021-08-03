class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s :
            return 0
        lpoint=0
        rpoint=0
        res = set()
        count=0
        slen = len(s)
        while lpoint<slen and  rpoint<slen:
            if s[rpoint] in res:
                if s[lpoint] in res:
                    res.remove(s[lpoint])
                lpoint+=1
            else:
                res.add(s[rpoint])
                rpoint+=1
                count=max(count,len(res))
        print(count)
        return count
s1 = ""
s=Solution()
s.lengthOfLongestSubstring(s1)