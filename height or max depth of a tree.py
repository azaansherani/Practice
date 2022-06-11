def maxDepth1(root):
    queue = [root]
    height = 0
    if root == None: return height
    while queue:
        size = len(queue)
        height+=1
        for _ in range(size):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return height
        
    
def maxDepth(root):
    if root == None: return 0
    leftheight = maxDepth(root.left)
    rightheight = maxDepth(root.right)

    return 1 + max(leftheight, rightheight)