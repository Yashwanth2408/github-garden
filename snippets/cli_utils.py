# CLI utilities — grown by the garden one function at a time

def color_print(text, color='reset', bold=False):
    """Print colored text using ANSI escape codes."""
    codes = {'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
             'magenta': 35, 'cyan': 36, 'white': 37, 'reset': 0}
    code = codes.get(color, 0)
    prefix = f'[{"1;" if bold else ""}{code}m'
    print(f'{prefix}{text}[0m')

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

def confirm_prompt(message, default=False):
    """Ask user a yes/no question. Returns bool."""
    hint = '[Y/n]' if default else '[y/N]'
    try:
        answer = input(f'{message} {hint}: ').strip().lower()
    except (KeyboardInterrupt, EOFError):
        return False
    return (answer in ('y', 'yes')) if answer else default

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

import sys


def progress_bar(current, total, width=40, prefix='', suffix=''):
    """Print an inline ASCII progress bar to stdout."""
    filled = int(width * current / max(total, 1))
    bar = '=' * filled + '-' * (width - filled)
    pct = int(100 * current / max(total, 1))
    sys.stdout.write(f'
{prefix}[{bar}] {pct:3d}% {suffix}')
    sys.stdout.flush()
    if current >= total:
        print()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'
{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'
{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()

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
        for ch in itertools.cycle(r'|/-\'):
            if self._stop.is_set():
                break
            sys.stdout.write(f'{self.message} {ch}')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(f'{self.message} done
')

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *_):
        self._stop.set()
        self._thread.join()
