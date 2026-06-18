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
