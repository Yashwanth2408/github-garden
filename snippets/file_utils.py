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

import hashlib


def hash_file(path, algorithm='sha256', chunk_size=65536):
    """Return hex digest of file. Streams to handle large files."""
    h = hashlib.new(algorithm)
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def safe_read(path, encoding='utf-8', default=None):
    """Read a file, returning default if missing or unreadable."""
    try:
        with open(path, encoding=encoding) as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return default

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
