# =============================================================================
# Week 07 - Day 04 | The datetime Module — Solutions
# =============================================================================

from datetime import date, datetime, timedelta

# Solution 1
today = date.today()
print(f"ISO:     {today.isoformat()}")
print(f"DD/MM:   {today.strftime('%d/%m/%Y')}")
print(f"Pretty:  {today.strftime('%A, %B %d')}")
print()

# Solution 2
today = date.today()
if today.month == 1 and today.day == 1:
    days_left = 0
else:
    next_year = date(today.year + 1, 1, 1)
    days_left = (next_year - today).days
print(f"Days until New Year: {days_left}")
print()

# Solution 3
start = datetime(2026, 6, 23, 14, 0)
duration = timedelta(minutes=90)
end = start + duration
print(f"Start:    {start.strftime('%H:%M')}")
print(f"End:      {end.strftime('%H:%M')}")
print(f"Duration: {duration.total_seconds() / 3600} hours")
print()

# Solution 4
s1 = "2026-06-23 09:15"
s2 = "2026-06-23 17:45"
fmt = "%Y-%m-%d %H:%M"
d1 = datetime.strptime(s1, fmt)
d2 = datetime.strptime(s2, fmt)

earlier = min(d1, d2)
print(f"Earlier: {earlier.strftime(fmt)}")

gap = abs(d2 - d1)
total_minutes = int(gap.total_seconds() // 60)
hours, minutes = divmod(total_minutes, 60)
print(f"Gap: {hours}h {minutes}m")
print()

# Solution 5
now = datetime(2026, 6, 23, 20, 0)
target = datetime(2026, 6, 23, 23, 40)
remaining = target - now
while remaining.total_seconds() > 0:
    print(f"{remaining} remaining")
    remaining -= timedelta(hours=1)
