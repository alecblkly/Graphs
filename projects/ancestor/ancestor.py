from util import Queue  # Importing Queue for BFS

# Copied Graph from graph.py
# Important functionality for the search


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("ERROR: Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("ERROR: Vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    # Defining parent, child relationships - vertex/edge, utilizing Graph
    g = Graph()

    for el in ancestors:
        g.add_vertex(el[0])
        g.add_vertex(el[1])
        g.add_edge(el[1], el[0])
    # Create a Queue
    q = Queue()
    # Enqueue a path to the starting vertex(starting_node)
    q.enqueue([starting_node])
    # Create a set to store visited vertices
    visited = set()
    # No parents set to -1 (Value Variable)
    parents = -1
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # Grab the vertex from the end of the path
        v = path[-1]
        # Check if its been visited
        # If it has not been visited...
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            # Check if path(v) is less than the value variable or length of path is longer than 1(parent)
            if ((v < parents) or (len(path) > 1)):
                # Update value variable
                parents = v
            # Enqueue a path to all its neighbors
            for neighbor in g.get_neighbors(v):
                # Make a copy of the path
                copy = path.copy()
                # Append the neighbor
                copy.append(neighbor)
                # Enqueue the copy
                q.enqueue(copy)
    # Return value variable
    return parents
