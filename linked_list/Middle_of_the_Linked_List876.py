class Solution(object):
    def middleNode(self, head):
        listlen =0
        countlen = head
        while countlen:
            countlen = countlen.next
            listlen+=1
        middlepoint = listlen/2
        for i in range(middlepoint):
            head = head.next
        return head
        
        