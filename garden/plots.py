import hashlib
import json
import os
import random
import re
from datetime import date, timedelta


def _daily_seed(target_date: date, offset: int = 0) -> int:
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32) + offset


# ── ALGORITHM POOL ───────────────────────────────────────────────────────────

_ALGORITHM_POOL = {
    'sorting': [
        ('bubble_sort', '''
def bubble_sort(arr):
    """Bubble sort. O(n²) time, O(1) space. Stable."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
'''),
        ('insertion_sort', '''
def insertion_sort(arr):
    """Insertion sort. O(n²) worst, O(n) best, O(1) space. Stable."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
'''),
        ('merge_sort', '''
def merge_sort(arr):
    """Merge sort. O(n log n) time, O(n) space. Stable."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
'''),
        ('quick_sort', '''
def quick_sort(arr, low=None, high=None):
    """Quicksort. O(n log n) average, O(n²) worst, O(log n) space."""
    if low is None:
        low, high = 0, len(arr) - 1
    if low < high:
        p = _partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
'''),
        ('heap_sort', '''
def heap_sort(arr):
    """Heapsort. O(n log n) time, O(1) space. Not stable."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr


def _heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)
'''),
        ('counting_sort', '''
def counting_sort(arr, max_val=None):
    """Counting sort for non-negative integers. O(n + k) time and space."""
    if not arr:
        return arr
    if max_val is None:
        max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for num, freq in enumerate(count):
        result.extend([num] * freq)
    return result
'''),
        ('shell_sort', '''
def shell_sort(arr):
    """Shell sort with Knuth sequence. O(n^1.5) average, O(1) space."""
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr
'''),
        ('binary_search', '''
def binary_search(arr, target):
    """Binary search in sorted array. O(log n) time, O(1) space.
    Returns index if found, -1 otherwise."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
'''),
        ('binary_search_leftmost', '''
def binary_search_leftmost(arr, target):
    """Find leftmost occurrence in sorted array. O(log n) time."""
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if low < len(arr) and arr[low] == target else -1
'''),
        ('radix_sort', '''
def radix_sort(arr):
    """Radix sort for non-negative integers. O(d*(n+b)) time, stable."""
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for num in arr:
        count[(num // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for num in reversed(arr):
        d = (num // exp) % 10
        count[d] -= 1
        output[count[d]] = num
    return output
'''),
    ],
    'graphs': [
        ('bfs', '''
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
'''),
        ('dfs', '''
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
'''),
        ('dijkstra', '''
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
'''),
        ('topological_sort', '''
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
'''),
        ('union_find', '''
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
'''),
        ('has_cycle', '''
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
'''),
        ('shortest_path', '''
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
'''),
        ('bellman_ford', '''
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
'''),
    ],
    'trees': [
        ('bst', '''
class BST:
    """Binary Search Tree — insert, search, in-order traversal."""

    class _Node:
        def __init__(self, val):
            self.val = val
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return self._Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):
        node = self.root
        while node:
            if val == node.val:
                return True
            node = node.left if val < node.val else node.right
        return False

    def inorder(self):
        result = []
        def _walk(n):
            if n:
                _walk(n.left); result.append(n.val); _walk(n.right)
        _walk(self.root)
        return result
'''),
        ('trie', '''
class Trie:
    """Trie (prefix tree) — insert, search, starts_with."""

    class _Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self._Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, self._Node())
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
'''),
        ('lca', '''
def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)
'''),
        ('tree_height', '''
def tree_height(root):
    """Height of binary tree. O(n) time."""
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def is_balanced(root):
    """True if tree is height-balanced. O(n) time."""
    def check(node):
        if node is None:
            return 0
        l, r = check(node.left), check(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    return check(root) != -1
'''),
        ('level_order', '''
from collections import deque


def level_order(root):
    """Level-order (BFS) traversal. Returns list of levels."""
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
'''),
        ('serialize_tree', '''
from collections import deque


def serialize(root):
    """Serialize binary tree to comma string using BFS."""
    if not root:
        return '#'
    parts, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            parts.append('#')
        else:
            parts.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
    return ','.join(parts)


def deserialize(data):
    """Reconstruct binary tree from serialized string."""
    from types import SimpleNamespace
    vals = data.split(',')
    if vals[0] == '#':
        return None
    make = lambda v: SimpleNamespace(val=int(v), left=None, right=None)
    root = make(vals[0])
    queue, i = deque([root]), 1
    while queue and i < len(vals):
        node = queue.popleft()
        if vals[i] != '#':
            node.left = make(vals[i]); queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != '#':
            node.right = make(vals[i]); queue.append(node.right)
        i += 1
    return root
'''),
    ],
    'dp': [
        ('fibonacci', '''
def fib(n):
    """Nth Fibonacci number. O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_memo(n, _cache={}):
    """Nth Fibonacci with memoization. O(n) time and space."""
    if n in _cache:
        return _cache[n]
    if n <= 1:
        return n
    _cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return _cache[n]
'''),
        ('lcs', '''
def lcs(s, t):
    """Longest Common Subsequence. O(mn) time and space.
    Returns the subsequence string."""
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == t[j-1] else max(dp[i-1][j], dp[i][j-1])
    seq, i, j = [], m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            seq.append(s[i-1]); i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(seq))
'''),
        ('knapsack', '''
def knapsack_01(weights, values, capacity):
    """0/1 Knapsack. O(n * capacity) time and space.
    Returns (max_value, list_of_selected_indices)."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i-1]
    return dp[n][capacity], list(reversed(selected))
'''),
        ('edit_distance', '''
def edit_distance(s, t):
    """Levenshtein edit distance. O(mn) time and space."""
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j-1] if s[i-1] == t[j-1] else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
'''),
        ('coin_change', '''
def coin_change(coins, amount):
    """Minimum coins for amount. O(n * amount). Returns -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """Count distinct ways to make amount. O(n * amount)."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
'''),
        ('kadane', '''
def kadane(arr):
    """Maximum subarray sum (Kadane). O(n) time, O(1) space.
    Returns (max_sum, start, end)."""
    best = curr = arr[0]
    best_s = best_e = tmp_s = 0
    for i in range(1, len(arr)):
        if curr + arr[i] < arr[i]:
            curr = arr[i]; tmp_s = i
        else:
            curr += arr[i]
        if curr > best:
            best = curr; best_s = tmp_s; best_e = i
    return best, best_s, best_e
'''),
        ('lis', '''
import bisect


def lis_length(arr):
    """Longest Increasing Subsequence length. O(n log n) — patience sorting."""
    tails = []
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
'''),
    ],
    'strings': [
        ('kmp', '''
def kmp_search(text, pattern):
    """KMP string search. O(n + m) time.
    Returns list of start indices where pattern occurs."""
    if not pattern:
        return list(range(len(text)))
    lps = _build_lps(pattern)
    matches, j = [], 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j - 1]
    return matches


def _build_lps(p):
    lps = [0] * len(p)
    length, i = 0, 1
    while i < len(p):
        if p[i] == p[length]:
            length += 1; lps[i] = length; i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0; i += 1
    return lps
'''),
        ('z_algorithm', '''
def z_function(s):
    """Z-array: z[i] = longest substring starting at i matching prefix. O(n)."""
    n = len(s)
    z = [0] * n; z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


def find_pattern_z(text, pattern):
    """Find all occurrences of pattern using Z-function."""
    s = pattern + '$' + text
    z = z_function(s)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(s)) if z[i] == m]
'''),
        ('anagram', '''
from collections import Counter


def is_anagram(s, t):
    """Check if s and t are anagrams. O(n) time."""
    return Counter(s) == Counter(t)


def find_anagrams(s, p):
    """Find all start indices of p's anagrams in s. O(n) sliding window."""
    if len(p) > len(s):
        return []
    need = Counter(p)
    window = Counter(s[:len(p)])
    result = [0] if window == need else []
    for i in range(len(p), len(s)):
        ch_in, ch_out = s[i], s[i - len(p)]
        window[ch_in] += 1
        window[ch_out] -= 1
        if window[ch_out] == 0:
            del window[ch_out]
        if window == need:
            result.append(i - len(p) + 1)
    return result
'''),
        ('palindrome', '''
def is_palindrome(s):
    """Check palindrome ignoring case and non-alphanumeric. O(n)."""
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]


def longest_palindromic_substring(s):
    """Longest palindromic substring — expand around center. O(n²)."""
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l + 1:r]

    best = ''
    for i in range(len(s)):
        for sub in (expand(i, i), expand(i, i + 1)):
            if len(sub) > len(best):
                best = sub
    return best
'''),
        ('brackets', '''
def is_valid_brackets(s):
    """Check balanced brackets. O(n) time, O(n) space."""
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return not stack


def min_remove_to_valid(s):
    """Remove minimum parens to make string valid. O(n)."""
    open_stack, to_remove = [], set()
    for i, ch in enumerate(s):
        if ch == '(':
            open_stack.append(i)
        elif ch == ')':
            if open_stack:
                open_stack.pop()
            else:
                to_remove.add(i)
    to_remove.update(open_stack)
    return ''.join(ch for i, ch in enumerate(s) if i not in to_remove)
'''),
    ],
}

