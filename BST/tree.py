import math
class TreeNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
 
class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self.recur_insert(self.root, key, value)
        return self.root
    
    def recur_insert(self, croot, key, value):
        if not croot:
            croot = TreeNode(key, value)
        elif key < croot.key:
            croot.left = self.recur_insert(croot.left, key, value)
        elif key > croot.key:
            croot.right = self.recur_insert(croot.right, key, value)
        return croot

    def find(self, key):
        if not self.root:
            print("No data")
        else:
            return self.recur_find(self.root, key)

    def recur_find(self, croot, key):
        if croot.key == key:
            return croot
        elif croot.left and key < croot.key:
            return self.recur_find(croot.left, key)
        elif croot.right and key > croot.key:
            return self.recur_find(croot.right, key)

    
    