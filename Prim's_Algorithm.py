"""
---------------------------------------------------------------
Prim’s Algorithm for Minimum Spanning Tree (MST)
---------------------------------------------------------------

Description:
Prim’s Algorithm builds an MST for a connected, weighted, undirected graph.
It starts with any vertex and grows the MST by repeatedly adding the smallest
edge that connects a vertex inside the MST to a vertex outside it.

Time Complexity:  O(E log V)
Space Complexity: O(V + E)

---------------------------------------------------------------
"""

import heapq

class Graph:
    def __init__(self, vertices):
        """Initialize graph with given number of vertices."""
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]  # adjacency list

    def add_edge(self, u, v, w):
        """Add an undirected edge (u, v) with weight w."""
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def prim_mst(self, start=0):
        """
        Perform Prim’s Algorithm to find MST.
        Returns a list of (u, v, weight) representing MST edges and total cost.
        """
        visited = [False] * self.V
        min_heap = [(0, start, -1)]  # (weight, current_node, parent)
        mst_edges = []
        total_cost = 0

        while min_heap:
            weight, u, parent = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            total_cost += weight

            # Ignore first dummy edge (parent = -1)
            if parent != -1:
                mst_edges.append((parent, u, weight))

            # Push all adjacent edges
            for v, w in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v, u))

        return mst_edges, total_cost


# ---------------- DRIVER CODE ----------------

def main():
    print("Enter number of vertices and edges: ", end="")
    V, E = map(int, input().split())

    graph = Graph(V)
    print(f"Enter {E} edges in the format: u v w")
    print("(0-indexed vertices)\n")

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph.add_edge(u, v, w)

    start_vertex = int(input("Enter starting vertex (0-indexed): "))
    mst_edges, total_cost = graph.prim_mst(start=start_vertex)

    print("\nEdges in the Minimum Spanning Tree:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} (weight = {w})")

    print(f"\nTotal cost of MST: {total_cost}")


if __name__ == "__main__":
    main()


"""
---------------------------------------------------------------
SAMPLE INPUT
5 6
0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
0

---------------------------------------------------------------
SAMPLE OUTPUT
Edges in the Minimum Spanning Tree:
0 - 1 (weight = 2)
1 - 2 (weight = 3)
1 - 4 (weight = 5)
0 - 3 (weight = 6)

Total cost of MST: 16

---------------------------------------------------------------
EXPLANATION
The MST connects all vertices with minimum total edge weight.
The chosen edges form a connected acyclic graph with cost 16.
---------------------------------------------------------------
"""
