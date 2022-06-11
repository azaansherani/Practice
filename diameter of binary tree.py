class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    diameter = [0]
    helper(root,diameter)
    return diameter[0]
        
def helper(root,diameter):
    if root == None: return 0
    lh = helper(root.left, diameter)
    rh = helper(root.right, diameter)        
    diameter[0] = max(diameter[0],lh+rh)

    return (1 + max(lh,rh))

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
    print(diameterOfBinaryTree(root))