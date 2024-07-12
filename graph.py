class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex,  edges in self.adj_list.items():
            print(vertex," : ", edges)
    
    def add_vertex(self, vertex):
        if not vertex in self.adj_list: # vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            for other_v in self.adj_list[v]:
                self.adj_list[other_v].remove(v)
            del self.adj_list[v]
            return True
        return False
    
    
"""myGraph = Graph()
print(myGraph.add_vertex('A'))
print(myGraph.add_vertex('B'))
print(myGraph.add_vertex('A'))
print(myGraph.add_vertex('C'))
print(myGraph.add_vertex('F'))
print(myGraph.add_edge('A', 'B'))
print(myGraph.add_edge('B', 'C'))
print(myGraph.add_edge('C', 'D'))
print(myGraph.add_edge('C', 'A'))
myGraph.print_graph()
print(myGraph.remove_edge('C', 'A'))
print(myGraph.remove_edge('C', 'F'))
myGraph.print_graph()"""

#Example for remove vertex 
myGraph = Graph()
myGraph.add_vertex('A')
myGraph.add_vertex('B')
myGraph.add_vertex('C')
myGraph.add_vertex('D')
myGraph.add_edge('A', 'B')
myGraph.add_edge('B', 'D')
myGraph.add_edge('D', 'A')
myGraph.add_edge('D', 'C')
myGraph.add_edge('C', 'A')
myGraph.print_graph()
print("Remove Vertex : ", 'D')
myGraph.remove_vertex('D')
myGraph.print_graph()        