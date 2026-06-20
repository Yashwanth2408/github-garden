"""
Spreads the multi_repo portion of the daily commit budget across other GitHub
repos via the GitHub Contents API.

Budget logic (shared with seeds.py):
  daily_budget = total target commits for the day (determines shade level)
  garden.yml  → handles 70%  via 5 cron triggers
  multi_repo  → handles 30%  via 2 cron triggers (this script)

Together they hit the day's target so contribution colours are always correct.
Requires GH_PAT secret (classic PAT, repo scope) in the github-garden repo.
"""
import base64
import hashlib
import json
import os
import random
import sys
import urllib.request
import urllib.error
from datetime import date, datetime, timezone

# Import shared budget functions from seeds.py (same directory)
sys.path.insert(0, os.path.dirname(__file__))
from seeds import daily_seed, is_rest_day, multi_repo_daily_total

OWNER = 'Yashwanth2408'
COMMITTER = {
    'name': 'Yashwanth2408',
    'email': 'yashwanthbalaji.2408@gmail.com',
}

TARGET_REPOS = {
    f'{OWNER}/n8n-construction-agent': 'n8n',
    f'{OWNER}/yashwanth-portfolio':    'portfolio',
    f'{OWNER}/Yashwanth2408':          'profile',
}

# Realistic dev-log entries per repo type
_ENTRIES = {
    'n8n': [
        "explored webhook authentication patterns for incoming construction data",
        "added retry logic notes for HTTP request nodes under high load",
        "documented n8n credential scoping best practices for multi-env setup",
        "researched community nodes for GeoJSON and spatial data transformation",
        "planned input validation layer for the construction data intake flow",
        "reviewed n8n v1.x migration notes — flagged deprecated expression syntax",
        "drafted error handling strategy for webhook timeouts and partial failures",
        "analyzed execution log format for downstream JSON parsing compatibility",
        "compared batch vs per-record approach for large construction datasets",
        "noted memory limits on self-hosted n8n when processing large payloads",
        "researched n8n + Supabase real-time integration patterns",
        "documented trigger conditions for construction project status changes",
        "planned conditional routing logic based on project phase and priority",
        "explored n8n AI Agent node for automated site report generation",
        "noted webhook signature verification approach for improved security",
        "reviewed queue mode setup for parallel workflow execution at scale",
        "documented testing strategy for webhook-triggered workflows in staging",
        "researched n8n variables vs expressions for dynamic runtime config",
        "planned splitting large workflow into focused sub-workflows",
        "noted environment variable management for multi-stage deployments",
        "explored n8n logging integrations for audit trail requirements",
        "drafted rollback strategy for failed workflow executions",
        "reviewed rate limiting on external API calls within workflows",
        "planned adding a dashboard view for workflow run statistics",
        "researched n8n form trigger for internal data collection use cases",
    ],
    'portfolio': [
        "reviewed Lighthouse scores — targeting 95+ across all Core Web Vitals",
        "planned project filter component with tag-based selection by tech stack",
        "explored framer-motion spring animations for project card interactions",
        "added SEO improvement notes for individual project detail pages",
        "researched next/image blur placeholder optimization for project screenshots",
        "planned contact form integration using Resend API with rate limiting",
        "noted considerations for adding MDX blog with syntax highlighting",
        "identified LCP bottleneck in hero section — image preload strategy needed",
        "explored next-themes for CSS variable-based dark mode implementation",
        "updated project scope notes to include measurable outcome metrics",
        "researched adding GitHub contribution stats widget to home section",
        "noted mobile nav UX issues on 375px — hamburger z-index conflict",
        "planned live demo section with animated screenshot previews",
        "explored dynamic OG image generation using @vercel/og",
        "reviewed font pairing — switching body to Inter for readability",
        "researched adding testimonial section with structured data markup",
        "planned consolidating project data into a single typed JSON config",
        "profiled animation performance — isolating layout shifts from card grid",
        "planned resume PDF download with click analytics via Umami",
        "noted i18n considerations for future multi-language support",
        "reviewed accessibility audit — focus ring visibility improvements needed",
        "planned skills section refresh to reflect current project experience",
        "explored adding a timeline view for career milestones",
        "noted loading skeleton pattern needed for projects grid on slow connections",
        "planned fetching GitHub star counts at build time for project cards",
    ],
    'profile': [
        "updated learning roadmap: deepening focus on system design and scalability",
        "reflected on this week's open-source contributions and key takeaways",
        "planned Q3 2026 project goals and skill development targets",
        "noted insights from reading about attention mechanisms in LLMs",
        "updated current tech focus: AI tooling, automation, developer productivity",
        "reflected on algorithm practice — solidified graph traversal patterns",
        "planned contributing to an open-source Python project this month",
        "noted productivity gains from AI-assisted coding workflows",
        "reviewed project showcase priorities for portfolio update",
        "reflected on the month's learning: n8n workflows, GitHub Actions, stdlib",
        "planned writing a blog post on workflow automation patterns",
        "noted interesting developer tools explored this week",
        "updated skill ratings based on recent project experience",
        "reflected on code review best practices applied in recent PRs",
        "planned exploring Rust for a small systems programming side project",
        "noted personal productivity systems that worked well this week",
        "updated reading list — distributed systems and API design",
        "reflected on developer experience improvements worth pursuing",
        "planned building a CLI tool to automate a recurring personal workflow",
        "noted interesting GitHub repos discovered and bookmarked this week",
        "reviewed open issues in personal projects — triaged and labelled",
        "planned a research spike on vector databases for a future project",
        "reflected on pair programming insights and communication patterns",
        "noted upcoming tech talks and conferences to follow online",
        "updated personal contribution goals for the next 30 days",
    ],
}

