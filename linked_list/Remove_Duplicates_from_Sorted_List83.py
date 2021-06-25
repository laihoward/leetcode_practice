class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return
        moveNode = head
        while moveNode:
            if moveNode.next and moveNode.val == moveNode.next.val:
               moveNode.next = moveNode.next.next
            else:
                moveNode =moveNode.next
        return head