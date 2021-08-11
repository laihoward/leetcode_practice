
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if not root or not root.left :
            return root
        queue = [root.left,root.right]
        levellen = len(queue)
        count =0
        while len(queue)>0:
            curnode = queue.pop(0)
            count+=1
            if curnode.left:
                queue.append(curnode.left)
                queue.append(curnode.right)
            if count ==1:
                head = curnode
            else:
                head.next = curnode
                head = head.next
            if levellen == count:
                count=0
                levellen*=2
        return root


        

        