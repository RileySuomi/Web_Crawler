import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_edge(1, 2)
G.add_node(3)
G.add_edge(2, 3)
G.add_node(4)
G.add_edge(3, 5)
G.add_node(5)
G.add_edge(3, 5)
G.add_edge(4, 5)
G.add_edge(1, 4)
G.add_edge(4, 2)


G.add_node(6)
G.add_edge(6,7)
G.add_node(7)
G.add_edge(7,8)
G.add_node(8)
G.add_edge(8,9)
G.add_node(9)
G.add_node(10)

nx.draw(G, with_labels = True, font_weight= 'bold')
plt.show()

#drawing 2
# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
#plt.show()

print(G.nodes)