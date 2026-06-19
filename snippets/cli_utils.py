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
