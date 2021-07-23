class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        l=list()
        s=0
        self.rec_maxDepth(root,l,s)
        maxpath = max(l)
        return maxpath
        
    def rec_maxDepth(self,root,l,s):
        s+=1
        if not root.left and not root.right:
            l.append(s)
        if root.left:
            self.rec_maxDepth(root.left,l,s)
        if root.right:
            self.rec_maxDepth(root.right,l,s)


#法2
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        max_depth = max(left_depth, right_depth) + 1
        return max_depth
       