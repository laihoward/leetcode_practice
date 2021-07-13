class Solution(object):
    def reverse(self, x):
        x=str(x)
        if x[0]=="-":
            y = x[1:]
            y=''.join(reversed(y))
            x="-"+y
        else:
            x=str(x)
            x=''.join(reversed(x))
        x=int(x)
        if -2**31>x or x>2**31:
            x = 0
        return x  
        
        

x = 1534236469

so=Solution()
print(so.reverse(x))