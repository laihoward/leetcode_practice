class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = [root]
        printqueue=[root]
        res = []
        count=0
        while queue:
            size = len(queue)
            tmp = []
            if count%2==0:
                print(1)
                while size>0:
                    cur = queue[0]
                    printcur=printqueue[0]
                    queue =queue[1:]
                    printqueue = printqueue[1:]
                    tmp.append(cur.val)
                    if printcur.right:
                        queue.append(printcur.right)
                    if printcur.left:
                        queue.append(printcur.left)
                    if cur.left:
                        printqueue.append(cur.left)
                    if cur.right:
                        printqueue.append(cur.right)
                    size-=1
                count+=1
            elif count%2==1:
                print(2)
                while size>0:
                    cur = queue[0]
                    printcur=printqueue[0]
                    queue =queue[1:]
                    printqueue = printqueue[1:]
                    tmp.append(cur.val)
                    if printcur.left:
                        queue.append(printcur.left)
                    if printcur.right:
                        queue.append(printcur.right)
                    if cur.right:
                        printqueue.append(cur.right)
                    if cur.left:
                        printqueue.append(cur.left)
                    size-=1
                count+=1
            res.append(tmp) 
        return res

        
