class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

from collections import defaultdict
def diagonalTraversal(root):
    res = defaultdict(list)
    def inorder(root,diag=1):
        if root == None: return 
        inorder(root.left,diag)
        res[diag].append(root.val)
        inorder(root.right,diag+1)
    inorder(root)
    
    r = []
    for key in res:
        r.append(res[key])
        
    return r

def solve(A):
        if A  == None: return []
        dct = defaultdict(list)
        
        def preorder(root, diag = 1):
            if root == None: return
            dct[diag].append(root.val)
            preorder(root.left, diag+1)
            preorder(root.right,diag)
        
        preorder(A)
        res = []
        for key in dct:
            res.append(dct[key])
        
        return res


    


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(11)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    print(diagonalTraversal(root))
    print(solve(root))