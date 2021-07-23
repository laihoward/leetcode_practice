class Solution(object):
    def generate(self, numRows):
        res=[[1], [1, 1]]
        if numRows==1:
            return [res[0]]
        elif numRows==2:
            return res
        else:
            i=2
            while i <numRows:
                pre = res[-1]
                temp = [1]
                for j in range(1,len(pre)):
                    temp.append(pre[j-1]+pre[j])
                temp.append(1)
                res.append(temp)
                i+=1
        print(res)
        return res


numRows=1
s=Solution()
s.generate(numRows)