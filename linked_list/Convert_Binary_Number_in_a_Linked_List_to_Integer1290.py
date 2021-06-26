
class Solution(object):
    def getDecimalValue(self, head):
        maxpower =-1
        countPower = head
        while countPower:
            countPower = countPower.next
            maxpower+=1
        sumBase2 = 0
        while head:
            if head.val == 1:
                sumBase2+=2**maxpower
            head = head.next
            maxpower-=1
