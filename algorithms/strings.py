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
