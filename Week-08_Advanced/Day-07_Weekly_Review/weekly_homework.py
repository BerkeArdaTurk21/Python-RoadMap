# =============================================================================
# Week 08 - Day 07 | Weekly Homework — Typed Sensor Data Pipeline
# =============================================================================
# Mini project combining all Week 8 topics:
#   - decorators        : @timed measures each pipeline run (functools.wraps)
#   - iterators         : SensorLog is a custom iterator (__iter__ / __next__)
#   - generators        : parse -> only_valid is a lazy generator pipeline
#   - context managers  : temp_dataset() creates a CSV and always cleans it up
#   - type hints        : every function is fully annotated (mypy-clean)
#   - pytest            : test_* functions at the bottom — run them for real:
#
#   python weekly_homework.py          # demo + manual test run
#   pytest weekly_homework.py -v      # the same tests via the pytest runner
# =============================================================================

import csv
import functools
import random
import time
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

# ─── Decorator: @timed ─────────────────────────────────────────────────────────

def timed(func):
    """Print how long the decorated function took."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        ms = (time.perf_counter() - start) * 1000
        print(f"[timed] {func.__name__} took {ms:.2f} ms")
        return result
    return wrapper


# ─── Data model (type hints + dataclass) ───────────────────────────────────────

@dataclass
class Reading:
    sensor: str
    temp_c: float


# ─── Context manager: temporary dataset ────────────────────────────────────────

@contextmanager
def temp_dataset(rows: int, seed: int | None = None) -> Generator[Path, None, None]:
    """Create a synthetic sensor CSV, yield its path, ALWAYS delete it after."""
    if seed is not None:
        random.seed(seed)

    path = Path("readings.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sensor", "temp_c"])
        for _ in range(rows):
            sensor = random.choice(["kitchen", "garage", "attic"])
            temp = round(random.uniform(-30.0, 60.0), 1)
            writer.writerow([sensor, temp])
        writer.writerow(["kitchen", "not-a-number"])   # corrupt row on purpose
        writer.writerow(["", "12.5"])                  # and a missing sensor
    try:
        yield path
    finally:
        path.unlink(missing_ok=True)   # cleanup runs even if the caller crashes


# ─── Custom iterator: SensorLog ────────────────────────────────────────────────

class SensorLog:
    """Iterates over the data rows of a sensor CSV, skipping the header."""

    def __init__(self, path: Path) -> None:
        self._file = open(path, encoding="utf-8")
        self._reader = csv.reader(self._file)
        next(self._reader)   # skip header row

    def __iter__(self) -> "SensorLog":
        return self

    def __next__(self) -> list[str]:
        try:
            return next(self._reader)
        except StopIteration:
            self._file.close()
            raise                      # re-raise so for-loops stop normally


# ─── Generator pipeline: parse -> only_valid ───────────────────────────────────

def parse(rows: Iterator[list[str]]) -> Generator[Reading, None, None]:
    """Lazily turn raw CSV rows into Reading objects, skipping corrupt rows."""
    for row in rows:
        if len(row) != 2 or not row[0]:
            continue
        try:
            yield Reading(sensor=row[0], temp_c=float(row[1]))
        except ValueError:
            continue                   # unparseable temperature → skip


def only_valid(
    readings: Iterator[Reading], lo: float = -40.0, hi: float = 85.0
) -> Generator[Reading, None, None]:
    """Drop physically impossible readings (outside the sensor's range)."""
    for r in readings:
        if lo <= r.temp_c <= hi:
            yield r


def summarize(readings: Iterator[Reading]) -> dict[str, dict[str, float]]:
    """Consume the pipeline once and compute min/max/avg per sensor."""
    temps: dict[str, list[float]] = {}
    for r in readings:
        temps.setdefault(r.sensor, []).append(r.temp_c)
    return {
        sensor: {
            "count": len(values),
            "min": min(values),
            "max": max(values),
            "avg": round(sum(values) / len(values), 2),
        }
        for sensor, values in temps.items()
    }


# ─── Putting it all together ───────────────────────────────────────────────────

@timed
def run_pipeline(path: Path) -> dict[str, dict[str, float]]:
    """SensorLog (iterator) → parse (gen) → only_valid (gen) → summarize."""
    return summarize(only_valid(parse(SensorLog(path))))


def print_report(stats: dict[str, dict[str, float]]) -> None:
    print("-- Sensor Report --")
    for sensor, s in sorted(stats.items()):
        print(
            f"  {sensor:<10} count={s['count']:<4.0f} "
            f"min={s['min']:<7.1f} max={s['max']:<7.1f} avg={s['avg']}"
        )


# ─── Tests (run with: pytest weekly_homework.py -v) ────────────────────────────

def test_parse_skips_corrupt_rows():
    rows = iter([["kitchen", "21.5"], ["garage", "oops"], ["", "3.0"], ["attic"]])
    readings = list(parse(rows))
    assert readings == [Reading("kitchen", 21.5)]

def test_only_valid_filters_out_of_range():
    readings = iter([Reading("a", 20.0), Reading("a", 999.0), Reading("a", -80.0)])
    assert [r.temp_c for r in only_valid(readings)] == [20.0]

def test_summarize_per_sensor():
    readings = iter([Reading("a", 10.0), Reading("a", 20.0), Reading("b", 5.0)])
    stats = summarize(readings)
    assert stats["a"] == {"count": 2, "min": 10.0, "max": 20.0, "avg": 15.0}
    assert stats["b"]["count"] == 1

def test_pipeline_end_to_end():
    with temp_dataset(rows=25, seed=7) as path:
        stats = run_pipeline(path)
        assert path.exists()
        total = sum(s["count"] for s in stats.values())
        assert 0 < total <= 25          # corrupt rows were skipped
    assert not path.exists()            # context manager cleaned up


# ─── Demo ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating 25 readings and running the pipeline...\n")
    with temp_dataset(rows=25, seed=7) as dataset:
        print_report(run_pipeline(dataset))
    print("\nDataset cleaned up by the context manager.")

    print("\nRunning tests manually...")
    test_parse_skips_corrupt_rows()
    test_only_valid_filters_out_of_range()
    test_summarize_per_sensor()
    test_pipeline_end_to_end()
    print("4 tests passed ✅  (also try: pytest weekly_homework.py -v)")
