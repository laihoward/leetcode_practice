
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        res =self.recurinorder(root,res)
        print(res)
        return res[k-1]
        

        


    def recurinorder(self,root,res):
        if root.left:
            self.recurinorder(root.left,res)
        res.append(root.val)    
        if root.right:
            self.recurinorder(root.right,res)
        return res
        