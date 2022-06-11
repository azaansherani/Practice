class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    ans =  []
    if root == None: return ans
    node = root
    queue = [node]
    while queue:
        size = len(queue)
        temp = []
        for i in range(size):
            node = queue.pop(0)
            temp.append(node.val)
            if node.left!=None: queue.append(node.left)
            if node.right!=None: queue.append(node.right)
        ans.append(temp)
    return ans


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
    print(levelOrder(root))