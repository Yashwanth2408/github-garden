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

def parse_size(size_str):
    """Parse human-readable size to bytes. '1.5 MB' -> 1572864."""
    units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
    s = size_str.strip().upper()
    for unit, mult in sorted(units.items(), key=lambda x: -x[1]):
        if s.endswith(unit):
            return int(float(s[:-len(unit)].strip()) * mult)
    return int(s)

def chunk_list(lst, size):
    """Split a list into chunks of given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def format_bytes(num_bytes, precision=2):
    """Format bytes as human-readable. 1572864 -> '1.50 MB'."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(num_bytes) < 1024:
            return f'{num_bytes:.{precision}f} {unit}'
        num_bytes /= 1024
    return f'{num_bytes:.{precision}f} PB'

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
