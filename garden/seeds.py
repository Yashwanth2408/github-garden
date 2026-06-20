import hashlib
import random
from datetime import date, datetime, timedelta

# UTC trigger hours (IST = UTC + 5:30)
# 3:30 UTC = 9:00 AM IST  |  7:00 = 12:30 PM  |  11:30 = 5:00 PM
# 14:00 = 7:30 PM IST     |  18:00 = 11:30 PM IST
HOUR_BASES = [3, 7, 11, 14, 18]

# Daily commit budget by weekday — controls which level each day lands on:
# Level 1 = 0  |  Level 2 = 1-11  |  Level 3 = 12-17
# Level 4 = 18-24  |  Level 5 = 25+
_DAY_RANGES = {
    0: (13, 17),   # Mon  → Level 3
    1: (18, 24),   # Tue  → Level 4
    2: (26, 34),   # Wed  → Level 5 (peak)
    3: (22, 28),   # Thu  → Level 5
    4: (12, 16),   # Fri  → Level 3
    5: (5, 11),    # Sat  → Level 2
    6: (2, 7),     # Sun  → Level 2 (low)
}


def daily_seed(target_date: date) -> int:
    """Deterministic seed — same date always produces same pattern."""
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def is_rest_day(target_date: date) -> bool:
    """~7% of days are 0-commit rest days → roughly 2 per month.
    Decision is day-level so ALL 5 triggers agree on the same rest day."""
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < 0.07


def _day_budget(target_date: date) -> int:
    """Total commits for the entire day. 0 on rest days."""
    if is_rest_day(target_date):
        return 0
    rng = random.Random(daily_seed(target_date) + 88881)
    lo, hi = _DAY_RANGES[target_date.weekday()]
    return rng.randint(lo, hi)


def _trigger_share(target_date: date, run_number: int) -> int:
    """Splits the day budget cleanly across 5 triggers (run_number 0-4).
    Each trigger gets floor(budget/5), first (budget%5) triggers get +1."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    base = budget // 5
    remainder = budget % 5
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
