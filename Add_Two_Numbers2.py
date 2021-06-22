
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 :
            return l2
        if not l2 :
            return l1   
        startNode = ListNode(-1)
        head = startNode
        carry = 0
        while l1 and l2:
            head.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)//10
            l1 = l1.next
            l2 = l2.next
            head = head.next
        
        while l1:
            head.next = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)//10
            l1 = l1.next
            head = head.next
        while l2:
            head.next = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)//10
            l2 = l2.next
            head = head.next


        if carry == 1:
            head.next = ListNode(1)
        return startNode.next
        

        


    
 
        