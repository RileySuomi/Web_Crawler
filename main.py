
from bs4 import BeautifulSoup
import requests
import networkx as nx
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

import validator

#A node that store representative url and href

class GraphVertex:
    def __init__(self, node_id, url):
        self.node_id = node_id
        self.url = u

def crawl(url, depth): 

    graph = Digraph() # instantiate the graph

    # want to create a queue that orders through the hrefs from the starter link 
    queue = [(url, 0)] 

    while queue: #queue not empty
        curr_url = queue.pop(0) 
        curr_depth = 0

        # need some conditions based on depth and if valid
        if curr_depth > depth and validator.valid_url(next_url) == False: 
            continue 

        try: 
            res = requests.get(curr_url) # fetch the page

            if res.status_code == 200: # code 200 represents a valide url 

                soup = BeautifulSoup(res.content, 'html parser') # parse the current html

                # find all links on the current html (a list). 
                # 'a' represents the <a tag in html which is used for hyperlinks, then also make sure it is a href
                links = soup.find_all('a', href=True) 

                # look at all the links 
                for link in links: 
                    next_url = link['href']

                    # check if valid html, some are different
                    if not validator.valid_url(next_url): # page.html
                        continue 
                    else:
                        graph.add_edge(curr_url, next_url)

        
        except Exception as here: 
             print(f"Error crawling {curr_url}: {here}")




def main():

    pass

if __name__ == "main":
    main()
