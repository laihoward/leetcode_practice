class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return
        printlist = head 
        while head:
            if head.next and head.next.val == val:
                head.next = head.next.next
            elif head.val == val:
                printlist = printlist.next
                head=head.next
            else:
                head=head.next
        return printlist