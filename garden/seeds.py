import hashlib
import random
from datetime import date, datetime, timedelta

HOUR_BASES = [3, 7, 11, 14, 18]
_GARDEN_FRAC = 0.70

# Week-score system — drives the "burst and gap" pattern seen in real graphs.
# Each week is independently scored:
#   0 = quiet  (30%) — whole week empty, large grey stretches
#   1 = light  (32%) — 2-3 active days, low commit counts
#   2 = active (26%) — 4-5 active days, moderate counts
#   3 = burst  (12%) — almost all days, higher counts
# This produces visible clusters of green separated by empty gaps.


def daily_seed(target_date: date) -> int:
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def _week_seed(target_date: date) -> int:
    iso_year, iso_week, _ = target_date.isocalendar()
    key = f'{iso_year}-w{iso_week:02d}'
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)


def _week_score(target_date: date) -> int:
    """Activity level for this ISO week. Same score for every day of the week."""
    rng = random.Random(_week_seed(target_date))
    r = rng.random()
    if r < 0.30: return 0   # quiet  30%
    if r < 0.62: return 1   # light  32%
    if r < 0.88: return 2   # active 26%
    return 3                 # burst  12%


def is_rest_day(target_date: date) -> bool:
    score = _week_score(target_date)
    if score == 0:
        return True  # entire quiet week = all grey squares
    rest_prob = {1: 0.60, 2: 0.30, 3: 0.12}[score]
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < rest_prob


def _day_budget(target_date: date) -> int:
    """Total commits for the day across ALL repos combined."""
    if is_rest_day(target_date):
        return 0
    score = _week_score(target_date)
    weekday = target_date.weekday()
    weekend = weekday >= 5

    # Lower ranges on weekends, higher mid-week
    ranges = {
        1: (1, 2) if weekend else (1, 3),
        2: (1, 3) if weekend else (2, 6),
        3: (2, 4) if weekend else (4, 9),
    }
    lo, hi = ranges[score]
    rng = random.Random(daily_seed(target_date) + 88881)
    return rng.randint(lo, hi)


def garden_daily_total(target_date: date) -> int:
    """70% of day budget handled by garden.yml's 5 cron triggers."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return max(1, round(budget * _GARDEN_FRAC))


def multi_repo_daily_total(target_date: date) -> int:
    """30% of day budget handled by multi_repo.yml across other repos."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return budget - garden_daily_total(target_date)


def _trigger_share(target_date: date, run_number: int) -> int:
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
    if target_date is None:
        target_date = date.today()
    rng = random.Random(daily_seed(target_date) + base_hour * 997)
    offset_minutes = rng.randint(-20, 20)
    base = datetime(target_date.year, target_date.month, target_date.day, base_hour, 0)
    return base + timedelta(minutes=offset_minutes)
