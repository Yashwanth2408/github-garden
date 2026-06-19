# String algorithms — grown by the garden one function at a time

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
