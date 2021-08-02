class Solution(object):
    def setZeroes(self, matrix):
        resrow = []
        rescol = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    resrow.append(i)
                    rescol.append(j)
        for i in resrow:
            for j in range(len(matrix[i])):
                matrix[i][j]=0
        for j in rescol:
            for i in range(len(matrix)):
                matrix[i][j]=0
        print(matrix)
        return matrix








matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s=Solution()
# s.setZeroes(matrix)
s.setZeroes(matrix2)