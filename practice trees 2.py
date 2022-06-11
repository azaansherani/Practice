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


def preorder(node,res):
    if node == None: return
    res.append(node.val)
    preorder(node.left,res)
    preorder(node.right,res)

def postorder(node,res): #left, right, root
    if node == None: return

    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.val)

def inorderIterative(node):
    stack = []
    ans = []

    while True:
        if node:
            stack.append(node)
            node = node.left        
        else:
            if not stack:
                break
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans

def preorderIterative(root):
    if root == None: return[]
    stack = [root]
    preorder = []
    while stack:
        node = stack.pop()
        preorder.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return preorder   

def postorderIterative(root): #left, right, root
    ans = []
    if root == None: return ans
    stack = [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return ans[::-1]




def inOrderMorris(root):
    traversal = []
    curr = root
    
    while curr:
        if curr.left == None:
            traversal.append(curr.val)
            curr = curr.right

        else:
            prev = curr.left
            while prev.right != None and prev.right!=curr:
                prev = prev.right
            
            if prev.right == None:
                prev.right = curr
                curr = curr.left

            else:
                prev.right == None
                traversal.append(curr.val)
                curr = curr.right
    return traversal       


def preOrderMorris(root):
    traversal = []
    curr = root
    
    while curr:
        if curr.left == None:
            traversal.append(curr.val)
            curr = curr.right

        else:
            prev = curr.left
            while prev.right != None and prev.right!=curr:
                prev = prev.right
            
            if prev.right == None:
                prev.right = curr
                traversal.append(curr.val)
                curr = curr.left

            else:
                prev.right == None
                curr = curr.right
    return traversal   

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
    res = []
    preorder(root,res)
    print("Preorder",res)
    res = []
    postorder(root,res)
    print("Postorder",res)
    print("Level Order Traversal: ", levelOrder(root))


    print('Iterative In order :',inorderIterative(root))

    print("Iterative Pre Order :", preorderIterative(root))

    print("Iterative Post Order :", postorderIterative(root))

    print("Morris In Order: ", inOrderMorris(root))

