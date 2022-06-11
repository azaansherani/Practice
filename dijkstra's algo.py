from heapq import heappush, heappop, heapify
# the min heap used here ensures that the node with the lowest distance(edgeweight) so far get's popped first
    
def dijkstraS(n, adj_list, source):
    dist = [float("inf") for _ in range(n)]
    dist[source] = 0

    prioQueue = [(0, source)]
    while prioQueue:
        edge_Weight_So_Far, node = heappop(prioQueue) #edge_Weight_So_Far think of it as distance traveled so far, we're looking for shortest distance

        if edge_Weight_So_Far>dist[node]: continue

        for neighbor, edgeWeight in adj_list[node]:

            if edge_Weight_So_Far + edgeWeight < dist[neighbor]:
                dist[neighbor] = edge_Weight_So_Far + edgeWeight
                heappush(prioQueue,(dist[neighbor], neighbor))
    
    print("Dijkstra:",*dist[1:], sep = ' ')

adj_list = [
            [],
            [(2,2),(4,1)],
            [(1,2), (5,5), (3,4)],
            [(2,4),(4,3),(5,1)],
            [(1,1),(3,3)],
            [(2,5), (3,1)]
            ]

dijkstraS(6, adj_list, 1)