class Solution(object):
    def isPowerOfTwo(self, n):
        print(n)
        if n==1:
            return True
        if n>=2:
            return self.isPowerOfTwo(n/float(2))
        else:
            return False
        

n=17
s=Solution()
print(s.isPowerOfTwo(n))