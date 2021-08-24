class Solution(object):
    def minCostToMoveChips(self, position):
        odd =0
        even=0
        for i in position:
            if i %2==0:
                even+=1
            else:
                odd+=1
        res = min(odd,even)
        return res








position = [1,1000000000]
s=Solution()
print(s.minCostToMoveChips(position))