"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a Queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While Queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if it has been visited
            # If it has not been visited...
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # Enqueue all of its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a Stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it has been visited
            # If it has not been visited...
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # Push all of its neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        # Unable to define set for visited in function definitions
        if visited is None:
            # Set to store visited vertices
            visited = set()
        print(starting_vertex)
        # Mark it as visited
        visited.add(starting_vertex)
        # Call dft_recursive on each neighbor, similar to what was done
        # within dft, but with using recursion
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a Queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if its been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    copy = path.copy()
                    # Append the neighbor
                    copy.append(neighbor)
                    # ENQUEUE THE COPY
                    q.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a Stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if its been visited
            # If it has been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN THE PATH
                    return path
                # Push A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    copy = path.copy()
                    # Append the neighbor
                    copy.append(neighbor)
                    # Push THE COPY
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check if the node has been visited
        if visited is None:
            visited = set()
        # Check if a path exists
        if path is None:
            path = []
        # Mark it as visited
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # Checking to see if we are at the destination, if we are return the path
        if starting_vertex == destination_vertex:
            return path
        # Call dfs_recursive on each neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            # If the neighbor is not in the visited set
            if neighbor not in visited:
                updated_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                # If items are within the updated_path, return it
                if updated_path is not None:
                    return updated_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("BFT: ")
    graph.bft(1)
    print("---")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT: ")
    graph.dft(1)
    print("---")
    print("DFT, recursive: ")
    graph.dft_recursive(1)
    print("---")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS: ")
    print(graph.bfs(1, 6))
    print("---")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS: ")
    print(graph.dfs(1, 6))
    print("---")
    print("DFS, recursive: ")
    print("---")
    print(graph.dfs_recursive(1, 6))
