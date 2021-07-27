class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res=[]
        return self.recur_inorder(root,res)
    
    def recur_inorder(self, root,res):
        if not root:
            return
        else:
            self.recur_inorder(root.left,res)
            res.append(root.val)
            self.recur_inorder(root.right,res)
        return res
        