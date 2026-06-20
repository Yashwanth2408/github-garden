import hashlib
import random
from datetime import date, datetime, timedelta

# UTC trigger hours (IST = UTC + 5:30)
HOUR_BASES = [3, 7, 11, 14, 18]

# Shade thresholds (GitHub's 5-level scale):
#   Level 1 = 0 commits  (empty)
#   Level 2 = 1-3        (light green)
#   Level 3 = 4-8        (medium green)
#   Level 4 = 9-15       (dark green)
#   Level 5 = 16+        (bright green)

# Daily commit budget sequence — 7 slots for 7 days, ordered HIGH → LOW.
# Each week this sequence rotates so no day is always the peak.
# Distribution is always: 2×L5, 1×L4, 2×L3, 2×L2 per week.
_LEVEL_SEQ = [
    (6, 9),    # slot 0 — peak-high  (bright green)
    (5, 8),    # slot 1 — peak-low   (bright green)
    (3, 6),    # slot 2 — high       (dark green)
    (2, 4),    # slot 3 — medium     (medium green)
    (2, 3),    # slot 4 — medium-low (medium green)
    (1, 2),    # slot 5 — light      (light green)
    (1, 1),    # slot 6 — minimal    (light green)
]

# 70% of the daily budget goes to garden.yml (5 triggers).
# 30% goes to multi_repo.yml (2 triggers across other repos).
# Both workflows read the same budget — together they hit the target.
_GARDEN_FRAC = 0.70


def daily_seed(target_date: date) -> int:
    """Deterministic seed — same date always produces same pattern."""
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def is_rest_day(target_date: date) -> bool:
    """~35% of days = 0 commits (~10 per month) — keeps graph realistic.
    Day-level decision so garden + multi_repo both skip."""
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < 0.35


def _day_budget(target_date: date) -> int:
    """Total commits planned for the entire day (garden + other repos combined).
    The level sequence rotates each week so the peak days shift around."""
    if is_rest_day(target_date):
        return 0
    iso_week = target_date.isocalendar()[1]
    rotation = iso_week % 7
    slot = (target_date.weekday() + rotation) % 7
    lo, hi = _LEVEL_SEQ[slot]
    rng = random.Random(daily_seed(target_date) + 88881)
    return rng.randint(lo, hi)


def garden_daily_total(target_date: date) -> int:
    """How many commits garden.yml is responsible for today (≈70% of budget)."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return max(1, round(budget * _GARDEN_FRAC))


def multi_repo_daily_total(target_date: date) -> int:
    """How many commits multi_repo.yml is responsible for today (≈30% of budget)."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return budget - garden_daily_total(target_date)


def _trigger_share(target_date: date, run_number: int) -> int:
    """Split garden_daily_total across garden.yml's 5 triggers."""
    total = garden_daily_total(target_date)
    if total == 0:
        return 0
    base = total // 5
    remainder = total % 5
    return base + (1 if run_number < remainder else 0)


def should_commit(target_date: date = None, run_number: int = 0) -> bool:
    if target_date is None:
        target_date = date.today()
    return _trigger_share(target_date, run_number) > 0


def commit_count(target_date: date = None, run_number: int = 0) -> int:
    if target_date is None:
        target_date = date.today()
    return max(1, _trigger_share(target_date, run_number))


def choose_plot(target_date: date = None, commit_index: int = 0) -> str:
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + commit_index * 2503)
    plots = ['algorithms', 'snippets', 'logs', 'stats']
    weights = [35, 30, 25, 10]
    return rng.choices(plots, weights=weights)[0]


def timestamp_jitter(base_hour: int, target_date: date = None) -> datetime:
    """Realistic timestamp with ±20 min jitter around the trigger hour."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + base_hour * 997)
    offset_minutes = rng.randint(-20, 20)
    base = datetime(target_date.year, target_date.month, target_date.day, base_hour, 0)
    return base + timedelta(minutes=offset_minutes)
