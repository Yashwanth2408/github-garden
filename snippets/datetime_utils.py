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
