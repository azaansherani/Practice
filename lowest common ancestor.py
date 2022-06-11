def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def pathToNode(node, b, arr):
        if node == None: return False
        arr.append(node)
        if node == b:
            return True
        
        if pathToNode(node.left, b, arr) or pathToNode(node.right, b, arr):
            return True
        
        arr.pop()
        return False
    arrp, arrq = [], []
    pathToNode(root, p, arrp)
    pathToNode(root, q, arrq)
    for i,j in zip(arrp,arrq):
        if i != j:
            break
        res = i
    return res

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root== None or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p ,q)
    right = self.lowestCommonAncestor(root.right, p ,q)
    
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root