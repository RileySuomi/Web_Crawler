
#Algorithms examples
import heapq as q
#import algorithms #library that implements a LOTT

#from algorithms.sort import bogo_sort as bg # example using bogo 

if __name__ == "__main__":
#     my_list = [1, 8, 3, 5, 6]
#     my_list = bg(my_list)
#     print(my_list)

    pq = []
    q.heappush(pq, (0, 'A'))
    u = q.heappop(pq)
    print(u[0])
    print(u[1])