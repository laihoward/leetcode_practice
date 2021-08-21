class Solution(object):
    def diStringMatch(self, s):
        start=0
        end=len(s)
        res=[]
        for i in s:
            if i =="I":
                res.append(start)
                start+=1
                
            else:
                res.append(end)
                end-=1
        if s[-1]=="I":
            res.append(start)
        else:
            res.append(end)
        print(res)
        return res




s = "DDI"
sol=Solution()
sol.diStringMatch(s)