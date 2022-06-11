class TreeNode :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

def allThreeTraversal(root):
    # Write your code here.
    stack = [(root,1)]
    if root == None: return [],[],[]
    preorder, inorder, postorder = [], [], []
    while stack:
        node, num = stack.pop()
        if num==1:
            preorder.append(node.val)
            stack.append((node,num+1))
            if node.left: stack.append((node.left,1))
                
        elif num == 2:
            inorder.append(node.val)
            stack.append((node,num+1))
            if node.right: stack.append((node.right,1))
        else:
            postorder.append(node.val)

    print("Preorder :", preorder)            
    print("Inorder :", inorder)
    print("Postorder :", postorder)

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

    allThreeTraversal(root)