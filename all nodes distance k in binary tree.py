# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/1283885/Elegant-Python-DFS-solution

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque
def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    def markParents(root, parentTrack):
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    parentTrack[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parentTrack[node.right] = node
                    queue.append(node.right)
        
    if root == None: return
    parentTrack = {}
    markParents(root, parentTrack)
    
    queue = deque()
    queue.append(target)
    visited = {target: True}
    distance = 0
    ans = []
    while queue and distance!=k:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            
            if node.left and node.left not in visited:
                queue.append(node.left)
                visited[node.left] = True
                
            if node.right and node.right not in visited:
                queue.append(node.right)
                visited[node.right] = True

            if node in parentTrack:
                if parentTrack[node] not in visited:
                    queue.append(parentTrack[node])
                    visited[parentTrack[node]] = True
        distance+=1
    ans = []
    for i in queue:
        ans.append(i.val)
    return ans