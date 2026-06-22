# =============================================================================
# Week 07 - Day 04 | The datetime Module
# =============================================================================
# The datetime module is the standard way to work with dates and times.
# Main classes:
#   date      — year, month, day
#   time      — hour, minute, second, microsecond
#   datetime  — date + time together
#   timedelta — a duration (the difference between two points in time)

from datetime import date, time, datetime, timedelta

# -----------------------------------------------------------------------------
# 1. date — Calendar Dates
# -----------------------------------------------------------------------------
today = date.today()
print(f"Today: {today}")
print(f"  year={today.year}, month={today.month}, day={today.day}")
print(f"  weekday (Mon=0): {today.weekday()}")
print(f"  isoweekday (Mon=1): {today.isoweekday()}")

# Build a specific date
independence = date(2023, 10, 29)
print(f"\nA specific date: {independence}")
print(f"  ISO format: {independence.isoformat()}")

# -----------------------------------------------------------------------------
# 2. time — Time of Day (no date attached)
# -----------------------------------------------------------------------------
t = time(14, 30, 15)
print(f"\nA time: {t}")
print(f"  hour={t.hour}, minute={t.minute}, second={t.second}")

# -----------------------------------------------------------------------------
# 3. datetime — Date + Time Together
# -----------------------------------------------------------------------------
now = datetime.now()
print(f"\nNow: {now}")
print(f"  date part: {now.date()}")
print(f"  time part: {now.time()}")

# Build a specific datetime
meeting = datetime(2026, 6, 23, 23, 40, 0)
print(f"\nMeeting: {meeting}")

# -----------------------------------------------------------------------------
# 4. timedelta — Durations & Date Math
# -----------------------------------------------------------------------------
# Add or subtract spans of time.
one_week = timedelta(days=7)
print(f"\nToday + 1 week: {today + one_week}")
print(f"Today - 10 days: {today - timedelta(days=10)}")

# The difference between two dates/datetimes IS a timedelta
delta = date(2026, 12, 31) - today
print(f"\nDays until 2026-12-31: {delta.days}")

# timedelta supports days, seconds, minutes, hours, weeks
span = timedelta(days=2, hours=3, minutes=30)
print(f"Total seconds in 2d 3h 30m: {span.total_seconds():,.0f}")

# -----------------------------------------------------------------------------
# 5. strftime — datetime -> formatted string
# -----------------------------------------------------------------------------
# strftime ("string format time") turns a datetime into a custom string.
# Common codes:
#   %Y full year   %m month(01-12)  %d day(01-31)
#   %H hour(00-23)  %M minute        %S second
#   %A weekday name %B month name    %p AM/PM
sample = datetime(2026, 6, 23, 23, 40, 5)
print(f"\nstrftime examples for {sample}:")
print(f"  {sample.strftime('%Y-%m-%d')}")              # 2026-06-23
print(f"  {sample.strftime('%d/%m/%Y %H:%M')}")        # 23/06/2026 23:40
print(f"  {sample.strftime('%A, %B %d, %Y')}")         # Tuesday, June 23, 2026
print(f"  {sample.strftime('%I:%M %p')}")              # 11:40 PM

# -----------------------------------------------------------------------------
# 6. strptime — string -> datetime
# -----------------------------------------------------------------------------
# strptime ("string parse time") reads a string into a datetime using a format.
parsed = datetime.strptime("2026-06-23 23:40", "%Y-%m-%d %H:%M")
print(f"\nParsed from string: {parsed}  (type: {type(parsed).__name__})")

# fromisoformat — the fast path for ISO 8601 strings
iso = datetime.fromisoformat("2026-06-23T23:40:00")
print(f"fromisoformat: {iso}")

# -----------------------------------------------------------------------------
# 7. A Small Real-World Example — Age in Days
# -----------------------------------------------------------------------------
birthday = date(2000, 1, 1)
age_days = (today - birthday).days
print(f"\nSomeone born {birthday} is {age_days:,} days old ({age_days // 365} years).")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# date / time / datetime — calendar dates, clock times, both combined
# date.today() / datetime.now() — current date / datetime
# timedelta              — durations; date arithmetic gives a timedelta
# .weekday() / .isoweekday() — day of week (Mon=0 vs Mon=1)
# strftime(fmt)          — datetime -> string
# strptime(s, fmt)       — string -> datetime
# fromisoformat / isoformat — fast ISO 8601 conversion
