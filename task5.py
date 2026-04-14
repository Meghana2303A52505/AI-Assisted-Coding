"""Write a Python program to implement a Graph using adjacency list.

Requirements:
- Methods:
  add_vertex(vertex)
  add_edge(v1, v2)
  display()

- Use dictionary for adjacency list
- Add comments and example graph"""
class Graph:
    """A simple graph implementation using adjacency list"""
    
    def __init__(self):
        """Initialize an empty graph using a dictionary"""
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2):
        """Add an edge between two vertices (undirected)"""
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def display(self):
        """Display the graph adjacency list"""
        print("Graph Adjacency List:")
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {neighbors}")


# Example usage
if __name__ == "__main__":
    g = Graph()
    
    # Add vertices
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    
    # Add edges
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    
    # Display graph
    g.display()