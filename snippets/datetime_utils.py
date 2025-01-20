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
