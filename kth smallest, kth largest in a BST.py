def kthSmallest(self, root, k: int) -> int:
    self.k1 = 0
    def inorder(root):
        if root == None: return
        l = inorder(root.left)
        if l: return l
        self.k1+=1
        if self.k1 == k:
            return root
        r = inorder(root.right)
        if r: return r

    return inorder(root).val


def kthLargest(self,root, k):
    self.k = k
    def inorder(root):
        if root == None: return
        r = inorder(root.right)
        if r: return r
        self.k -= 1
        if self.k == 0:
            return root
        l = inorder(root.left)
        return l

    return inorder(root).val

def kthLargest(root, k):
    if root == None: return
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.right
        else:
            root = stack.pop()
            k-=1
            if k == 0: return root.data
            root = root.left


def kthSmallest(root, k):
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            k-=1
            if k == 0: return root.val
            root = root.right