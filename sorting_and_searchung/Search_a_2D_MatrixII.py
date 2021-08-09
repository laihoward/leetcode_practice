class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            l = 0
            r= len(matrix[i])-1
            while l<=r:
                middle = (l+r)//2    
                if matrix[i][middle]==target:
                    return True
                elif matrix[i][middle]<target:
                    l=middle+1
                else:
                    r=middle-1
        return False





matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
s=Solution()
print(s.searchMatrix(matrix,target))