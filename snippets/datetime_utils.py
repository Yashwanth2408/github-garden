# Datetime utilities — grown by the garden one function at a time

from datetime import datetime


def parse_date_flexible(text):
    """Try multiple date formats. Returns a date object or None."""
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%B %d, %Y', '%b %d, %Y']
    for fmt in formats:
        try:
            return datetime.strptime(text.strip(), fmt).date()
        except ValueError:
            continue
    return None

def humanize_delta(seconds):
    """Convert seconds to human-readable. 3661 -> '1h 1m 1s'."""
    parts = []
    for unit, size in [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]:
        if seconds >= size:
            parts.append(f'{int(seconds // size)}{unit}')
            seconds %= size
    return ' '.join(parts) if parts else '0s'

from datetime import date


def week_number(dt=None):
    """Return ISO week number for a date (default: today)."""
    if dt is None:
        dt = date.today()
    return dt.isocalendar()[1]

from datetime import timedelta


def date_range(start, end, inclusive=True):
    """Yield dates from start to end. Both are date objects."""
    current = start
    while current < end or (inclusive and current == end):
        yield current
        current += timedelta(days=1)

from datetime import date


def is_business_day(dt=None):
    """True if the date is Mon–Fri (no holiday calendar)."""
    if dt is None:
        dt = date.today()
    return dt.weekday() < 5

from datetime import date, timedelta


def next_business_day(dt=None):
    """Return the next weekday after the given date."""
    if dt is None:
        dt = date.today()
    dt += timedelta(days=1)
    while dt.weekday() >= 5:
        dt += timedelta(days=1)
    return dt
