class Solution(object):
    def generate(self, numRows):
        res=[]
        if numRows==1:
            res.append([1])
        if numRows==2:
            res.append([1])
            res.append([1,1])
        print(res)
        # pre = res[-1]
        # temp = [1]
        # temp.append()
