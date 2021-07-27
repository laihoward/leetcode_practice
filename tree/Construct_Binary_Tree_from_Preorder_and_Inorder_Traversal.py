class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootindex+1],inorder[:rootindex])
        root.right = self.buildTree(preorder[rootindex+1:],inorder[rootindex+1:])
        return root