import hashlib
import random
from datetime import date, datetime, timedelta

# Mon=1.0, Tue=1.15, Wed=1.3, Thu=1.25, Fri=1.05, Sat=0.65, Sun=0.55
DAY_WEIGHT = [1.0, 1.15, 1.3, 1.25, 1.05, 0.65, 0.55]

HOUR_BASES = [9, 12, 15, 18, 21]

# Per-trigger commit counts — max mode: peaks at 15-25/day on weekdays,
# 4-8 on weekends, with realistic low days sprinkled in
COUNT_CHOICES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
COUNT_WEIGHTS = [5, 8, 12, 16, 18, 16, 12, 7, 4, 2]


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
    # ~3% rest chance on weekdays, ~8% on weekends → ~1 full rest day/month
    weekday = target_date.weekday()
    rest_chance = 0.03 if weekday < 5 else 0.08
    if rng.random() < rest_chance:
        return False
    day_w = DAY_WEIGHT[weekday]
    skip_chance = 1.0 - (day_w * 0.88)  # weekdays: ~12% skip · weekends: ~42% skip
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
