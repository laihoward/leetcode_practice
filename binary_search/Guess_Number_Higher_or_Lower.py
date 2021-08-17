class Solution(object):
    def guessNumber(self, n):
        l=0
        r=n
        while l<=r:
            mid=(l+r)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res ==-1:
                r=mid-1
            else:
                l=mid+1
        


