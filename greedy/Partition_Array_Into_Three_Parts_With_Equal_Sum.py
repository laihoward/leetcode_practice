class Solution(object):
    def canThreePartsEqualSum(self, arr):
        res=sum(arr)
        temp = 0
        count=0
        if res%3 !=0:
            return False
        else:
            target = res//3 
        for i in range(len(arr)):
            temp+=arr[i]
            if temp == target and count<=1:
                count+=1
                temp=0
                if i==len(arr)-1 and count<=2:
                    return False
        if temp == target :
            return True
        else:
            return False




arr = [1,-1,1,-1]
s=Solution()

print(s.canThreePartsEqualSum(arr))