#morris like , TC = O(N), SC = O(1)
def flatten(root) -> None:
    if root == None: return
    curr = root
    while curr:
        if curr.left:
            prev = curr.left
            while prev.right:
                prev = prev.right
            prev.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right

#go to the bottom for understanding


#recursive, go pura right last ko prev bnaao, then go left: TC = O(N), SC = O(N) 
def flatten(root) -> None:
    prev = None
    def helper(root):
        if root  == None: return
        
        helper(root.right)
        helper(root.left)
        
        root.right = prev
        root.left = None
        prev = root
        
    helper(root)



#iterative with stack, TC = O(N), SC = O(N)
def flatten(root) -> None:
    if root == None: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        if stack:
            node.right = stack[-1]
        node.left = None

#your solution
def flatten(root) -> None:
    ptr = dummy = TreeNode(0)
    if root == None: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            dummy.right = node
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
            dummy.left = None
        dummy = dummy.right

#morris for an idea
def flatten(root) -> None:
    if root == None: return
    curr = root
    while curr:
        if curr.left == None:
            curr = curr.right
        else:
            prev = curr.left
            while prev.right!=None and  prev.right!=curr:
                prev = prev.right
            
            if prev.right == None:
                prev.right = curr
                curr = curr.left
            
            else:
                prev.right = curr.right
                r = curr.right
                curr.right = curr.left
                curr.left = None
                curr = r