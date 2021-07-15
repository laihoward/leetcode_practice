
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            tmp = []
            while size>0:
                cur = queue[0]
                queue =queue[1:]
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size-=1
            res.append(tmp) 
        return res

        
