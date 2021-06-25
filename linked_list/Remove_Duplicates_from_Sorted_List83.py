class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return
        printlist = head
        while head:
            if head.val == head.next.val:
                head.next = head.next.next
            head =head.next
        return printlist