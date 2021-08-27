class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return True
        l=[]
        s=0
        self.dfs(root,l,s)
        if targetSum not in l:
            return False
        else:
            return True
        
    def dfs(self,root,l,s):
        s+=root.val
        if not root.left and not root.right:
            l.append(s)
        if root.left:
            self.dfs(root.left,l,s)
        if root.right:
            self.dfs(root.right,l,s)
        