_MESSAGES = {
    'n8n': [
        "docs: add workflow development notes",
        "docs: update agent architecture notes",
        "chore: capture integration research",
        "docs: plan next workflow iteration",
        "chore: add implementation notes",
    ],
    'portfolio': [
        "docs: add UX improvement planning notes",
        "chore: update feature development log",
        "docs: capture performance research",
        "chore: add enhancement planning notes",
        "docs: plan next portfolio iteration",
    ],
    'profile': [
        "chore: update learning and development log",
        "docs: reflect on weekly progress",
        "chore: update goals and planning notes",
        "docs: capture monthly milestones",
        "chore: add tech exploration notes",
    ],
}


# ── GitHub API helpers ─────────────────────────────────────────────────────

def _api(method: str, path: str, token: str, body: dict = None):
    url = f'https://api.github.com{path}'
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(
        url, data=data,
        headers={
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'github-garden/1.0',
            'Content-Type': 'application/json',
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise RuntimeError(f'GitHub API {e.code}: {e.read().decode()[:200]}') from e


def _get_file(repo: str, path: str, token: str):
    data = _api('GET', f'/repos/{repo}/contents/{path}', token)
    if data is None:
        return None, None
    return base64.b64decode(data['content']).decode('utf-8'), data['sha']


def _put_file(repo: str, path: str, content: str, message: str, token: str, sha: str = None):
    body = {
        'message': message,
        'content': base64.b64encode(content.encode('utf-8')).decode('ascii'),
        'committer': COMMITTER,
    }
    if sha:
        body['sha'] = sha
    return _api('PUT', f'/repos/{repo}/contents/{path}', token, body)


def _prepend_entry(content: str, entry: str, stamp: str) -> str:
    new_line = f'- [{stamp}] {entry}\n'
    marker = '## Log\n\n'
    if marker in content:
        return content.replace(marker, marker + new_line, 1)
    return content.rstrip('\n') + '\n\n' + new_line


# ── Core logic ─────────────────────────────────────────────────────────────

def _seed(key: str) -> int:
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)


def _trigger_idx() -> int:
    """Determine if this is the morning (0) or evening (1) multi_repo trigger."""
    hour = datetime.now(timezone.utc).hour
    return 0 if hour < 10 else 1


def _trigger_quota(today: date, trigger_idx: int) -> int:
    """Split the multi_repo daily total across 2 triggers."""
    total = multi_repo_daily_total(today)
    if total == 0:
        return 0
    base = total // 2
    return base + (1 if trigger_idx < total % 2 else 0)


def _pick_repo(today: date, trigger_idx: int) -> tuple:
    """Pick which repo this trigger commits to (rotates each day × trigger)."""
    rng = random.Random(_seed(f'repo-pick-{today}-{trigger_idx}'))
    return rng.choice(list(TARGET_REPOS.items()))


def commit_to_repo(repo: str, repo_type: str, today: date,
                   trigger_idx: int, n_commits: int, token: str):
    """Make n_commits sequential API commits to repo's DEVLOG.md."""
    rng = random.Random(_seed(f'{repo}-{today}-{trigger_idx}'))
    stamp = today.strftime('%Y-%m-%d')

    current_content, sha = _get_file(repo, 'DEVLOG.md', token)

    if current_content is None:
        repo_name = repo.split('/')[1]
        current_content = (
            f'# Dev Log — {repo_name}\n\n'
            f'Development notes, research, and planning entries.\n\n'
            f'## Log\n\n'
        )
        sha = None

    for i in range(n_commits):
        entry = rng.choice(_ENTRIES[repo_type])
        message = rng.choice(_MESSAGES[repo_type])
        current_content = _prepend_entry(current_content, entry, stamp)
        result = _put_file(repo, 'DEVLOG.md', current_content, message, token, sha)
        sha = result['content']['sha']
        print(f'  [{repo}][{i+1}/{n_commits}] {message}')
        print(f'    {entry}')


def main():
    token = os.environ.get('GH_PAT', '').strip()
    if not token:
        print('GH_PAT not set — skipping multi-repo updates.')
        print('Add a PAT (repo scope) as GH_PAT secret in github-garden.')
        sys.exit(0)

    today = date.today()

    if is_rest_day(today):
        print(f'Rest day ({today}) — no commits from anyone today.')
        return

    forced_repo = os.environ.get('TARGET_REPO', '').strip()
    tidx = _trigger_idx()
    quota = _trigger_quota(today, tidx)

    print(f'multi_repo | {today} | trigger {tidx} | quota {quota} commit(s)')

    if quota == 0:
        print('No multi_repo commits this trigger (quota exhausted or budget fully taken by garden).')
        return

    if forced_repo:
        repo = forced_repo
        rtype = TARGET_REPOS.get(repo, 'profile')
    else:
        repo, rtype = _pick_repo(today, tidx)

    print(f'Target: {repo} ({rtype})')
    try:
        commit_to_repo(repo, rtype, today, tidx, quota, token)
        print('Done.')
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