# ── TIL ENTRIES ──────────────────────────────────────────────────────────────

_TIL_ENTRIES = [
    "Python's `functools.cache` is a simpler alias for `lru_cache(maxsize=None)` added in 3.9.",
    "Git's `--fixup` flag creates a commit that auto-squashes into another when you rebase with `--autosquash`.",
    "`dict.setdefault(key, default)` only sets the key if it's missing — unlike `dict[key] = default`.",
    "In Python, `a, *b, c = [1,2,3,4,5]` gives `a=1`, `b=[2,3,4]`, `c=5` — extended unpacking.",
    "SQL `EXPLAIN ANALYZE` shows actual vs estimated row counts — key for spotting bad plans.",
    "The `__slots__` class attribute prevents instance dicts, reducing memory ~40% for data-heavy classes.",
    "`git stash push -m 'name' -- file1 file2` stashes only specific files with a label.",
    "Python's `bisect` module gives O(log n) insertion into sorted lists without a full re-sort.",
    "`collections.Counter` supports arithmetic: `c1 + c2`, `c1 - c2`, `c1 & c2` all work.",
    "In bash, `!!` repeats the last command — `sudo !!` is the classic 'forgot sudo' fix.",
    "HTTP 429 is 'Too Many Requests' — the standard rate-limit response with `Retry-After` header.",
    "Python's `zip(strict=True)` (3.10+) raises an error if iterables have different lengths.",
    "Linux `ionice -c 3 cmd` runs a command at idle I/O priority so it doesn't starve others.",
    "`git log --follow -p -- file` shows full diff history even across renames.",
    "In Python, `object.__init_subclass__` runs whenever a class is subclassed — useful for registries.",
    "PostgreSQL's `RETURNING` clause gives back values from INSERT/UPDATE/DELETE in one round trip.",
    "CSS `contain: layout` prevents a subtree from affecting external layout — great for perf isolation.",
    "Python's `textwrap.dedent` strips common leading whitespace from multiline strings.",
    "`git bisect run pytest tests/` automates binary search for the commit that broke tests.",
    "In Python, `__class_getitem__` makes a class subscriptable without metaclass magic.",
    "The Linux `perf stat` command gives CPU cycle counts, cache misses, and branch mispredictions.",
    "`dict | other_dict` merges dicts in Python 3.9+ — `|=` updates in place.",
    "In SQL, `LATERAL` joins let each row on the left use a correlated subquery on the right.",
    "Python's `__set_name__` descriptor hook fires when the descriptor is assigned to a class attribute.",
    "`git worktree add ../branch-name branch-name` checks out a branch into a separate directory.",
    "In HTTP/2, a single TCP connection multiplexes many streams — no head-of-line blocking.",
    "Python's `match` statement (3.10+) supports structural pattern matching, not just value equality.",
    "`grep -E` enables extended regex — same as `egrep`. `-P` enables Perl-compatible regex.",
    "In Python, `type(obj).__mro__` shows the full method resolution order.",
    "PostgreSQL's `pg_stat_statements` extension tracks per-query stats — essential for tuning.",
    "CSS `grid-template-areas` lets you name grid zones and reference them in `grid-area`.",
    "Python's `asyncio.gather` runs coroutines concurrently; `asyncio.TaskGroup` (3.11+) handles errors better.",
    "`git shortlog -sn --no-merges` shows commit counts per author.",
    "In Python, `__missing__` on a `dict` subclass is called when a key isn't found.",
    "Linux `ss -tlnp` shows TCP listening sockets with process names — faster than `netstat`.",
    "Python's `dataclasses.field(default_factory=list)` creates a fresh list per instance, not shared.",
    "The HTTP `Idempotency-Key` header lets clients safely retry POST requests.",
    "`git blame -L 10,20 file` limits blame output to specific lines.",
    "In Python, `importlib.reload(module)` re-executes module code — useful in REPLs.",
    "PostgreSQL `COPY` is 10-100x faster than `INSERT` for bulk data loading.",
    "CSS `clamp(min, preferred, max)` replaces many media queries for fluid typography.",
    "Python's `pathlib.Path.rglob('*.py')` recursively globs files — cleaner than `os.walk`.",
    "`docker system prune -af --volumes` reclaims all unused images, containers, and volumes.",
    "In Python, `weakref.WeakValueDictionary` lets values be GC'd if no other refs exist.",
    "SQL window functions (`ROW_NUMBER`, `LAG`, `LEAD`, `RANK`) work without collapsing rows.",
    "Python's `subprocess.run(['cmd'], capture_output=True, text=True)` is the modern API.",
    "`git cherry-pick -n HASH` stages changes without committing — lets you squash multiple picks.",
    "In Python, `__future__.annotations` defers annotation evaluation — useful for forward refs.",
    "Linux `lsof -i :8080` lists processes holding a port open.",
    "Python's `heapq.nlargest(k, iterable)` is O(n log k) — faster than full sort when k << n.",
    "In HTTP, `Cache-Control: stale-while-revalidate=N` serves stale content while fetching fresh.",
    "Python's `itertools.islice` lazily slices any iterator without materializing it.",
    "`git log --graph --oneline --all` prints a compact visual branch graph.",
    "In Python, `contextlib.suppress(Exception)` cleanly ignores specific exceptions.",
    "PostgreSQL `JSONB` with `@>` does containment queries using GIN indexes efficiently.",
    "Python's `__init_subclass__` + `__subclasses__()` is a plugin registry without metaclasses.",
    "CSS `aspect-ratio: 16/9` maintains proportions without the padding-bottom hack.",
    "`time curl -o /dev/null -s -w '%{time_total}\\n' URL` measures HTTP response time.",
    "In Python, `struct.pack` and `struct.unpack` convert between Python values and C structs.",
    "Git's `rerere` (reuse recorded resolution) auto-applies previous conflict resolutions.",
    "Python's `logging.captureWarnings(True)` redirects `warnings.warn` into logging.",
    "In SQL, `EXCEPT` returns rows in the first query not in the second — set subtraction.",
    "Python's `sys.getsizeof` is shallow size only; `tracemalloc` tracks all allocations.",
    "`curl -v --compressed URL` tests if a server supports gzip/br content encoding.",
    "In Python, `__slots__` on a child class must include `__dict__` if the parent doesn't use slots.",
    "PostgreSQL `EXPLAIN (BUFFERS)` shows cache hit/miss counts — crucial for I/O analysis.",
    "CSS `scroll-behavior: smooth` enables smooth scrolling for same-page anchors with one line.",
    "Python's `abc.abstractmethod` + `@property` creates abstract properties subclasses must implement.",
    "`git log -S 'string'` shows commits that added or removed that exact string — pickaxe search.",
    "In Python, `functools.reduce` with `operator.or_` merges a list of dicts.",
    "Linux `ncdu` gives an interactive ncurses directory size explorer.",
    "Python's `zipfile.ZipFile` can open ZIP files as context managers and iterate entries.",
    "In HTTP, `Accept-Encoding: br` requests Brotli — ~20% smaller than gzip.",
    "Python's `__repr__` should return something `eval()` can reconstruct; `__str__` is for humans.",
    "`docker stats --no-stream` gives a one-shot snapshot of container resource usage.",
    "In Python, `itertools.chain.from_iterable` handles arbitrary-depth list flattening.",
    "PostgreSQL `VACUUM ANALYZE` reclaims dead rows and updates planner statistics.",
    "CSS `will-change: transform` hints browser to promote element to its own compositor layer.",
    "`git rebase --onto new-base old-base branch` replants a branch onto a different parent.",
    "In Python, `threading.local()` provides per-thread storage — each thread sees its own copy.",
    "SQL `MERGE` (or `INSERT ... ON CONFLICT`) is an upsert — insert or update atomically.",
    "Python's `inspect.signature` gives a function's parameter list programmatically.",
    "Linux `strace -p PID` attaches to a running process and shows every system call.",
    "`curl --resolve host:443:IP URL` tests a specific backend without changing DNS.",
    "In Python, `__enter__` and `__exit__` on any class makes it a context manager.",
    "PostgreSQL partial indexes (`WHERE condition`) are smaller and faster than full-column ones.",
    "CSS `font-display: swap` shows a fallback font immediately while web fonts load.",
    "Python's `concurrent.futures.ProcessPoolExecutor` bypasses the GIL for CPU-bound work.",
    "`git diff main...feature` shows only commits unique to `feature` since it diverged.",
    "In Python, `dataclasses.asdict` deep-converts a dataclass to a plain dict recursively.",
    "Linux `journalctl -u service --since '10 minutes ago'` tails a systemd log by time.",
    "HTTP `ETag` + `If-None-Match` enables conditional GET — 304 if unchanged.",
    "Python's `ast.parse` turns source code into an AST — useful for static analysis.",
    "`docker buildx build --platform linux/arm64,linux/amd64 .` builds multi-arch images.",
    "PostgreSQL `pg_trgm` enables fuzzy text search with trigram-based similarity.",
    "CSS `@layer` (cascade layers) gives explicit control over specificity ordering.",
    "Python's `multiprocessing.Pool.imap_unordered` yields results as they complete, not in order.",
    "In Python, `__bytes__` defines the `bytes()` conversion for custom objects.",
    "Git `reflog` is your safety net — it records every HEAD change for 90 days.",
    "Python's `functools.singledispatch` enables function overloading by first-argument type.",
    "`jq '.[].name' data.json` is the go-to for quick CLI JSON field extraction.",
    "In PostgreSQL, `WITH RECURSIVE` enables hierarchical/tree queries in pure SQL.",
    "Python's `operator` module has `itemgetter`, `attrgetter` for clean sort keys.",
    "The `SIGTERM` signal is a polite 'please stop'; `SIGKILL` cannot be caught or ignored.",
    "CSS `gap` works for both `grid` and `flex` containers since Chrome 84 / Firefox 63.",
    "Python's `io.StringIO` wraps a string as a file-like object — great for testing parsers.",
    "`git show HEAD:path/to/file` reads a file at a specific commit without checking it out.",
    "In Python, `__format__` lets you define custom format specs: `f'{obj:myspec}'`.",
    "PostgreSQL `gen_random_uuid()` generates UUID v4 natively since 13.",
    "Linux `watch -n 1 'command'` re-runs a command every second — poor man's monitoring.",
    "Python's `pathlib.Path` is cross-platform; never manually join paths with string concatenation.",
    "HTTP `103 Early Hints` lets servers push Link headers before the main response.",
    "In Python, `defaultdict(lambda: defaultdict(int))` creates auto-nested dicts cleanly.",
    "`git tag -a v1.0 -m 'message'` creates an annotated tag with a message and tagger info.",
    "CSS `subgrid` (now widely supported) lets nested elements align to the parent's grid tracks.",
    "Python's `datetime.timezone.utc` is the preferred way to create tz-aware UTC datetimes.",
]

