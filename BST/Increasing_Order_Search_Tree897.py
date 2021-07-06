
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        res = self.in_order(root)
        newroot = TreeNode(res[0])
        moveroot = newroot
        for i in range(1,len(res)):
            moveroot.right = TreeNode(res[i])
            moveroot = moveroot.right
        return newroot
         
        

    def in_order(self, root):
        res = list()
        return self.recur_in_order(root,res)
    
    def recur_in_order(self, croot, res):
        if not croot:
            return
        else:
            self.recur_in_order(croot.left,res)
            res.append(croot.val)
            self.recur_in_order(croot.right,res)
        return res

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        