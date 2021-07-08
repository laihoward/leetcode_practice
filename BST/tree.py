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
            return self.recur_find_parent_croot(croot, croot.left, key)
        elif croot.right and key > croot.key:
            return self.recur_find_parent_croot(croot, croot.right, key)
        else:
            return None, None
    
    def right_most_child(self, croot, crootleft):
        if crootleft.right:
            return self.right_most_child(crootleft, crootleft.right)
        else:
            return croot,crootleft
    
    def remove(self, key):
        if not self.root:
            return
        parent,croot = self.find_parent_croot(key)
        if not croot:
            return
        if croot.left and croot.right:
            self.two_child_remove(parent,croot)
        else:
            self.zero_one_child_remove(parent, croot)

    def two_child_remove(self, parent, croot):
        newparent,newcroot = self.right_most_child(croot,croot.left)#找出左樹最大的值
        croot.key = newcroot.key#替換值
        croot.value = newcroot.value
        self.zero_one_child_remove(newparent,newcroot) #將左樹最大的值刪除

    def zero_one_child_remove(self, parent, croot):
        if parent.left and parent.left.key == croot.key:
            if croot.left:
                parent.left = croot.left
            elif croot.right:
                parent.left = croot.right
            else:
                parent.left = None
        elif parent.right and parent.right.key == croot.key:
            if croot.left:
                parent.right = croot.left
            elif croot.right:
                parent.right = croot.right
            else:
                parent.right = None

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
    
    def print_paths(self):
        if not self.root:
            return
        s=''
        l=list()
        self.recur_print_paths(self.root,s,l)
        return l

    def recur_print_paths(self,croot, s,l):
        s=f'{s} {croot.key}'
        if not croot.left and not croot.right:
            l.append(s)
        if croot.left:
            self.recur_print_paths(croot.left,s,l)
        if croot.right:
            self.recur_print_paths(croot.right,s,l)