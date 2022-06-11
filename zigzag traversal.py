def zigzagLevelOrder(root):
    ans = []
    if root== None: return ans
    queue = [root]
    flag = 1
    while queue:
        size = len(queue)
        temp = []
        flag^=1
        for _ in range(size):
            node = queue.pop(0)
            temp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        if flag==0:
            ans.append(temp)
        else:
            ans.append(temp[::-1])
    return ans

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []
    if root== None: return ans
    queue = [root]
    flag = 0
    while queue:
        size = len(queue)
        temp = [0]*size
        for i in range(size):
            node = queue.pop(0)
            if flag==0:
                temp[i] = node.val
            else:
                temp[size-i-1] = node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        ans.append(temp)
        flag^=1
    return ans