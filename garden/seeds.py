import hashlib
import random
from datetime import date, datetime, timedelta

HOUR_BASES = [3, 7, 11, 14, 18]
_GARDEN_FRAC = 0.70

# Seasonal activity weight per calendar month.
# Higher = more active/burst weeks; lower = mostly quiet.
_SEASON = {
    1: 0.82,   # Jan — dense
    2: 0.78,   # Feb — active
    3: 0.72,   # Mar — active
    4: 0.55,   # Apr — moderate
    5: 0.48,   # May — lighter
    6: 0.42,   # Jun — sparse start of summer
    7: 0.35,   # Jul — summer quiet
    8: 0.38,   # Aug — quiet
    9: 0.55,   # Sep — back to work
    10: 0.65,  # Oct — picking up
    11: 0.72,  # Nov — productive
    12: 0.62,  # Dec — active
}


def daily_seed(target_date: date) -> int:
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def _week_seed(target_date: date) -> int:
    iso_year, iso_week, _ = target_date.isocalendar()
    key = f'{iso_year}-w{iso_week:02d}'
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)


def _month_seed_days(year: int, month: int) -> set:
    """Return a set of day-of-month ints that are guaranteed to have commits.
    Low-season months (summer) get 2-3 seeded days so there's always at least
    some visible green — prevents unlucky all-quiet months.
    High-season months get 0 seed days (natural activity is plentiful)."""
    season = _SEASON[month]
    if season >= 0.50:
        return set()   # Active months don't need a floor

    # Number of seed days scales inversely with season
    n = 3 if season < 0.40 else 2
    key = f'{year}-{month:02d}-seeddays'
    rng = random.Random(int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32))
    days = set()
    while len(days) < n:
        days.add(rng.randint(1, 28))   # day 1-28 always valid in any month
    return days


def _week_score(target_date: date) -> int:
    season = _SEASON[target_date.month]
    rng = random.Random(_week_seed(target_date))
    r = rng.random()
    quiet_p = 1.0 - season
    if r < quiet_p:
        return 0
    r2 = (r - quiet_p) / (1.0 - quiet_p)
    if r2 < 0.45: return 1
    if r2 < 0.80: return 2
    return 3


def is_rest_day(target_date: date) -> bool:
    # Seeded days are never rest days (guaranteed visible activity)
    if target_date.day in _month_seed_days(target_date.year, target_date.month):
        return False

    score = _week_score(target_date)
    if score == 0:
        return True
    rest_prob = {1: 0.62, 2: 0.32, 3: 0.14}[score]
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < rest_prob


def _day_budget(target_date: date) -> int:
    is_seed = target_date.day in _month_seed_days(target_date.year, target_date.month)
    score = _week_score(target_date)

    if score == 0 and is_seed:
        # Seed day in a quiet week: light activity (1-3 commits)
        rng = random.Random(daily_seed(target_date) + 55555)
        return rng.randint(1, 3)

    if is_rest_day(target_date):
        return 0

    weekday = target_date.weekday()
    weekend = weekday >= 5
    ranges = {
        1: (1, 2) if weekend else (1, 3),
        2: (1, 3) if weekend else (3, 7),
        3: (3, 5) if weekend else (6, 12),
    }
    lo, hi = ranges[score]
    rng = random.Random(daily_seed(target_date) + 88881)
    return rng.randint(lo, hi)


def garden_daily_total(target_date: date) -> int:
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return max(1, round(budget * _GARDEN_FRAC))


def multi_repo_daily_total(target_date: date) -> int:
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
