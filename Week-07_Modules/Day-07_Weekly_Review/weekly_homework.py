# =============================================================================
# Week 07 - Day 07 | Weekly Homework — CLI Log Analyzer
# =============================================================================
# Mini project combining all Week 7 topics:
#   - Import system & __main__ : module layout + the if __name__ guard
#   - os / pathlib             : create, locate and clean up files
#   - sys & argparse           : a real CLI with subcommands
#   - datetime                 : timestamps and time-window filtering
#   - random                   : generate a realistic sample log
#   - re (regex)               : parse each log line into fields
#
# Usage:
#   python weekly_homework.py generate --lines 50 --out app.log
#   python weekly_homework.py analyze app.log
#   python weekly_homework.py analyze app.log --level ERROR
#
# With no arguments it runs a self-contained demo.
# =============================================================================

import argparse
import random
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

# ─── Log format ────────────────────────────────────────────────────────────────
# Each line looks like:
#   2026-06-24 14:03:11 [ERROR] auth: login failed for user 42
LOG_LINE = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"\[(?P<level>[A-Z]+)\] "
    r"(?P<module>\w+): "
    r"(?P<message>.+)$"
)

LEVELS  = ["DEBUG", "INFO", "INFO", "INFO", "WARNING", "ERROR"]  # weighted
MODULES = ["auth", "db", "api", "cache", "worker"]
MESSAGES = {
    "auth":   ["login ok for user {n}", "login failed for user {n}", "token refreshed"],
    "db":     ["query took {n}ms", "connection pool at {n}%", "slow query detected"],
    "api":    ["GET /items returned {n}", "POST /orders ok", "rate limit hit"],
    "cache":  ["hit ratio {n}%", "evicted {n} keys", "miss for key user:{n}"],
    "worker": ["job {n} done", "retrying job {n}", "queue depth {n}"],
}


# ─── generate ───────────────────────────────────────────────────────────────────

def generate_log(lines: int, out: Path, seed: int | None = None) -> Path:
    """Write a synthetic log file with `lines` entries and return its path."""
    if seed is not None:
        random.seed(seed)

    start = datetime.now() - timedelta(minutes=lines)
    with open(out, "w", encoding="utf-8") as f:
        for i in range(lines):
            ts = (start + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(LEVELS)
            module = random.choice(MODULES)
            template = random.choice(MESSAGES[module])
            message = template.format(n=random.randint(1, 999))
            f.write(f"{ts} [{level}] {module}: {message}\n")
    return out


# ─── analyze ────────────────────────────────────────────────────────────────────

def parse_line(line: str) -> dict | None:
    """Return the parsed fields of one log line, or None if it doesn't match."""
    m = LOG_LINE.match(line.rstrip("\n"))
    if not m:
        return None
    data = m.groupdict()
    data["dt"] = datetime.strptime(data["ts"], "%Y-%m-%d %H:%M:%S")
    return data


def analyze_log(path: Path, level: str | None = None) -> dict:
    """Read a log file and return summary statistics."""
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    level_counts: dict[str, int] = {}
    module_counts: dict[str, int] = {}
    matched, skipped = 0, 0
    first_dt = last_dt = None

    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            entry = parse_line(line)
            if entry is None:
                skipped += 1
                continue
            if level and entry["level"] != level.upper():
                continue
            matched += 1
            level_counts[entry["level"]]   = level_counts.get(entry["level"], 0) + 1
            module_counts[entry["module"]] = module_counts.get(entry["module"], 0) + 1
            first_dt = first_dt or entry["dt"]
            last_dt = entry["dt"]

    return {
        "matched": matched,
        "skipped": skipped,
        "levels": level_counts,
        "modules": module_counts,
        "first": first_dt,
        "last": last_dt,
    }


def print_report(stats: dict) -> None:
    print("-- Log Analysis Report --")
    print(f"  Matched lines : {stats['matched']}")
    print(f"  Skipped lines : {stats['skipped']}")
    if stats["first"] and stats["last"]:
        span = stats["last"] - stats["first"]
        print(f"  Time span     : {stats['first']}  ->  {stats['last']}  ({span})")

    if stats["levels"]:
        print("\n  By level:")
        for lvl, n in sorted(stats["levels"].items(), key=lambda kv: -kv[1]):
            print(f"    {lvl:<8} {'#' * n} {n}")

    if stats["modules"]:
        print("\n  By module:")
        for mod, n in sorted(stats["modules"].items(), key=lambda kv: -kv[1]):
            print(f"    {mod:<8} {n}")


# ─── CLI ────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="log_analyzer",
        description="Generate and analyze application logs.",
    )
    sub = parser.add_subparsers(dest="command")

    g = sub.add_parser("generate", help="create a synthetic log file")
    g.add_argument("--lines", type=int, default=50, help="number of log lines")
    g.add_argument("--out", default="app.log", help="output file path")
    g.add_argument("--seed", type=int, default=None, help="seed for reproducibility")

    a = sub.add_parser("analyze", help="analyze an existing log file")
    a.add_argument("file", help="log file to analyze")
    a.add_argument("--level", help="only count this level (e.g. ERROR)")

    return parser


def run_demo() -> None:
    """No CLI args → generate a small log, analyze it, then clean up."""
    print("No command given - running demo.\n")
    demo = Path("demo.log")
    generate_log(lines=30, out=demo, seed=7)
    print(f"Generated {demo} (30 lines, seed=7)\n")

    stats = analyze_log(demo)
    print_report(stats)

    print("\n-- Filtered: ERROR only --")
    print_report(analyze_log(demo, level="ERROR"))

    demo.unlink(missing_ok=True)
    print(f"\n{demo} removed. Done!")


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)

    if args.command == "generate":
        out = generate_log(args.lines, Path(args.out), args.seed)
        print(f"Wrote {args.lines} lines to {out.resolve()}")
    elif args.command == "analyze":
        print_report(analyze_log(Path(args.file), args.level))
    else:
        run_demo()


if __name__ == "__main__":
    main()
