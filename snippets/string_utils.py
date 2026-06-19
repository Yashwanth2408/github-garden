# String utilities — grown by the garden one function at a time

import re


def slugify(text):
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return re.sub(r'^-+|-+$', '', text)

def truncate(text, max_len, suffix='...'):
    """Truncate text to max_len, appending suffix if cut."""
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix

import re


def camel_to_snake(name):
    """Convert camelCase or PascalCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'_', name)
    return re.sub('([a-z0-9])([A-Z])', r'_', s1).lower()

def snake_to_camel(name, upper=False):
    """Convert snake_case to camelCase or PascalCase."""
    parts = name.split('_')
    if upper:
        return ''.join(p.capitalize() for p in parts)
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def flatten(nested, depth=None):
    """Flatten nested list to given depth (None = fully flat)."""
    result = []
    for item in nested:
        if isinstance(item, (list, tuple)) and depth != 0:
            result.extend(flatten(item, None if depth is None else depth - 1))
        else:
            result.append(item)
    return result
