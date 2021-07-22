
class Solution(object):
    def isPalindrome(self, head):
        checkPalindrome = ""
        while head:
            addval = str(head.val)
            checkPalindrome = ''.join((checkPalindrome,addval))
            head = head.next
        
        reversed_string=''.join(reversed(checkPalindrome))
        
        if checkPalindrome==reversed_string:
            return True
        else:
            return False
    #時間O(n)空間O(n)
    def isPalindrome(self, head):
        checkPalindrome = []
        while head:
            checkPalindrome.append(head.val)
            head = head.next 
        l = len(checkPalindrome)
        print(l//2)
        for i in range(0,l//2):
            if checkPalindrome[i]!=checkPalindrome[l-1-i]:
                return False
        return True
    
    #時間O(n)空間O(1)
    def isPalindrome(self, head):
    #快慢指針法找中點
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow=slow.next
            head = head.next
        return True


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