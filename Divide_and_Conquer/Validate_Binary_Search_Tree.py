
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.last = None
    
    def isValidBST(self, root):
        if root:
            if root.left and root.val <= root.left.val:
                return False
            elif root.right and root.val >= root.right.val:
                return False
            elif root.left and root.val > root.left.val:
                return self.isValidBST(root.left)
            elif root.right and root.val < root.right.val:
                return self.isValidBST(root.right)
            
            else:
                return True

        else:
            return True
                
        
