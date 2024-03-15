import networkx as nx
import heapq as q

import matplotlib.pyplot as plt

# dijkstra algorithm to traverse the tree

def Dijkstra(G, s): # O(e logv)
    
    V = list(G.nodes)
    #print(V)
    S_visited = set()
    pq = [] #priority queue based on weight/distance
    D = {v: float('infinity') for v in V}
    D[s] = 0
    q.heappush(pq, (0, s))
    while pq: #while the queue not empty. 
        
        #Cheapest vertex reachable from q -> pop distance and url
        u = q.heappop(pq)
        S_visited.add(u[1])

        for v in G.neighbors(u[1]): #looping for all adjacent vertex from u
            if v in S_visited:
                continue
            updated_D = D[u[1]] + 1 # +1 because each directed edge only has a weight/ length of 1
            if D[v] > updated_D:
                D[v] = updated_D
                q.heappush(pq, (updated_D, v))    
    sum = 0
    n = 0
    for v in D:
        if D[v] != float('inf'):
            sum += D[v]
            n +=1
    if (sum != 0):
        return n/sum
    else:
        return float('inf')
    

# find closeness of the points 
def closeness(G):
    close_list = {}
    for v in G.nodes:
        shortest = Dijkstra(G, v)
        close_list[v] = shortest
    #print(close_list)
    return close_list

# sort from most close to least
def sort_centrality(closests):
    centralities_list = dict(sorted(closests.items(), key=lambda item: item[1]))
    return centralities_list


# test code

if __name__ == '__main__' :
    
    G = nx.DiGraph()

    G.add_node('A')
    G.add_node('B')
    G.add_edge('A', 'B')
    G.add_node('C')
    G.add_edge('B', 'C')
    G.add_node('D')
    G.add_node('E')
    G.add_edge('B', 'E')
    G.add_edge('C', 'E')
    G.add_edge('D', 'E')
    G.add_edge('A', 'D')
    G.add_edge('D', 'B')

    updated = sort_centrality(closeness(G))
    #print(updated)

    nx.draw(G, with_labels = True, font_weight= 'bold')
    plt.show()
