class Solution(object):
    def isPerfectSquare(self, num):
        l=0
        r=num
        while l<=r:
            mid=(l+r)//2
            res = mid*mid
            if res==num:
                return True
            elif res>num:
                r=mid-1
            else:
                l=mid+1
        return False
        




num = 48
s=Solution()
print(s.isPerfectSquare(num))