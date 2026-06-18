import hashlib
import random
from datetime import date, datetime, timedelta

# Day weights — controls how aggressively each day fires commits
# Mon=high, Tue-Thu=peak, Fri=medium-high, Sat=low, Sun=very low
DAY_WEIGHT = [1.0, 1.2, 1.3, 1.25, 1.05, 0.48, 0.35]

# UTC hours that map to realistic IST coding windows
# 3:30 UTC = 9:00 AM IST  |  7:00 = 12:30 PM  |  11:00 = 4:30 PM
# 14:30 = 8:00 PM IST     |  17:30 = 11:00 PM IST
HOUR_BASES = [3, 7, 11, 14, 17]

# Commits per trigger — avg ~5.4, produces:
#   Level 3 on slow triggers (2-3 commits × few triggers)
#   Level 4-5 on busy triggers (5-8 commits × all 5 triggers)
COUNT_CHOICES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
COUNT_WEIGHTS = [5, 10, 16, 22, 22, 13, 7, 3, 2]


def daily_seed(target_date: date) -> int:
    """Deterministic seed from date — same date always produces same base pattern."""
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def is_rest_day(target_date: date) -> bool:
    """~6% of all days are full 0-commit rest days (~1-2 per month).
    Decision is made at day level so all 5 triggers agree."""
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < 0.06


def should_commit(target_date: date = None, run_number: int = 0) -> bool:
    """Per-trigger commit oracle.
    Rest days always return False regardless of trigger."""
    if target_date is None:
        target_date = date.today()

    # Full rest day — no commits at all today
    if is_rest_day(target_date):
        return False

    rng = random.Random(daily_seed(target_date) + run_number * 7919)
    day_w = DAY_WEIGHT[target_date.weekday()]
    # weekdays: 8-16% skip chance | weekends: 52-68% skip chance
    skip_chance = max(0.0, 1.0 - (day_w * 0.92))
    return rng.random() > skip_chance


def commit_count(target_date: date = None, run_number: int = 0) -> int:
    """How many commits this trigger makes if it fires."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + run_number * 1337)
    return rng.choices(COUNT_CHOICES, weights=COUNT_WEIGHTS)[0]


def choose_plot(target_date: date = None, commit_index: int = 0) -> str:
    """Which content plot to use for this commit."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + commit_index * 2503)
    plots = ['algorithms', 'snippets', 'logs', 'stats']
    weights = [35, 30, 25, 10]
    return rng.choices(plots, weights=weights)[0]


def timestamp_jitter(base_hour: int, target_date: date = None) -> datetime:
    """Realistic commit timestamp with ±20 min jitter around the base hour."""
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + base_hour * 997)
    offset_minutes = rng.randint(-20, 20)
    base = datetime(target_date.year, target_date.month, target_date.day, base_hour, 0)
    return base + timedelta(minutes=offset_minutes)
