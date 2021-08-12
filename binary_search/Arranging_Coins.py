class Solution(object):
    #O(n)
    def arrangeCoins1(self, n):
        i=0
        res = 0
        while res<=n:
            i+=1
            res+=i 
        return i-1
    #O(logn)
    #1+2+3+....+n=n(n+1)/2
    def arrangeCoins(self, n):
        l = 0
        r=n
        while l<=r:
            mid=(l+r)//2
            if mid*(mid+1)==2*n:
                return mid
            elif mid*(mid+1)>2*n:
                r=mid-1
            else:
                l=mid+1
        return r





n=1
s=Solution()
print(s.arrangeCoins(n))