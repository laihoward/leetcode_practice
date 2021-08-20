class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed)==1:
            if flowerbed[0]==0 and n<=1:
                return True                
            elif n==0:
                return True
            else:
                return False
        res=0
        mark_1=0
        temp = 0
        for i in range(len(flowerbed)):
            if mark_1==0:
                if flowerbed[i]==1:
                    mark_1=1
                    if temp>=2:
                        x = temp//2
                        res+=x
                    temp = 0
                else:
                    temp +=1
            else:
                if flowerbed[i]==1:
                    if temp>=3:
                        x = (temp-1)//2
                        res+=x
                    temp = 0
                else:
                    temp +=1
        if mark_1==0:
            if temp>=1:
                x = (temp+1)//2
                res+=x
        else:
            if temp>=2:
                x = temp//2
                res+=x
        print(res)
        if n>res:
            return False
        else:
            return True


    def canPlaceFlowers(self, A, n):
        count = 0
        A = [0] + A + [0]
        for i in range(1, len(A)-1):
            if A[i]==1:
                continue   
            if A[i - 1] != 1 and A[i + 1] != 1:
                A[i] = 1
                count += 1
        return count >= n
                     

flowerbed = [1,0,0,0,1,0,0]
n = 2
s=Solution()
print(s.canPlaceFlowers(flowerbed,n))