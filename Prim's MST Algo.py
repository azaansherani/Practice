#BRUTE FORCE TC: O(n){setting arrays values} + O(n^2) + O(n+e)
def spanningTree(V, adj):
    key = [float("inf")]*V
    parent = [-1]*V
    mst = [False]*V
    
    key[0] = 0
    
    for i in range(V-1):
        mini = float("inf") 
        for i in range(V):      #O(n^2)
            if mst[i] == False and key[i]<mini:
                mini = key[i]
                miniNode = i
            
        mst[miniNode] = True
        
        for nei, edgeWeight in adj[miniNode]: #O(n + e)
            if mst[nei] == False and key[nei]> edgeWeight:
                key[nei] = edgeWeight
                parent[nei] = miniNode

    return key, parent

#Optimized Approach TC: O(n) + O(nlogn) + O(n + e); we basically used a priority instead of calculating min of key at every iteration
from heapq import heappush, heappop

def spanningTree(self, V, adj):
    key = [float("inf")]*V
    parent = [-1]*V
    mst = [False]*V
    key[0] = 0
    prioQueue = [(key[0], 0)] #(key[node], node)
    
    for i in range(V-1):
        miniNode = heappop(prioQueue)[1]  #here we're not checking if the min of key is not already in mst cuz min of key pop ho rhe h, so h hi nhi mst true waale
        mst[miniNode] = True
        
        for nei, edgeWeight in adj[miniNode]:
            if mst[nei] == False and key[nei]> edgeWeight:
                key[nei] = edgeWeight
                parent[nei] = miniNode
                heappush(prioQueue, (key[nei], nei))
    
    #key and parent se form hojaaygi mst
