# Graph algorithms — grown by the garden one function at a time

class UnionFind:
    """Union-Find with path compression and union by rank. O(alpha(n)) per op."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

from collections import deque


def shortest_path_bfs(graph, start, end):
    """BFS shortest path in unweighted graph. Returns path list or None."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for nb in graph.get(node, []):
            if nb == end:
                return path + [nb]
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, path + [nb]))
    return None

def topological_sort(graph):
    """Kahn's algorithm topological sort. O(V + E).
    Raises ValueError on cycle. graph: {node: [neighbors]}"""
    from collections import deque
    in_degree = {n: 0 for n in graph}
    for node in graph:
        for nb in graph[node]:
            in_degree[nb] = in_degree.get(nb, 0) + 1
    queue = deque(n for n, d in in_degree.items() if d == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph.get(node, []):
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                queue.append(nb)
    if len(order) != len(in_degree):
        raise ValueError("Graph has a cycle")
    return order

def dfs(graph, start, visited=None):
    """DFS traversal (recursive). Returns nodes in visit order."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for nb in graph.get(start, []):
        if nb not in visited:
            order.extend(dfs(graph, nb, visited))
    return order


def dfs_iterative(graph, start):
    """DFS traversal (iterative). Avoids recursion depth limits."""
    visited, stack, order = set(), [start], []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for nb in reversed(graph.get(node, [])):
                if nb not in visited:
                    stack.append(nb)
    return order
