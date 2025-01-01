# File utilities — grown by the garden one function at a time

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

from pathlib import Path


def walk_files(directory, pattern='*', recursive=True):
    """Yield file paths matching pattern under directory."""
    root = Path(directory)
    yield from (root.rglob if recursive else root.glob)(pattern)
