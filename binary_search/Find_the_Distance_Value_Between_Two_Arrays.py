class Solution(object):
    # def findTheDistanceValue(self, arr1, arr2, d):
    #     res = 0
    #     for i in arr1:
    #         temp = True
    #         for j in arr2:
    #             if abs(i-j) <= d:
    #                 temp=False
    #         if temp==True:
    #             res+=1
    #     print(res)
    #     return res

    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist


arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6
s=Solution()
print(s.findTheDistanceValue(arr1, arr2, d))