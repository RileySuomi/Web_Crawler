import networkx as nx
import heapq as q
from nanoid import generate

Graph = nx.DiGraph()


#Adding directed edge function:
def add_edge(G,url, url1):
    id = generate(size = 10)
    G.add_node(id, url = url)

    id1 = generate(size = 10)
    G.add_node(id1, url = url1)
    
    G.add_edge(id, id1)


def Dijkstra(Graph, s):
    D = {v: int('infinity') for v in }
    V = list(G.nodes)
    #for v in V: