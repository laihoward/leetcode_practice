class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        l_len=self.maxlen(root.left)
        r_len=self.maxlen(root.right)
        if abs(l_len-r_len)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        

    def maxlen(self, root):
        if not root:
            return 0
        max_len=max(self.maxlen(root.left),self.maxlen(root.right))+1
        return max_len

