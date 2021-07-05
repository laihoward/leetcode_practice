class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return []
        else:
            return self.recsearchBST(root, val)
    

    def recsearchBST(self, root, val):
        if root.val == val:
            return root
        elif root.left and val<root.val:
            return self.recsearchBST(root.left, val)
        elif root.right and val>root.val:
            return self.recsearchBST(root.right, val)
