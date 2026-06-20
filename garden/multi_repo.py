"""
Spreads realistic dev-log commits across your other GitHub repos via the API.
Requires GH_PAT secret (classic PAT, repo scope) stored in github-garden.
"""
import base64
import hashlib
import json
import os
import random
import sys
import urllib.request
import urllib.error
from datetime import date

OWNER = 'Yashwanth2408'
COMMITTER = {
    'name': 'Yashwanth2408',
    'email': 'yashwanthbalaji.2408@gmail.com',
}

# Repos to receive commits and their content type
TARGET_REPOS = {
    f'{OWNER}/n8n-construction-agent': 'n8n',
    f'{OWNER}/yashwanth-portfolio':    'portfolio',
    f'{OWNER}/Yashwanth2408':          'profile',
}

# Realistic dev-log entries per repo type
# These are the actual lines written into DEVLOG.md — meaningful dev diary content
_ENTRIES = {
    'n8n': [
        "explored webhook authentication patterns for incoming construction data payloads",
        "added notes on retry logic strategy for HTTP request nodes under high load",
        "documented n8n credential scoping best practices for multi-env deployments",
        "researched community nodes available for GeoJSON / spatial data transformation",
        "planned input validation layer for construction data intake flow",
        "reviewed n8n v1.x migration notes — flagged deprecated expression syntax",
        "drafted error handling strategy for webhook timeouts and partial failures",
        "analyzed execution log output format for downstream JSON parsing compatibility",
        "compared batch processing vs per-record approach for large construction datasets",
        "added notes on self-hosted n8n memory limits when processing large payloads",
        "researched n8n + Supabase real-time integration patterns",
        "documented agent trigger conditions for construction project status changes",
        "planned conditional routing logic based on project phase and priority",
        "explored n8n AI Agent node for automated site report generation",
        "noted webhook signature verification approach for improved security",
        "reviewed queue mode setup for parallel workflow execution at scale",
        "documented testing strategy for webhook-triggered workflows in staging",
        "researched n8n variables vs expressions for dynamic runtime configuration",
        "planned splitting large monolithic workflow into focused sub-workflows",
        "noted environment variable management pattern for multi-stage deployments",
        "explored n8n logging integrations for audit trail requirements",
        "drafted rollback strategy for failed workflow executions",
        "reviewed rate limiting behavior on external API calls within workflows",
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
        "noted considerations for adding MDX blog support with syntax highlighting",
        "identified LCP bottleneck in hero section — image preload needed",
        "explored next-themes for CSS variable-based dark mode implementation",
        "updated project description scope to include measurable outcome metrics",
        "researched adding GitHub contribution stats widget to home section",
        "noted mobile nav UX issues on 375px — hamburger menu z-index conflict",
        "planned live demo section with animated screenshot previews",
        "explored dynamic OG image generation using @vercel/og",
        "reviewed font pairing — switching body to Inter for readability",
        "researched adding testimonial section with structured data markup",
        "planned consolidating project data into a single typed JSON config file",
        "profiled animation performance — isolating layout shifts from card grid",
        "planned resume PDF download button with click analytics via Umami",
        "noted i18n considerations for future multi-language portfolio support",
        "reviewed accessibility audit results — focus ring visibility improvements",
        "planned skills section refresh to reflect current project experience",
        "explored adding a timeline view for career milestones",
        "noted loading skeleton pattern needed for projects grid",
        "planned adding project GitHub stars count fetched at build time",
    ],
    'profile': [
        "updated learning roadmap: deepening focus on system design and scalability",
        "reflected on this week's open-source contributions and key takeaways",
        "planned Q3 2026 project goals and skills development targets",
        "noted interesting insights from reading about attention mechanisms in LLMs",
        "updated current tech focus: AI tooling, automation, and developer productivity",
        "reflected on algorithm practice — solidified graph traversal patterns",
        "planned contributing to an open-source Python project this month",
        "noted productivity gains from new VS Code extensions for AI-assisted coding",
        "reviewed project showcase priorities for the portfolio update",
        "reflected on the month's learning: n8n workflows, GitHub Actions, Python stdlib",
        "planned writing a short blog post on workflow automation patterns",
        "noted interesting developer tools explored this week",
        "updated self-assessed skill levels based on recent project work",
        "reflected on code review best practices applied in recent PRs",
        "planned exploring Rust for a small systems programming side project",
        "noted personal productivity systems that worked well this week",
        "updated reading list — added books on distributed systems and API design",
        "reflected on developer experience improvements worth pursuing next quarter",
        "planned building a CLI tool to automate a recurring personal workflow",
        "noted interesting GitHub repos discovered and bookmarked this week",
        "reviewed open issues in personal projects — triaged and labeled",
        "planned a small research spike on vector databases for a future project",
        "reflected on pair programming session insights and communication patterns",
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


def _seed(key: str) -> int:
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2 ** 32)


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
        body_text = e.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'GitHub API {e.code}: {body_text[:200]}') from e


def _get_file(repo: str, path: str, token: str):
    """Returns (content_str, sha) or (None, None) if not found."""
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
    _api('PUT', f'/repos/{repo}/contents/{path}', token, body)


def update_repo(repo: str, repo_type: str, today: date, run_number: int, token: str):
    rng = random.Random(_seed(f'{repo}-{today}-{run_number}'))

    entry = rng.choice(_ENTRIES[repo_type])
    message = rng.choice(_MESSAGES[repo_type])

    current, sha = _get_file(repo, 'DEVLOG.md', token)
    stamp = today.strftime('%Y-%m-%d')
    new_line = f'- [{stamp}] {entry}\n'

    if current is None:
        repo_name = repo.split('/')[1]
        content = (
            f'# Dev Log — {repo_name}\n\n'
            f'Development notes, research, and planning.\n\n'
            f'## Log\n\n'
            f'{new_line}'
        )
    else:
        if '## Log\n\n' in current:
            content = current.replace('## Log\n\n', f'## Log\n\n{new_line}', 1)
        else:
            content = current.rstrip('\n') + f'\n\n{new_line}'

    _put_file(repo, 'DEVLOG.md', content, message, token, sha)
    print(f'[{repo}] {message}')
    print(f'  note: {entry}')


def pick_repo(today: date, run_number: int) -> tuple:
    """Deterministically pick one target repo per trigger run."""
    rng = random.Random(_seed(f'pick-{today}-{run_number}'))
    repos = list(TARGET_REPOS.items())

    # ~75% of triggers update a repo; 25% rest (realistic)
    if rng.random() > 0.75:
        return None, None

    repo, rtype = rng.choice(repos)
    return repo, rtype


def main():
    token = os.environ.get('GH_PAT', '').strip()
    if not token:
        print('GH_PAT not configured — skipping multi-repo updates.')
        print('See README: create a PAT with repo scope and add it as GH_PAT secret.')
        sys.exit(0)

    run_number = int(os.environ.get('GARDEN_SEED', '1'))
    today = date.today()

    # Manual override via workflow_dispatch
    forced_repo = os.environ.get('TARGET_REPO', '').strip()
    if forced_repo:
        repo = forced_repo
        rtype = TARGET_REPOS.get(repo, 'profile')
    else:
        repo, rtype = pick_repo(today, run_number)

    if not repo:
        print(f'Resting today ({today}) — no repo update this trigger.')
        return

    print(f'Updating {repo} ({today}, run={run_number})')
    try:
        update_repo(repo, rtype, today, run_number, token)
        print('Done.')
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
