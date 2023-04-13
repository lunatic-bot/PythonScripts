## make rank and parent set
def makeSet(parent, rank, n):
    for i in range(n):
        parent[i] = i
        rank[i] = 0


## find parent of a node
def findParent(parent, node):
    if parent[node] != node:

        parent[node] = findParent(parent, parent[node])
    return parent[node]


## find union set of two vertices
def unionSet(u, v, parent, rank):
    ## find parent of both u and v
    u = findParent(parent, u)
    v = findParent(parent, v)

    ## if rank of v is greater, make v the parent
    if rank[u] < rank[v]:
        parent[u] = v
    
    ## else make u the parent
    elif rank[u] > rank[v]:
        parent[v] = u

    else:
        ## we can meke any of the node parent
        parent[v] = u
        ## increment the rank of parent
        rank[u] += 1

## 
def minimumSpanningTree(edges):
    """"
    edges is a nx3 array where n is number of vertices
    and each row will represent one edge and its weight

    """
    n = len(edges)
    parent, rank = [0] * n, [0] * n
    makeSet(parent, rank, n)


    ## sort edges array with respect to weights
    edges = sorted(edges, key = lambda x: x[2])

    ## initialize minimum weight
    minimumWeight = 0
    
    ## iterate over sorted edges and edge one by one(edge with smallest weight)
    for i in range(n):
        ## find parent for both vertices
        u = findParent(parent, edges[i][0])
        v = findParent(parent, edges[i][1])
        weight = edges[i][2]

        ## if both have different parents, make unionset of both
        if u != v:
            minimumWeight += weight
            unionSet(u, v, parent, rank)
    
    return minimumWeight


graph = [[1, 4, 1], [1, 2, 2], [2, 3, 3], [2, 4, 3], [1, 5, 4], 
         [3, 4, 5], [2, 6, 7], [3, 6, 8], [4, 5, 9]]

if __name__ == "__main__":
    min_weight = minimumSpanningTree(graph)
    print(min_weight)
