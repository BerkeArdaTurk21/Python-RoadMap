# =============================================================================
# Week 07 - Day 04 | The datetime Module — Exercises
# =============================================================================

from datetime import date, time, datetime, timedelta

# -----------------------------------------------------------------------------
# Exercise 1 — Today, Formatted
# -----------------------------------------------------------------------------
# Get today's date and print it in three formats:
#   a) ISO format            (2026-06-23)
#   b) DD/MM/YYYY            (23/06/2026)
#   c) "Weekday, Month DD"   (Tuesday, June 23)
#
# Hint: date.today(), .isoformat(), strftime with %d %m %Y %A %B.

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Days Until New Year
# -----------------------------------------------------------------------------
# Calculate and print how many days are left until the next January 1st
# from today. If today IS January 1st, the answer should be 0.
#
# Expected (will vary): "Days until New Year: 192"
#
# Hint: build date(today.year + 1, 1, 1), subtract today, read .days.
#       (Edge case: if today is Jan 1, days until THIS year's Jan 1 is 0.)

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Meeting Scheduler
# -----------------------------------------------------------------------------
# A meeting starts at 2026-06-23 14:00 and lasts 90 minutes.
#   a) Print the start time as "HH:MM"
#   b) Compute and print the end time as "HH:MM"
#   c) Print the meeting duration in hours as a float (1.5)
#
# Expected:
#   Start:    14:00
#   End:      15:30
#   Duration: 1.5 hours
#
# Hint: datetime + timedelta(minutes=90); total_seconds() / 3600.

start = datetime(2026, 6, 23, 14, 0)
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Parse and Compare
# -----------------------------------------------------------------------------
# Two event timestamps arrive as strings:
#   "2026-06-23 09:15"  and  "2026-06-23 17:45"
# Parse both with strptime, then print:
#   a) Which one is earlier (print that timestamp)
#   b) The gap between them in hours and minutes, e.g. "Gap: 8h 30m"
#
# Hint: strptime(s, "%Y-%m-%d %H:%M"); subtract; use total_seconds().

s1 = "2026-06-23 09:15"
s2 = "2026-06-23 17:45"
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Countdown Generator
# -----------------------------------------------------------------------------
# Given a target datetime of 2026-06-23 23:40 and a "now" of 2026-06-23 20:00,
# print a countdown line for each whole hour remaining BEFORE the target,
# counting down. For each step print: "T-3:00:00 ..." style remaining time.
#
# Expected (now=20:00, target=23:40):
#   3:40:00 remaining
#   2:40:00 remaining
#   1:40:00 remaining
#   0:40:00 remaining
#
# Hint: start from (target - now), then repeatedly subtract timedelta(hours=1)
#       while the remaining timedelta is positive. str(timedelta) prints H:MM:SS.

now = datetime(2026, 6, 23, 20, 0)
target = datetime(2026, 6, 23, 23, 40)
# TODO
