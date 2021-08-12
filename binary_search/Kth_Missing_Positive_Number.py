class Solution(object):
    #O(n)
    def findKthPositive(self, arr, k):
        count=1
        res=1
        while count<=k :
            if res not in arr:
                count+=1
            res+=1
        res-=1
        print(res)
        return res
    #O(logn)
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr)
        while l<r:
            middle = (left+right) // 2
            if arr[middle]-(middle+1) < k:
                l=middle+1
            else:
                r=middle
        return left+k

arr = [1,2,3,4]
k = 2
s=Solution()
s.findKthPositive(arr,k)