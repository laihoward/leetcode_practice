
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        point_g=0
        point_s=0
        while point_g<len(g) and point_s<len(s):
            if s[point_s]>=g[point_g]:
                point_s+=1
                point_g+=1
            else:
                point_s+=1
        print(point_g)
        return point_g


g = [1,2,3]
s = [1,1]
sol=Solution()
sol.findContentChildren(g,s)
        