# ── SNIPPET POOL ─────────────────────────────────────────────────────────────

_SNIPPET_POOL = {
    'string_utils': [
        ('slugify', '''
import re


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return re.sub(r'^-+|-+$', '', text)
'''),
        ('truncate', '''
def truncate(text, max_len, suffix='...'):
    """Truncate text to max_len, appending suffix if cut."""
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix
'''),
        ('camel_to_snake', '''
import re


def camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
'''),
        ('snake_to_camel', '''
def snake_to_camel(name, upper=False):
    """Convert snake_case to camelCase or PascalCase."""
    parts = name.split('_')
    if upper:
        return ''.join(p.capitalize() for p in parts)
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])
'''),
        ('chunk_list', '''
def chunk_list(lst, size):
    """Split a list into chunks of given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]
'''),
        ('flatten', '''
def flatten(nested, depth=None):
    """Flatten nested list to given depth (None = fully flat)."""
    result = []
    for item in nested:
        if isinstance(item, (list, tuple)) and depth != 0:
            result.extend(flatten(item, None if depth is None else depth - 1))
        else:
            result.append(item)
    return result
'''),
        ('memoize', '''
def memoize(func):
    """Simple memoization decorator using a dict cache."""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper
'''),
        ('parse_size', '''
def parse_size(size_str):
    """Parse human-readable size to bytes. '1.5 MB' -> 1572864."""
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
    s = size_str.strip().upper()
    for unit, mult in sorted(units.items(), key=lambda x: -x[1]):
        if s.endswith(unit):
            return int(float(s[:-len(unit)].strip()) * mult)
    return int(s)
'''),
        ('format_bytes', '''
def format_bytes(num_bytes, precision=2):
    """Format bytes as human-readable. 1572864 -> '1.50 MB'."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(num_bytes) < 1024:
            return f'{num_bytes:.{precision}f} {unit}'
        num_bytes /= 1024
    return f'{num_bytes:.{precision}f} PB'
'''),
        ('dedupe', '''
def dedupe(items, key=None):
    """Remove duplicates preserving order. key: optional transform fn."""
    seen = set()
    result = []
    for item in items:
        k = key(item) if key else item
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result
'''),
    ],
    'file_utils': [
        ('safe_read', '''
def safe_read(path, encoding='utf-8', default=None):
    """Read a file, returning default if missing or unreadable."""
    try:
        with open(path, encoding=encoding) as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return default
'''),
        ('walk_files', '''
from pathlib import Path


def walk_files(directory, pattern='*', recursive=True):
    """Yield file paths matching pattern under directory."""
    root = Path(directory)
    yield from (root.rglob if recursive else root.glob)(pattern)
'''),
        ('hash_file', '''
import hashlib


def hash_file(path, algorithm='sha256', chunk_size=65536):
    """Return hex digest of file. Streams to handle large files."""
    h = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()
'''),
        ('retry', '''
import time
import functools


def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Decorator that retries a function on specified exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay * (2 ** attempt))
        return wrapper
    return decorator
'''),
        ('deep_merge', '''
def deep_merge(base, override):
    """Recursively merge override dict into base. Returns new dict."""
    result = base.copy()
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result
'''),
        ('atomic_write', '''
import os
import tempfile


def atomic_write(path, content, encoding='utf-8'):
    """Write file atomically via temp + rename. Prevents partial writes."""
    dirpath = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(dir=dirpath)
    try:
        with os.fdopen(fd, 'w', encoding=encoding) as f:
            f.write(content)
        os.replace(tmp, path)
    except Exception:
        os.unlink(tmp)
        raise
'''),
    ],
    'datetime_utils': [
        ('humanize_delta', '''
def humanize_delta(seconds):
    """Convert seconds to human-readable. 3661 -> '1h 1m 1s'."""
    parts = []
    for unit, size in [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]:
        if seconds >= size:
            parts.append(f'{int(seconds // size)}{unit}')
            seconds %= size
    return ' '.join(parts) if parts else '0s'
'''),
        ('week_number', '''
from datetime import date


def week_number(dt=None):
    """Return ISO week number for a date (default: today)."""
    if dt is None:
        dt = date.today()
    return dt.isocalendar()[1]
'''),
        ('is_business_day', '''
from datetime import date


def is_business_day(dt=None):
    """True if the date is Mon–Fri (no holiday calendar)."""
    if dt is None:
        dt = date.today()
    return dt.weekday() < 5
'''),
        ('next_business_day', '''
from datetime import date, timedelta


def next_business_day(dt=None):
    """Return the next weekday after the given date."""
    if dt is None:
        dt = date.today()
    dt += timedelta(days=1)
    while dt.weekday() >= 5:
        dt += timedelta(days=1)
    return dt
'''),
        ('date_range', '''
from datetime import timedelta


def date_range(start, end, inclusive=True):
    """Yield dates from start to end. Both are date objects."""
    current = start
    while current < end or (inclusive and current == end):
        yield current
        current += timedelta(days=1)
'''),
        ('parse_date_flexible', '''
from datetime import datetime


def parse_date_flexible(text):
    """Try multiple date formats. Returns a date object or None."""
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%B %d, %Y', '%b %d, %Y']
    for fmt in formats:
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            continue
    return None
'''),
    ],
    'cli_utils': [
        ('progress_bar', '''
import sys


def progress_bar(current, total, width=40, prefix='', suffix=''):
    """Print an inline ASCII progress bar to stdout."""
    filled = int(width * current / max(total, 1))
    bar = '=' * filled + '-' * (width - filled)
    pct = int(100 * current / max(total, 1))
    sys.stdout.write(f'\r{prefix}[{bar}] {pct:3d}% {suffix}')
    sys.stdout.flush()
    if current >= total:
        print()
'''),
        ('color_print', '''
def color_print(text, color='reset', bold=False):
    """Print colored text using ANSI escape codes."""
    codes = {'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
             'magenta': 35, 'cyan': 36, 'white': 37, 'reset': 0}
    code = codes.get(color, 0)
    prefix = f'\033[{"1;" if bold else ""}{code}m'
    print(f'{prefix}{text}\033[0m')
'''),
        ('table_print', '''
def table_print(rows, headers=None, min_width=3):
    """Print a list of dicts or tuples as a formatted ASCII table."""
    if not rows:
        return
    if isinstance(rows[0], dict):
        if headers is None:
            headers = list(rows[0].keys())
        data = [[str(row.get(h, '')) for h in headers] for row in rows]
    else:
        data = [[str(c) for c in row] for row in rows]
        if headers is None:
            headers = [f'Col{i}' for i in range(len(data[0]))]
    widths = [max(min_width, len(h), *(len(r[i]) for r in data)) for i, h in enumerate(headers)]
    fmt = '  '.join(f'{{:<{w}}}' for w in widths)
    print(fmt.format(*headers))
    print('  '.join('-' * w for w in widths))
    for row in data:
        print(fmt.format(*row))
'''),
        ('confirm_prompt', '''
def confirm_prompt(message, default=False):
    """Ask user a yes/no question. Returns bool."""
    hint = '[Y/n]' if default else '[y/N]'
    try:
        answer = input(f'{message} {hint}: ').strip().lower()
    except (KeyboardInterrupt, EOFError):
        return False
    return (answer in ('y', 'yes')) if answer else default
'''),
        ('spinner', '''
import sys
import itertools
import threading
import time


class Spinner:
    """Terminal spinner as a context manager."""

    def __init__(self, message='Working'):
        self.message = message
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._spin, daemon=True)

    def _spin(self):
        for ch in itertools.cycle(r'|/-\\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'\r{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'\r{self.message} done\n')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()
'''),
    ],
}


