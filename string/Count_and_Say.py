class Solution(object):
    def countAndSay(self, n):
        x="1"
        for i in range(n-1):
            l = len(x)
            s=''
            i=0
            count=1
            while i <l-1:
                if x[i]==x[i+1]:
                    count+=1
                else:
                    s+=str(count)
                    s+=x[i]
                    count=1
                i+=1
            s+=str(count)
            s+=x[i]
            x=s
        print(x)
        return x
    

n="1"
# n="1211"
n2=2
s1=Solution()
s1.countAndSay(7)