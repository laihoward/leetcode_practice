class Solution(object):
    def removeDuplicates(self, s):
        printS=[]
        i = 0
        while i < len(s):
            if len(printS)!=0 and printS[-1]==s[i]:
                i+=1
                printS.pop(-1)
            else:
                printS.append(s[i])
                i+=1     
        return "".join(printS)

    def removeDuplicates(self, s):
        printS=[]
        for i in s:
            if printS and printS[-1]==i:
                printS.pop()
            else:
                printS.append(i)
                   
        return "".join(printS)