
class Solution(object):
    def calPoints(self, ops):
        count = -1
        recordlist = []
        for i in ops:
            x = i
            if x == "+":
                recordlist.append(recordlist[count]+recordlist[count-1])
                count+=1
            elif x == "D":
                recordlist.append(recordlist[count]*2)
                count+=1
            elif x == "C":
                recordlist.pop(-1)
                count-=1
            else:
                recordlist.append(int(i))
                count+=1
            print(recordlist)
        sumlist = 0
        for i in recordlist:
            sumlist += i
        print(sumlist)
        return sumlist
