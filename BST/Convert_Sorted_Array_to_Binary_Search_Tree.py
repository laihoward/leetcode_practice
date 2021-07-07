class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        middleindex = len(nums)//2
        root = TreeNode(nums[middleindex])
        printroot = root
        nums.pop(middleindex)
        for i in nums:
            self.insert(root,i)
        return printroot

    def insert(self,croot,val):
        if not croot:
            croot = TreeNode(val)
        elif val<croot.val:   
            croot.left = self.insert(croot.left,val)
        else:
            croot.right = self.insert(croot.right,val)
        return croot

        """
        :type nums: List[int]
        :rtype: TreeNode
        """
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        middleindex = len(nums)//2
        root = TreeNode(nums[middleindex])
        root.left = self.sortedArrayToBST(nums[:middleindex])
        root.right = self.sortedArrayToBST(nums[middleindex+1:])
        return root
        