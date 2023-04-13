class Graph:
    def __init__(self, edges):
        self.edges = edges 
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        
        # print(self.graph_dict)

    def get_paths(self, start, end, path = []):
        path = path + [start]

        ## if start and end are same
        if start == end:
            return [path]
        
        ## if start has no paths originating
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if not node in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        
    
    ## sortest path with minimum number of stops
    def get_shortest_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return path 
        
        if start not in self.graph_dict:
            return None
        
        sortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if sortest_path is None or len(sp) < len(sortest_path):
                        sortest_path = sp

        return sortest_path
            



        





if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start = "Mumbai"
    end = "New York"

    print(f"sortest path between {start} and {end} is : ", route_graph.get_shortest_path(start, end))