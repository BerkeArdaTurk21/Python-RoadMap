# =============================================================================
# Week 07 - Day 06 | Regular Expressions — Solutions
# =============================================================================

import re

# Solution 1
text = "Room 3 has 14 chairs, opened in 2026, closes in 7 days."
strings = re.findall(r"\d+", text)
ints = [int(s) for s in strings]
print(f"Strings: {strings}")
print(f"Ints:    {ints}")
print(f"Sum:     {sum(ints)}")
print()

# Solution 2
def is_valid_phone(s):
    return re.match(r"^0\d{3} \d{3} \d{2} \d{2}$", s) is not None

numbers = ["0532 123 45 67", "532 123 45 67", "0532 123 4567"]
for n in numbers:
    print(f"{n:<15} -> {is_valid_phone(n)}")
print()

# Solution 3
text = "Contact ceo@company.com or team@support.org for help."
masked = re.sub(r"[\w.+-]+@[\w.-]+", "[EMAIL]", text)
domains = re.findall(r"[\w.+-]+@([\w.-]+)", text)
print(f"Masked: {masked}")
print(f"Domains: {domains}")
print()

# Solution 4
line = "2026-06-24 23:00:15 ERROR Disk full"
pattern = r"(?P<date>\S+) (?P<time>\S+) (?P<level>\w+) (?P<message>.+)"
m = re.search(pattern, line)
g = m.groupdict()
print(f"date={g['date']}  time={g['time']}  level={g['level']}  message={g['message']}")
print()

# Solution 5
sentence = "This is is a test where the the words repeat."
for match in re.finditer(r"\b(\w+)\s+\1\b", sentence, re.IGNORECASE):
    print(f"Repeated: {match.group(1)}")
