# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        preNode = None
        curNode = head
        moveNode = curNode.next
        while moveNode is not None:
            curNode.next = preNode 
            preNode = curNode
            curNode = moveNode
            moveNode = moveNode.next
        curNode.next = preNode 
        return curNode


        """
        :type head: ListNode
        :rtype: ListNode
        """