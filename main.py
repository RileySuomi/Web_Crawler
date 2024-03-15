import sys
import networkx as ax
import matplotlib.pyplot as plt
import time
import closeness_centrality as cc
import os

import graph as g

def main():
    
    if len(sys.argv) != 2:
        print("Incorrect amount of flags")

    # command line process should be "python main.py <txt.file>"
        
    # .txt file format should be <url> <depth>
    
    # the .txt file
    txt_file = sys.argv[1]

    try: 
        # read file
        with open(txt_file, 'r') as file: 
            # get one line at a time
            for line in file:
                parts = line.strip().split()
                if len(parts) != 2 :
                    print("Invalid format. Each line should be a url and a depth sperated by a space")
                    sys.exit(1)
                #order +=1
                url, depth_as_str= line.split() # splits by the blank space
                depth = int(depth_as_str) # depth needs to be a int

                # processing of the files

                last_time = time.time()
                graph = g.crawl(url, depth) #crawl 
                print(f"Runtime = {time.time() - last_time}")

            sorted_cc = cc.sort_centrality(cc.closeness(graph))
            # for key, value in sorted_cc.items():
            #     if (value != float('inf')):
            #         print(f"url: {key}, Centrality: {value}")
                            
            
            #creating a CSV file:
            path: str = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(path, 'sorted_closeness.csv')
            with open(file_path, 'w', newline='') as file:
                file.write("[url],[desc_central]\n")
                for key, value in sorted_cc.items():
                    if (value != float('inf')):
                        #Writing Rows to the CSV file:
                        file.write(f"{key}, {value}\n")
            
            print("CSV list of closesness's have successfully been put in your filepath!")
            plt.figure(figsize=(12, 8))
            pos = ax.spring_layout(graph)
            ax.draw(graph, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=6, edge_color='gray', arrowsize=10)
            plt.title(f"Web Crawler Graph (Depth={depth})")
            plt.show()

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    
if __name__ == "__main__":   

    #graph.main()
    main()         

    