
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    #space complexity O(n) and time complexity O(n) .
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        count = 1
        oddhead = ListNode(head.val)
        x = oddhead
        evenhead = ListNode(head.next.val)
        y = evenhead
        head = head.next.next
        while head:
            if count%2==1:
                oddhead.next = ListNode(head.val)
                oddhead = oddhead.next
            else:
                evenhead.next = ListNode(head.val)
                evenhead = evenhead.next
            head=head.next
            count+=1
        oddhead.next = y
        return x
    