# class Graph:

## adjacency matrix representation of graph ::
# n, m = 5, 7
# adjMat = [[0 for i in range(n)] for j in range(n)]

# # edges = [(1,2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 4), (1, 3)]

# edges = [(0, 1), (1,2), (2, 3), (3, 4), (0, 4), (1, 3), (0, 2)]

# for i in range(n):
#     u, v = edges[i]
#     adjMat[u][v] = 1
#     adjMat[v][u] = 1

# print(adjMat)


## Adjacency list representation of graph
"""An array of linked lists is used. The size of the array is equal to the number of vertices.
et the array be an array[]. An entry array[i] represents the linked list of vertices adjacent 
to the ith vertex. This representation can also be used to represent a weighted graph. 
The weights of edges can be represented as lists of pairs."""

## node of adjacency list(linked list)
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
 
    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
 
 
# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
 
    graph.print_graph()








