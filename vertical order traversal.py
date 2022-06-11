from collections import deque
def verticalTraversal(self, root) -> list[list[int]]:
    queue = deque()
    if root == None: return []
    queue.append((root,0,0))
    dctv = {}
    
    while queue:
        node, vertical, level = queue.popleft()
        if vertical in dctv:
            dctv[vertical].append((level, node.val))
        else:
            dctv[vertical] = [(level, node.val)]
        
        if node.left: queue.append((node.left, vertical-1, level+1))
        if node.right: queue.append((node.right, vertical+1, level+1))
    
    result = []
    for vertical in sorted(dctv.keys()):
        temp = []
        for j in sorted(dctv[vertical]):
            temp.append(j[1])
        result.append(temp)
    return result

#definitely checkout leetcode
from collections import defaultdict
def helper(self, placement,level, root, dic, limits):
    if(not root):
        return
    
    dic[placement].append((level, root.val))
    limits[0] = min(limits[0], placement)   #instead of using this you can use sorted(dic.keys()) in the first for loop
    limits[1] = max(limits[1], placement)
    
    self.helper(placement-1, level+1, root.left, dic, limits)
    self.helper(placement+1, level+1, root.right, dic, limits)
    
def verticalTraversal(self, root) -> list[list[int]]:
    dic = defaultdict(list)
    limits = [float('inf'), float('-inf')]
    
    self.helper(0,0, root, dic, limits)
    result = []
    
    for i in range(limits[0], limits[1]+1):
        temp = []
        for j in sorted(dic[i]):
            temp.append(j[1])
        result.append(temp)
    return result