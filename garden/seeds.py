import hashlib
import random
from datetime import date, datetime, timedelta

# Mon=1.0, Tue=1.1, Wed=1.2, Thu=1.1, Fri=0.9, Sat=0.55, Sun=0.50
DAY_WEIGHT = [1.0, 1.1, 1.2, 1.1, 0.9, 0.55, 0.50]

HOUR_BASES = [9, 12, 15, 18, 21]

COUNT_CHOICES = [1, 2, 3, 4, 5]
COUNT_WEIGHTS = [40, 30, 20, 7, 3]


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
    # ~6% chance per trigger of a full rest — accumulates to ~1.5 skip-days/month
    if rng.random() < 0.06:
        return False
    day_w = DAY_WEIGHT[target_date.weekday()]
    skip_chance = 1.0 - (day_w * 0.7)  # ranges 0.35 (Wed) to 0.65 (Sun)
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
