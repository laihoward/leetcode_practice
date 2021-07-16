
class Solution(object):
#use recursion  
# O(2的n次方)
    def fib(self, n):
        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
# use Dynamic Programming
#O(n)
    def fib_dy(self, n):
        fib_list=[0]*n
        fib_list[0]=1
        fib_list[1]=1
        for i in range(2,n):
            fib_list[i] = fib_list[i-1]+fib_list[i-2]
        print(fib_list)
s=Solution()
s.fib_dy(7)