# ── HELPERS ──────────────────────────────────────────────────────────────────

def _existing_definitions(file_path):
    """Return set of def/class names already in a Python file."""
    if not os.path.exists(file_path):
        return set()
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
    return set(re.findall(r'^(?:def|class)\s+(\w+)', content, re.MULTILINE))


def _read_or_empty(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return f.read()
    return ''


# ── PLOT GENERATORS ──────────────────────────────────────────────────────────

_FILE_MAP = {
    'sorting': 'algorithms/sorting.py',
    'graphs': 'algorithms/graphs.py',
    'trees': 'algorithms/trees.py',
    'dp': 'algorithms/dp.py',
    'strings': 'algorithms/strings.py',
}

_SNIPPET_FILE_MAP = {
    'string_utils': 'snippets/string_utils.py',
    'file_utils': 'snippets/file_utils.py',
    'datetime_utils': 'snippets/datetime_utils.py',
    'cli_utils': 'snippets/cli_utils.py',
}


def _gen_algorithm(target_date: date, index: int):
    rng = random.Random(_daily_seed(target_date, index * 3001))
    categories = list(_ALGORITHM_POOL.keys())
    rng.shuffle(categories)
    for cat in categories:
        fpath = _FILE_MAP[cat]
        existing = _existing_definitions(fpath)
        candidates = [(n, c) for n, c in _ALGORITHM_POOL[cat] if n not in existing]
        if candidates:
            name, code = rng.choice(candidates)
            return fpath, _read_or_empty(fpath) + '\n' + code.strip() + '\n'
    # All implemented — add a revisit comment
    cat = rng.choice(categories)
    fpath = _FILE_MAP[cat]
    name, code = rng.choice(_ALGORITHM_POOL[cat])
    suffix = f'\n\n# variant: {name}\n' + code.strip() + '\n'
    return fpath, _read_or_empty(fpath) + suffix


def _gen_snippets(target_date: date, index: int, dry_run: bool = False):
    rng = random.Random(_daily_seed(target_date, index * 2003))
    modules = list(_SNIPPET_POOL.keys())
    rng.shuffle(modules)
    for mod in modules:
        fpath = _SNIPPET_FILE_MAP[mod]
        existing = _existing_definitions(fpath)
        candidates = [(n, c) for n, c in _SNIPPET_POOL[mod] if n not in existing]
        if candidates:
            name, code = rng.choice(candidates)
            content = _read_or_empty(fpath) + '\n' + code.strip() + '\n'
            if not dry_run:
                _update_index(mod, name)
            return fpath, content
    mod = rng.choice(modules)
    fpath = _SNIPPET_FILE_MAP[mod]
    name, code = rng.choice(_SNIPPET_POOL[mod])
    return fpath, _read_or_empty(fpath) + '\n# re-export\n' + code.strip() + '\n'


def _update_index(module, name):
    index_path = 'snippets/index.yml'
    existing = _read_or_empty(index_path)
    if name not in existing:
        with open(index_path, 'a', encoding='utf-8') as f:
            f.write(f'- name: {name}\n  module: {module}.py\n')


def _gen_logs(target_date: date, index: int):
    rng = random.Random(_daily_seed(target_date, index * 1009))
    entry = rng.choice(_TIL_ENTRIES)
    month_file = f'logs/{target_date.strftime("%Y-%m")}.md'
    timestamp = target_date.isoformat()
    tag = rng.choice(['#til', '#note', '#python', '#git', '#linux', '#sql', '#web', '#perf'])
    new_entry = f'\n## {timestamp} {tag}\n\n{entry}\n'
    return month_file, _read_or_empty(month_file) + new_entry


def _gen_stats(target_date: date, index: int):
    stats_file = 'stats/garden.json'
    stats = {
        'total_commits': 0, 'current_streak': 0, 'longest_streak': 0,
        'last_commit_date': None,
        'by_plot': {'algorithms': 0, 'snippets': 0, 'logs': 0, 'stats': 0},
        'by_month': {},
    }
    if os.path.exists(stats_file):
        try:
            with open(stats_file, encoding='utf-8') as f:
                stats = json.load(f)
        except (json.JSONDecodeError, KeyError):
            pass

    stats['total_commits'] = stats.get('total_commits', 0) + 1
    stats.setdefault('by_plot', {})['stats'] = stats['by_plot'].get('stats', 0) + 1
    month_key = target_date.strftime('%Y-%m')
    stats.setdefault('by_month', {})[month_key] = stats['by_month'].get(month_key, 0) + 1

    last = stats.get('last_commit_date')
    if last:
        try:
            last_date = date.fromisoformat(last)
            if target_date - last_date == timedelta(days=1):
                stats['current_streak'] = stats.get('current_streak', 0) + 1
            elif target_date > last_date:
                stats['current_streak'] = 1
        except ValueError:
            stats['current_streak'] = 1
    else:
        stats['current_streak'] = 1
    stats['longest_streak'] = max(stats.get('longest_streak', 0), stats['current_streak'])
    stats['last_commit_date'] = target_date.isoformat()

    os.makedirs('stats', exist_ok=True)
    with open('stats/README.md', 'w', encoding='utf-8') as f:
        f.write(_stats_readme(stats, target_date))

    return stats_file, json.dumps(stats, indent=2)


def _stats_readme(stats, target_date):
    total = stats.get('total_commits', 0)
    streak = stats.get('current_streak', 0)
    longest = stats.get('longest_streak', 0)
    by_plot = stats.get('by_plot', {})
    by_month = stats.get('by_month', {})
    bars = ''
    if by_month:
        max_v = max(by_month.values(), default=1)
        for month, count in sorted(by_month.items())[-6:]:
            bar = int(20 * count / max_v)
            bars += f'  {month}  {"█" * bar} {count}\n'
    return f"""# Garden Stats

> Updated: {target_date.isoformat()}

| Metric | Value |
|--------|-------|
| Total Commits | {total} |
| Current Streak | {streak} days |
| Longest Streak | {longest} days |

## By Plot

| Plot | Commits |
|------|---------|
| Algorithms | {by_plot.get('algorithms', 0)} |
| Snippets | {by_plot.get('snippets', 0)} |
| Logs | {by_plot.get('logs', 0)} |
| Stats | {by_plot.get('stats', 0)} |

## Monthly Activity

```
{bars.rstrip()}
```
"""


# ── PUBLIC API ───────────────────────────────────────────────────────────────

def generate_content(plot: str, target_date: date = None, index: int = 0, dry_run: bool = False):
    """Return (file_path, content) for the given plot."""
    if target_date is None:
        target_date = date.today()
    if plot == 'algorithms':
        return _gen_algorithm(target_date, index)
    elif plot == 'snippets':
        return _gen_snippets(target_date, index, dry_run=dry_run)
    elif plot == 'logs':
        return _gen_logs(target_date, index)
    elif plot == 'stats':
        return _gen_stats(target_date, index)
    return _gen_logs(target_date, index)
