# Tree algorithms — grown by the garden one function at a time

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

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

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

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)

def lowest_common_ancestor(root, p, q):
    """LCA in binary tree. O(n) time, O(h) space."""
    if root is None or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if (left and right) else (left or right)
