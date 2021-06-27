
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