# Introduction to WebCrawler
Collaborative work with teammate to implement a graph through systematic way of crawling through the web. 


# Projects Goals: 
+ Practice using third-party libraries
+ Apply knowledge of graphs to real-world problem
+ Apply understandings of time complexity
+ Enhance problem-solving skills


## Description

This program takes in a text file which contains multiple or maybe just one line of Url(s) with each url have a number with it, in the format : URL digit. The digit
represents the depth we want to search through that corresponding Url, meaning how many jumps we want to make from that starting point. From this input the program crawls web pages up to the specified depth, analyzing all the hrefs and creating a network graph in terms of centrality of all the links and produces a pop-up GUI of the created graph. In the end, we are able to see with our csv of which nodes of the created graph are "most" central and connected to the rest of the graph.


## Requirements

First need to make sure you have python on your system (py 3.12) :

1. install pip 
2. install py

..then configure py interpreter into your path

Install additional packages for various library access for functions and support :

1. pip install validators 
2. pip insatll beautifulsoup4
3. pip insatll PyQt5
4. pip insatll requests
5. pip insatll algorithms
6. pip insatll networkx
7. pip install matplotlib
8. pip install scipy (internal math library)
9. pip install heapq
10. pip install matplotlib.pyplot


## User Manual

To start the program. You must enter your list of input(s) line-by-line in URL_List.txt. Your input must be in this form:
        "url depth\n"

1. Open new terminal. 
2. run 'python main.py URL_List.txt'
3. In the terminal, the first output is the Runtime of the program.
4. Next, a CSV file is generated and saved within your repository's directory in File Explorer. The same file is also included in your IDE as "sorted_closeness.csv". This file is the sorted list from the most central url to the least (top to bottom) along with their degree of centrality. 
5. Lastly, a user interface will pop up and show the representive image of the directed graph. Each circle represent each vertex of url, and each arrow with direction represent each directed edge of the vertex pair.


## Reflection

Next to all the functions we have included time complexities in comments.

One of our first troubles we ran into was where we made our own implementation of dijkstra and at first we had problems with runtime and it being too long. Over the course of some time we analyzed areas we could optimize and made those changes to achieve faster runtimes. Examples were - learning about heapq library and queue optimization and also to better track visistied webpages that way we wouldn't need to load that html all over again if previously done so. 

For the most part, our first week of starting the project were all about research & design and we hardly started implementing code, which was very benefical and is a good method. We focused on what the goal of a task was and what stages we needed to comeplete such. Then when we got to implementation phase, we had it all layed out and found progress and productivity in implementing our functions. The main difficulties we ran into were moments of design and how we wanted our program to take inputs and display the outputs, in which we changed the methods multiple times. We finalized with the idea that taking in a text file was easiest in the form of test cases because it allowed us to easily change the input as well as test multiple Urls together, creating more interesting outputs in terms of connectivity and closeness. Then displaying outputs we came down to producing a csv in same directory that gets overwritten each time you run it, as well as a pop-up visual of the graph. Which the design off this pop-up visual can possibly be updated "nicer" but in terms of scalability, as you start getting large inputs the graph is going to have a lot of nodes and edges to display and becomes a mess anyway.

There is reference to our tasks layout at the bottom of this README.



## Results

**These results are specific for a test of " https://chess.com 2 "**

CSV list : 


![webcrawler_csv_list](https://github.com/DANNY130/WebCrawler/assets/97262216/003713ad-556a-45fd-a896-564ee97650af)



Visual Graph: 


![webcrawler_visual_graph](https://github.com/DANNY130/WebCrawler/assets/97262216/a79cedfe-d3f5-407e-9bbf-8f2d32fb77ac)



## Tasks:
**Workflow tasks:**
+ Validate URLs and depth function
+ Retrieve function HTML from each URLs
+ Parse url from href on the current webpage function 
+ Create a graph in memory and update function for correct depth 
+ Print graph function
+ closeness computation 
+ Print closeness computation process

**Program Output Tasks:**
+ Parse HTML function
+ Find function for link (href attribute reference) 
+ Encrypting function for URL_list files
+ Graphical display - Graph representation 
+ Generate function to a CSV file of crawled webpage's closeness as output
+ Function measuring centrality.
