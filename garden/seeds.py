import hashlib
import random
from datetime import date, datetime, timedelta

HOUR_BASES = [3, 7, 11, 14, 18]
_GARDEN_FRAC = 0.70

# Seasonal activity weights — each calendar month gets a base activity level.
# Higher = more active/burst weeks that month; lower = mostly empty.
# This creates clear "busy periods" and "quiet stretches" across the year.
_SEASON = {
    1: 0.82,   # Jan — productive, post-holiday grind
    2: 0.78,   # Feb — active
    3: 0.72,   # Mar — still strong
    4: 0.50,   # Apr — slowing down
    5: 0.42,   # May — lighter
    6: 0.25,   # Jun — summer begins, sparsely active
    7: 0.12,   # Jul — summer break, mostly empty
    8: 0.18,   # Aug — still quiet
    9: 0.48,   # Sep — back to work
    10: 0.65,  # Oct — picking up
    11: 0.72,  # Nov — productive
    12: 0.58,  # Dec — active then holiday tail-off
}


def daily_seed(target_date: date) -> int:
    return int(hashlib.md5(str(target_date).encode()).hexdigest(), 16) % (2 ** 32)


def _week_seed(target_date: date) -> int:
    iso_year, iso_week, _ = target_date.isocalendar()
    key = f'{iso_year}-w{iso_week:02d}'
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)


def _week_score(target_date: date) -> int:
    """Week-level activity score 0-3.
    Quiet probability is inverse of the month's season weight,
    so summer months are mostly 0 (empty) and winter months
    have more 2s and 3s (active/burst)."""
    season = _SEASON[target_date.month]
    rng = random.Random(_week_seed(target_date))
    r = rng.random()

    quiet_p = 1.0 - season          # e.g. Jul: 88% quiet, Jan: 18% quiet
    if r < quiet_p:
        return 0                    # entire week empty

    # Distribute remaining probability across scores 1-3
    r2 = (r - quiet_p) / (1.0 - quiet_p)
    if r2 < 0.45: return 1          # light  — 45% of non-quiet weeks
    if r2 < 0.80: return 2          # active — 35%
    return 3                        # burst  — 20%


def is_rest_day(target_date: date) -> bool:
    """True when this specific day has 0 commits.
    Quiet weeks = all days rest. Within active weeks, some days still skip."""
    score = _week_score(target_date)
    if score == 0:
        return True
    # Day-level rest probability (higher score = fewer rest days within week)
    rest_prob = {1: 0.62, 2: 0.32, 3: 0.14}[score]
    rng = random.Random(daily_seed(target_date) + 999983)
    return rng.random() < rest_prob


def _day_budget(target_date: date) -> int:
    """Total commits for the day across all repos combined."""
    if is_rest_day(target_date):
        return 0
    score = _week_score(target_date)
    weekday = target_date.weekday()
    weekend = weekday >= 5

    # Wider spread between scores so GitHub shows distinct colour shades:
    # score-1 days → light green, score-3 burst days → bright green
    ranges = {
        1: (1, 2) if weekend else (1, 3),
        2: (1, 3) if weekend else (3, 7),
        3: (3, 5) if weekend else (6, 12),
    }
    lo, hi = ranges[score]
    rng = random.Random(daily_seed(target_date) + 88881)
    return rng.randint(lo, hi)


def garden_daily_total(target_date: date) -> int:
    """70% of day budget — handled by garden.yml's 5 cron triggers."""
    budget = _day_budget(target_date)
    if budget == 0:
        return 0
    return max(1, round(budget * _GARDEN_FRAC))


def multi_repo_daily_total(target_date: date) -> int:
    """30% of day budget — handled by multi_repo.yml across other repos."""
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
