# CLI utilities — grown by the garden one function at a time

def color_print(text, color='reset', bold=False):
    """Print colored text using ANSI escape codes."""
    codes = {'red': 31, 'green': 32, 'yellow': 33, 'blue': 34,
             'magenta': 35, 'cyan': 36, 'white': 37, 'reset': 0}
    code = codes.get(color, 0)
    prefix = f'[{"1;" if bold else ""}{code}m'
    print(f'{prefix}{text}[0m')
