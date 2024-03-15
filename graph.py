import networkx as ax
import matplotlib.pyplot as plt
import validator
from bs4 import BeautifulSoup
import heapq as q
import requests
# instantiate the graph

graph = ax.DiGraph()
def crawl(url, depth): 

    # want to create a queue that orders through the hrefs from the starter link 
    queue = [(url, 0)] 

    # want to create a set of visited links.. to make it BFS instead of brute
    visited = set() 

    while queue: #queue not empty

        # get the current url and current depth
        curr_url, curr_depth = q.heappop(queue) 

        # need some conditions based on depth and if valid
        if curr_depth >= depth or not validator.valid_url(curr_url): 
            graph.add_node(curr_url)
            continue 

        #  special case for a depth of zero
        # elif depth == 0:
        #     graph.add_node(curr_url)
        #     continue

        try: 
            res = requests.get(curr_url) # fetch the page

            if res.status_code == 200: # code 200 represents a valide url 
                #print(f"crawling {curr_url} ...")
                soup = BeautifulSoup(res.content, 'html.parser') # parse the current html

                # find all links on the current htsml (a list). 
                # 'a' represents the <a tag in html which is used for hyperlinks, then also make sure it is a href
                links = soup.find_all('a', href=True) 

                # look at all the links 
                for link in links: 
                    next_url = link['href']

                    # check if valid html, some are different
                    if not validator.valid_url(next_url): # page.html
                        continue 

                    #if next url is valid, we want to add it to queue 
                    # as well as increase the depth since we are going to make a jump here
                    # dont want to fetch pages that we already have (append to queue and do it all again)
                    if next_url not in visited:
                        visited.add(next_url)
                        q.heappush(queue, (next_url, curr_depth + 1))

                    # add an edge from current url to here
                    graph.add_edge(curr_url, next_url)
                   
        
        except Exception as err: # error handler
             print(f"Error crawling {curr_url}: {err}")

    # want to return the graph created
    return graph


#
# graph building practice
#


# G = nx.Graph()

# G.add_node(1)
# G.add_node(2)
# G.add_edge(1, 2)
# G.add_node(3)
# G.add_edge(2, 3)
# G.add_node(4)
# G.add_edge(3, 5)
# G.add_node(5)
# G.add_edge(3, 5)
# G.add_edge(4, 5)
# G.add_edge(1, 4)
# G.add_edge(4, 2)


# G.add_node(6)
# G.add_edge(6,7)
# G.add_node(7)
# G.add_edge(7,8)
# G.add_node(8)
# G.add_edge(8,9)
# G.add_node(9)
# G.add_node(10)

# nx.draw(G, with_labels = True, font_weight= 'bold')
# plt.show()

#drawing 2
# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
#plt.show()

# print(G.nodes)
# A =  nx.adjacency_matrix(G)
# A_dense = A.todense()
# print(A_dense)

# G = nx.Graph()

# G.add_node('A')
# G.add_node('B')
# G.add_edge('A', 'B')
# G.add_node('C')
# G.add_edge('B', 'C')
# G.add_node('D')
# G.add_node('E')
# G.add_edge('B', 'E')
# G.add_edge('C', 'E')
# G.add_edge('D', 'E')
# G.add_edge('A', 'D')
# G.add_edge('D', 'B')

# nx.draw(G, with_labels = True, font_weight= 'bold')
# plt.show()

#drawing 2
# G = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
#plt.show()

# print(G.nodes)
# A =  nx.adjacency_matrix(G)
# A_dense = A.todense()
# print(A_dense)