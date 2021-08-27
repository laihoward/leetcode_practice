#https://ithelp.ithome.com.tw/articles/10213282

class Solution(object):
    #use DFS
    def minDepth(self, root):
        if root is None:    
            return 0
        l_dep = self.minDepth(root.left)
        r_dep = self.minDepth(root.right)
        if l_dep ==0 or r_dep==0:
            return l_dep+r_dep+1
        else:
            return min(l_dep,r_dep)+1

    #use BFS
    def minDepth(self, root):
        if root is None:    
            return 0
        dep =0
        queue=[root]
        while len(queue) >0:
            
            dep+=1
            for i in range(0,len(queue)):
                res = queue.pop(0)
                if not res.left and not res.right:
                    return dep
                if res.left:
                    queue.append(res.left)
                if res.right:
                    queue.append(res.right)
                
        return dep