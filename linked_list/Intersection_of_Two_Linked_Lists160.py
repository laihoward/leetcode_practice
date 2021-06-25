class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA:
            return None
        if not headB:
            return None
        moveA = headA
        moveB = headB
        while moveA and moveB and moveA!=moveB:
            moveA = moveA.next
            moveB = moveB.next
            if moveA == moveB:
                return moveA
            if not moveA:
                moveA = headB
            if not moveB:
                moveB = headA
        return moveA
        
            


        