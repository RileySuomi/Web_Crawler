import sys
from bs4 import BeautifulSoup
import requests
import networkx as nx
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from nanoid import generate
import validator

#Adding directed edge function:
def add_edge(G,url, url1):
    id = generate(size = 10)
    G.add_node(id, url = url)

    id1 = generate(size = 10)
    G.add_node(id1, url = url1)
    
    G.add_edge(id, id1)





def crawl(url, depth): 

    # instantiate the graph
    graph = nx.DiGraph() 

    # want to create a queue that orders through the hrefs from the starter link 
    queue = [(url, 0)] 

    while queue: #queue not empty

        # get the current url and current depth
        curr_url, curr_depth = queue.pop(0) 

        # need some conditions based on depth and if valid
        if curr_depth > depth or not validator.valid_url(curr_url): 
            continue 

        try: 
            res = requests.get(curr_url) # fetch the page

            if res.status_code == 200: # code 200 represents a valide url 
                print(f"crawling {curr_url} ...")
                soup = BeautifulSoup(res.content, 'html.parser') # parse the current html

                # find all links on the current html (a list). 
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
                    queue.append((next_url, curr_depth + 1))

                    # add an edge from current url to here
                    #graph.add_edge(curr_url, next_url)
                    add_edge(graph, curr_url, next_url)

        
        except Exception as err: # error handler
             print(f"Error crawling {curr_url}: {err}")

    # want to return the graph created
    return graph

def main():
    #with open('URL_List.txt','r') as  file:
        
        #pass
    pass

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Incorrect amount of flags")

    # command line process should be "python <url> <depth>"
    url = sys.argv[0]
    depth = int(sys.argv[1])

    graph = crawl(url, depth)