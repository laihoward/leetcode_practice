# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        printNode = head
        startNode = printNode.next #return 要用

        while (True): 
            Endswap = printNode.next
            temp = Endswap.next

            Endswap.next = printNode
            if not temp or not temp.next:
                printNode.next = temp
                break
            printNode.next = temp.next #連1->4
            printNode = temp
 
            
        return startNode

        

        """
        :type head: ListNode
        :rtype: ListNode
        """