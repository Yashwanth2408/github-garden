#!/usr/bin/env python3
"""
water.py — The garden watering entrypoint.

Called by GitHub Actions 5x/day and locally for manual runs.

Usage:
  python garden/water.py              # normal daily run
  python garden/water.py --force      # skip the oracle, always commit
  python garden/water.py --dry-run    # print what would happen, no commits
  python garden/water.py --backfill   # read START_DATE/END_DATE from env
"""
import os
import sys
import subprocess
from datetime import date, timedelta

# Allow direct execution from repo root: python garden/water.py
sys.path.insert(0, os.path.dirname(__file__))

from seeds import should_commit, commit_count, choose_plot, timestamp_jitter, HOUR_BASES
from plots import generate_content
from messages import pick_message


def git(*args):
    result = subprocess.run(['git'] + list(args), capture_output=True, text=True)
    return result.stdout.strip(), result.returncode


def make_commit(target_date: date, commit_index: int, run_number: int, dry_run: bool = False):
    plot = choose_plot(target_date, commit_index)
    file_path, content = generate_content(plot, target_date, commit_index, dry_run=dry_run)
    message = pick_message(plot, target_date, commit_index)
    hour = HOUR_BASES[run_number % len(HOUR_BASES)]
    ts = timestamp_jitter(hour, target_date)
    ts_str = ts.strftime('%Y-%m-%dT%H:%M:%S')

    if dry_run:
        print(f'  [dry-run] {plot}: {file_path}')
        print(f'  [dry-run] message: "{message}"')
        print(f'  [dry-run] timestamp: {ts_str}')
        return True

    os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else '.', exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    git('add', file_path)

    # Also add snippets/index.yml if it was updated
    if plot == 'snippets' and os.path.exists('snippets/index.yml'):
        git('add', 'snippets/index.yml')

    # Also add stats/README.md if stats plot
    if plot == 'stats' and os.path.exists('stats/README.md'):
        git('add', 'stats/README.md')

    staged, _ = git('diff', '--staged', '--stat')
    if not staged:
        print(f'  no diff in {file_path}, skipping.')
        git('reset', 'HEAD', file_path)
        return False

    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = ts_str
    env['GIT_COMMITTER_DATE'] = ts_str
    result = subprocess.run(
        ['git', 'commit', '-m', message],
        env=env, capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f'  committed [{plot}]: {message}')
        return True
    else:
        print(f'  commit failed: {result.stderr.strip()}')
        return False


def run_for_date(target_date: date, run_number: int, force: bool, dry_run: bool):
    if not force and not should_commit(target_date, run_number):
        print(f'skip oracle: rest for {target_date} run#{run_number}')
        return 0

    count = commit_count(target_date, run_number)
    print(f'watering: {count} commit(s) for {target_date} (run#{run_number})')
    made = 0
    for i in range(count):
        if make_commit(target_date, i, run_number, dry_run):
            made += 1
    return made


def main():
    dry_run = '--dry-run' in sys.argv
    force = '--force' in sys.argv or os.getenv('FORCE_COMMIT', '').lower() == 'true'
    backfill_mode = '--backfill' in sys.argv or os.getenv('BACKFILL_MODE', '').lower() == 'true'

    if backfill_mode:
        start = date.fromisoformat(os.environ['START_DATE'])
        end = date.fromisoformat(os.environ['END_DATE'])
        total = 0
        current = start
        while current <= end:
            # Simulate all 5 daily triggers so the commit count matches the target level
            for rn in range(5):
                total += run_for_date(current, run_number=rn, force=False, dry_run=dry_run)
            current += timedelta(days=1)
        print(f'backfill done: {total} commits from {start} to {end}')
    else:
        backfill_date_str = os.getenv('BACKFILL_DATE', '').strip()
        if backfill_date_str:
            target_date = date.fromisoformat(backfill_date_str)
        else:
            target_date = date.today()

        # run_number 0-4 cycles through the 5 daily triggers
        run_number = int(os.getenv('GARDEN_SEED', '0')) % 5
        run_for_date(target_date, run_number, force, dry_run)


if __name__ == '__main__':
    main()
