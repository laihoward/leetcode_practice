class Solution(object):
    def climbStairs(self, n):
        fib_list=[1,2]
        if n<=2:
            return fib_list[n-1]
        for i in range(n-2):
            fib_list.append(fib_list[-1]+fib_list[-2])
        print(fib_list)
        return fib_list[-1]
        
        