import hashlib
import random
from datetime import date, datetime, timedelta

# Mon=1.0, Tue=1.1, Wed=1.3, Thu=1.2, Fri=1.0, Sat=0.45, Sun=0.35
DAY_WEIGHT = [1.0, 1.1, 1.3, 1.2, 1.0, 0.45, 0.35]

HOUR_BASES = [9, 12, 15, 18, 21]

# Target: 25-35 commits/day on weekdays, 8-12 on weekends
# avg ~5.4 per trigger × 5 triggers × ~92% weekday fire rate = ~25/day
COUNT_CHOICES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
COUNT_WEIGHTS = [5, 10, 16, 22, 22, 13, 7, 3, 2]


def daily_seed(target_date: date) -> int:
    """Deterministic seed from a date — same date always gives same base pattern."""
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def should_commit(target_date: date = None, run_number: int = 0) -> bool:
    """
    Skip oracle. Returns True if this trigger should produce a commit.

    Uses day-of-week weighting + occasional rest days (~1.5/month).
    The seed is deterministic per (date, run_number) for reproducibility.
    """
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + run_number * 7919)
    # ~4% rest chance per trigger → ~1.5 full rest days/month
    if rng.random() < 0.04:
        return False
    day_w = DAY_WEIGHT[target_date.weekday()]
    skip_chance = 1.0 - (day_w * 0.92)  # weekdays: ~8% skip · weekends: ~58-68% skip
    return rng.random() > skip_chance


def commit_count(target_date: date = None, run_number: int = 0) -> int:
    """How many commits to make when committing. Weighted toward 1-2."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + run_number * 1337)
    return rng.choices(COUNT_CHOICES, weights=COUNT_WEIGHTS)[0]


def choose_plot(target_date: date = None, commit_index: int = 0) -> str:
    """Which content plot to use. Rotates with weighted randomness."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + commit_index * 2503)
    plots = ['algorithms', 'snippets', 'logs', 'stats']
    weights = [35, 30, 25, 10]
    return rng.choices(plots, weights=weights)[0]


def timestamp_jitter(base_hour: int, target_date: date = None) -> datetime:
    """Returns a realistic datetime with ±25 min jitter around the base hour."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + base_hour * 997)
    offset_minutes = rng.randint(-25, 25)
    base = datetime(target_date.year, target_date.month, target_date.day, base_hour, 0)
    return base + timedelta(minutes=offset_minutes)
