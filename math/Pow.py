class Solution(object):
    def myPow(self, x, n):
        res = x
        if n>0:
            for i in range(1,n):
                res =res*x
        elif n<0:
            for i in range(1,-n):
                res =res*x
            res=1/res
        else:
            return 1
        print(res)
        return res



x=2
n=-2
s=Solution()
s.myPow(x,n)