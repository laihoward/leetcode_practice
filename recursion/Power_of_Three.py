class Solution(object):
    def isPowerOfThree(self, n):
        print(n)
        if n==1:
            return True
        if n>=3:
            return self.isPowerOfThree(n/float(3))
        else:
            return False
        

n=9
s=Solution()
print(s.isPowerOfThree(n))