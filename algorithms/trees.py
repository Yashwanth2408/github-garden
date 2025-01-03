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
