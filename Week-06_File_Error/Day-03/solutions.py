# =============================================================================
# Week 06 - Day 03 | Working with Paths — Solutions
# =============================================================================
import shutil
from pathlib import Path

# Solution 1
# KEY INSIGHT: Path(__file__).parent gives the directory of the script itself.
here = Path(__file__).parent
py_files = sorted(here.glob("*.py"))
print(f"Directory: {here.resolve()}")
print(f"Python files: {len(py_files)}")
for f in py_files:
    print(f"  {f.name:<16} — {f.stat().st_size} bytes")
print()

# Solution 2
# KEY INSIGHT: parents=True + exist_ok=True creates the full path in one call.
root = Path("project_root")
for d in [root / "src", root / "tests"]:
    d.mkdir(parents=True, exist_ok=True)

(root / "src"   / "main.py"      ).write_text("# main module\n",  encoding="utf-8")
(root / "src"   / "utils.py"     ).write_text("# utilities\n",    encoding="utf-8")
(root / "tests" / "test_main.py" ).write_text("# tests\n",        encoding="utf-8")
(root           / "README.md"    ).write_text("# My Project\n",   encoding="utf-8")

all_files = sorted(f for f in root.rglob("*") if f.is_file())
for f in all_files:
    print(f.relative_to(root))
print()

# Solution 3
path_str = "/home/berke/projects/data_analysis/report_2026.csv"
p = Path(path_str)
print(f"Parent:    {p.parent}")
print(f"Filename:  {p.name}")
print(f"Stem:      {p.stem}")
print(f"Extension: {p.suffix}")
print(f"Absolute:  {p.resolve()}")
print()

# Solution 4
docs = root / "docs"
docs.mkdir(exist_ok=True)
(docs / "notes.txt").write_text("notes\n", encoding="utf-8")
(docs / "todo.txt" ).write_text("todo\n",  encoding="utf-8")

matches = sorted(
    f for f in root.rglob("*")
    if f.is_file() and f.suffix in {".txt", ".md"}
)
for f in matches:
    print(f"  {str(f.relative_to(root)):<20} {f.stat().st_size} bytes")
print()

# Solution 5
# KEY INSIGHT: check source exists AND destination doesn't before renaming.
src_dir = root / "src"
source = src_dir / "utils.py"
dest   = src_dir / "helpers.py"

if source.exists() and not dest.exists():
    source.rename(dest)
    print(f"Renamed {source.name} -> {dest.name}")
elif not source.exists():
    print("Source file does not exist.")
else:
    print("Destination already exists — rename aborted.")

print("Files in src/:")
for f in sorted(src_dir.iterdir()):
    print(f"  {f.name}")

# Cleanup
if root.exists():
    shutil.rmtree(root)
