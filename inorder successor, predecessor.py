def inorderSuccessor(self, root, p):
    if root == None: return
 
    if root.val <= p.val:
        return self.inorderSuccessor(root.right, p)
 
    else: #root.val>p
        return self.inorderSuccessor(root.left, p) or root

def inorderPredecessor(self, root, p):
    if root == None: return
 
    if root.val >= p.val:
        return self.inorderPredecessor(root.left, p)
    
    else:
        return self.inorderPredecessor(root.right, p) or root