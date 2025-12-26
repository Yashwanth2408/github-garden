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

import heapq


def dijkstra(graph, start):
    """Dijkstra shortest paths from start. O((V+E) log V).
    graph: {node: [(neighbor, weight)]}
    Returns dict of {node: shortest_distance}."""
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist.get(node, float('inf')):
            continue
        for nb, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nb, float('inf')):
                dist[nb] = nd
                heapq.heappush(pq, (nd, nb))
    return dist

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

def bellman_ford(edges, num_vertices, start):
    """Bellman-Ford shortest paths. O(VE). Detects negative cycles.
    edges: [(u, v, weight)]. Returns dist dict or None on neg cycle."""
    dist = {i: float('inf') for i in range(num_vertices)}
    dist[start] = 0
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # negative cycle
    return dist

from collections import deque


def bfs(graph, start):
    """BFS traversal. Returns nodes in visit order.
    graph: {node: [neighbors]}"""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph.get(node, []):
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return order

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

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

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

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

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

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

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

def has_cycle_directed(graph):
    """Detect cycle in directed graph via DFS coloring. O(V + E)."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def dfs(node):
        color[node] = GRAY
        for nb in graph.get(node, []):
            if color[nb] == GRAY or (color[nb] == WHITE and dfs(nb)):
                return True
        color[node] = BLACK
        return False

    return any(dfs(n) for n in graph if color[n] == WHITE)

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
