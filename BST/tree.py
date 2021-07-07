import math
from typing import Coroutine
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
    
    def find_parent_croot(self, key):
        if not self.root:
            print("No data")
        else:
            return self.recur_find_parent_croot(self.root, self.root, key)
    
    def recur_find_parent_croot(self, parent, croot, key):
        if croot.key == key: #包含root.key == key 和base case
            return parent,croot
        elif croot.left and key < croot.key:
            return self.recur_find_parent_croot(parent, croot.left, key)
        elif croot.right and key > croot.key:
            return self.recur_find_parent_croot(parent, croot.right, key)
    
    def right_most_child(self, parent, croot):
        if croot.right:
            return self.right_most_child(croot, croot.right)
        else:
            return parent,croot

    def in_order(self):
        res = list()
        return self.recur_in_order(self.root,res)
    
    def recur_in_order(self, croot, res):
        if not croot:
            return
        else:
            self.recur_in_order(croot.left,res)
            res.append(croot.key)
            self.recur_in_order(croot.right,res)
        return res

    def pre_order(self):
        res = list()
        return self.recur_pre_order(self.root,res)

    def recur_pre_order(self, croot, res):
        if not croot:
            return
        else:
            res.append(croot.key)
            self.recur_pre_order(croot.left,res)
            self.recur_pre_order(croot.right,res)
        return res

    def level_order(self):
        queue = [self.root]
        res = list()
        while len(queue)>0:
            cur = queue[0]
            res.append(cur.key)
            queue = queue[1:]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res

    def height(self):
        if not self.root:
            return -1
        else:
            return self.recur_height(self.root,-1)
    
    def recur_height(self, croot,chight):
        if not croot:
            return chight
        leftheight =  self.recur_height(croot.left,chight+1)
        rightheight = self.recur_height(croot.right,chight+1)
        return max(leftheight,rightheight)
    
    