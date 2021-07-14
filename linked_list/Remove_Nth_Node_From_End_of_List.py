
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 1
        countlen = 0
        printnode = head
        counthead =head
        while counthead:
            countlen+=1
            counthead=counthead.next
        print(countlen)
        if countlen == 1:
            head =None
            return head
        if countlen-n==0:
            head = head.next
            return head
        while count<countlen-n:
            count+=1
            head= head.next
        head.next = head.next.next
        return printnode
    