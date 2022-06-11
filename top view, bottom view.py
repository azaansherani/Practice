#line concept use hota h nodes ko vertical value assign krte h with root being (0,0)
from collections import deque
def topView(root):
    if root == None: return
    queue = deque()
    queue.append((root, 0))
    ans = []
    dct = {}
    minVert, maxVert = float("inf"), float("-inf")
    while queue:
        node, vertical = queue.popleft()
        minVert = min(minVert, vertical)
        maxVert = max(maxVert, vertical)
        if vertical not in dct:
            dct[vertical] = node.data
        if node.left: queue.append((node.left, vertical-1))
        if node.right: queue.append((node.right, vertical+1))
    ans = []
    for vertical in range(minVert, maxVert+1):
        ans.append(dct[vertical])
        
    return ans
    

def bottomView(self, root):
    if root == None: return
    queue = deque()
    queue.append((root, 0))
    dct = {}
    minVert = float("inf")
    maxVert = float("-inf")
    while queue:
        node, vertical = queue.popleft()
        dct[vertical] = node.data
        minVert = min(minVert, vertical)
        maxVert = max(maxVert, vertical)
        
        if node.left: queue.append((node.left, vertical-1))
        if node.right: queue.append((node.right, vertical+1))
    
    ans = []
    
    for i in range(minVert, maxVert+1):
        ans.append(dct[i])
    return ans


    """
we can use both of these using dfs as well but usme dictionary me tuple store krna pdega (node.val, level) 
fir agr vertical dictinary me h toh compare the level with the existing one (the one in the tuple) then decide what to do with the node
like vertical key exist krti h dictionary me toh check if it's level is greater or lesser than the node we're at right now,
agr current node ka level greater h toh incase of bottom view this would replace the current value of vertical in the dictionary, as we
need last possible level in case of bottom view and vice versa in case of top view
"""
            