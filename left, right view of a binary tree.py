#iterative right view using Level Order
def rightView(self,root):
        ans = []
        if root== None: return ans
        queue = [root]
        
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i==0: ans.append(node.data)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            
        return ans

#Iterative left view using level order
def leftview(root):
    ans = []
    if root== None: return ans
    queue = [root]
    
    while queue:
        size = len(queue)
        temp = []
        for i in range(size):
            node = queue.pop(0)
            temp.append(node.data)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        ans.append(temp[0])
    return ans