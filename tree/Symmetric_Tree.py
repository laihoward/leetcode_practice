class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        
        return self.isSame(root.left, root.right)
            
        
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left = self.isSame(p.left, q.right)
        right = self.isSame(p.right, q.left)
        return (left and right)