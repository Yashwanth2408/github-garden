import hashlib
import random
from datetime import date as date_cls

_ALGO_NAMES = [
    "bubble sort", "merge sort", "quick sort", "heap sort", "insertion sort",
    "shell sort", "counting sort", "radix sort",
    "binary search", "linear search", "jump search", "interpolation search",
    "BFS traversal", "DFS traversal", "Dijkstra shortest path",
    "topological sort", "cycle detection", "union-find",
    "sliding window maximum", "two-pointer technique", "prefix sum",
    "KMP string matching", "Z-algorithm", "Rabin-Karp search",
    "LRU cache", "trie insertion", "trie search",
    "segment tree range query", "Kadane algorithm",
    "Floyd-Warshall", "Bellman-Ford", "Prim MST", "Kruskal MST",
    "binary heap", "red-black tree",
    "matrix chain multiplication", "longest common subsequence",
    "coin change", "0-1 knapsack", "edit distance",
    "longest palindromic substring", "valid brackets check",
    "level-order traversal", "tree serialization", "LCA",
]

_SNIPPET_NAMES = [
    ("slugify", "string_utils"),
    ("truncate", "string_utils"),
    ("camel_to_snake", "string_utils"),
    ("chunk_list", "string_utils"),
    ("flatten", "string_utils"),
    ("memoize", "string_utils"),
    ("parse_size", "string_utils"),
    ("format_bytes", "string_utils"),
    ("safe_read", "file_utils"),
    ("walk_files", "file_utils"),
    ("hash_file", "file_utils"),
    ("retry", "file_utils"),
    ("deep_merge", "file_utils"),
    ("atomic_write", "file_utils"),
    ("humanize_delta", "datetime_utils"),
    ("week_number", "datetime_utils"),
    ("is_business_day", "datetime_utils"),
    ("next_business_day", "datetime_utils"),
    ("date_range", "datetime_utils"),
    ("parse_date_flexible", "datetime_utils"),
    ("progress_bar", "cli_utils"),
    ("color_print", "cli_utils"),
    ("table_print", "cli_utils"),
    ("confirm_prompt", "cli_utils"),
    ("spinner", "cli_utils"),
]

_TEMPLATES = {
    'algorithms': [
        "add {algo} implementation",
        "implement {algo} with test cases",
        "refactor {algo}: improve time complexity",
        "add edge case handling to {algo}",
        "feat: add {algo} to algorithms library",
        "optimize {algo} space complexity",
        "docs: add complexity analysis to {algo}",
        "add iterative version of {algo}",
        "implement {algo} with early termination",
        "fix: correct off-by-one in {algo}",
        "add {algo} with custom comparator support",
        "improve readability of {algo}",
    ],
    'snippets': [
        "add {name} utility function",
        "add {name} helper to {module}",
        "feat: implement {name}",
        "add type hints to {name}",
        "improve error handling in {name}",
        "add docstring to {name}",
        "expand {module}: add {name}",
        "chore: add {name} to snippets library",
        "utils: implement {name}",
        "refactor: clean up {module} utilities",
        "chore: update snippets index",
    ],
    'logs': [
        "notes: {date} dev log",
        "docs: add {date} notes",
        "journal: learning notes for {date}",
        "update dev log",
        "chore: add daily notes",
        "log: {date} session notes",
        "docs: {date} TIL entry",
        "add notes for {date}",
        "chore: update learning log",
        "log: weekly notes update",
        "docs: append dev journal",
        "notes: checkpoint {date}",
        "chore: log daily learnings",
    ],
    'stats': [
        "chore: update garden stats",
        "stats: daily metrics update",
        "chore: sync contribution stats",
        "update README dashboard",
        "stats: refresh streak counter",
        "chore: daily stats sync",
        "update garden metrics",
        "chore: regenerate stats dashboard",
    ],
    'general': [
        "chore: minor cleanup",
        "fix: correct typo in docs",
        "refactor: simplify logic",
        "docs: improve comments",
        "style: formatting",
        "chore: housekeeping",
        "fix: remove debug leftover",
        "refactor: rename for clarity",
        "chore: update .gitignore",
        "docs: update README",
        "fix: edge case handling",
        "chore: code organization",
        "style: consistent naming",
        "refactor: extract helper",
        "docs: add usage examples",
        "fix: handle empty input",
        "refactor: reduce nesting",
        "chore: remove unused imports",
        "docs: clarify description",
    ],
}


def _daily_seed(target_date: date_cls) -> int:
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def pick_message(plot: str, target_date: date_cls = None, index: int = 0) -> str:
    """Pick a commit message for the given plot, deterministically seeded."""
    if target_date is None:
        target_date = date_cls.today()
    rng = random.Random(_daily_seed(target_date) + index * 4001 + abs(hash(plot)) % 10000)
    templates = _TEMPLATES.get(plot, _TEMPLATES['general'])
    template = rng.choice(templates)
    if '{algo}' in template:
        template = template.replace('{algo}', rng.choice(_ALGO_NAMES))
    if '{name}' in template or '{module}' in template:
        name, module = rng.choice(_SNIPPET_NAMES)
        template = template.replace('{name}', name).replace('{module}', module)
    if '{date}' in template:
        template = template.replace('{date}', target_date.isoformat())
    return template
