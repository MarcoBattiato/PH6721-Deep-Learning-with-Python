"""PH6721 cell markers — clear and validate cells that must ship without output.

Two tags, both meaning "do not store this cell's output", for two different reasons:

  predict    the student should work out the answer before running it
  run-fresh  a stored output would be misleading (a setup check that must
             prove *their* environment works, not that mine did)

Each tagged code cell must be immediately preceded by a markdown cell carrying
the matching banner, so the machine marker and the student-facing instruction
cannot drift apart.

Usage:
    python notebook_markers.py check     # validate, exit 1 on any problem
    python notebook_markers.py clear     # clear tagged outputs, then validate
"""
import json, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BANNERS = {
    "predict":   "Think about your answer before running this cell.",
    "run-fresh": "Run this cell yourself. Its output is not stored in the notebook.",
}

def notebooks():
    for p in sorted(glob.glob(f"{ROOT}/Classes/**/*.ipynb", recursive=True)):
        if "checkpoint" in p or "_archive" in p:
            continue
        yield p

def tags_of(cell):
    return [t for t in cell.get("metadata", {}).get("tags", []) if t in BANNERS]

def preceding_markdown(cells, i):
    for j in range(i - 1, -1, -1):
        if cells[j]["cell_type"] == "markdown":
            return "".join(cells[j]["source"])
        return None          # a non-markdown cell sits immediately before
    return None

def clear(path):
    nb = json.load(open(path)); changed = 0
    for c in nb["cells"]:
        if c["cell_type"] != "code":
            continue
        # nbconvert injects per-cell execution timings; they are pure noise in a
        # committed notebook and change on every run.
        if c.get("metadata", {}).pop("execution", None) is not None:
            changed += 1
        if tags_of(c) and (c.get("outputs") or c.get("execution_count") is not None):
            c["outputs"] = []; c["execution_count"] = None; changed += 1
    if changed:
        json.dump(nb, open(path, "w"), indent=1)
    return changed

def check(path):
    nb = json.load(open(path)); cells = nb["cells"]; problems = []
    banner_texts = list(BANNERS.values())

    for i, c in enumerate(cells):
        if c["cell_type"] != "code":
            continue
        tags = tags_of(c)
        if not tags:
            continue
        if len(tags) > 1:
            problems.append(f"cell {i}: more than one marker tag {tags}")
            continue
        tag = tags[0]
        if c.get("outputs"):
            problems.append(f"cell {i}: tagged '{tag}' but still has stored output")
        before = preceding_markdown(cells, i)
        if before is None:
            problems.append(f"cell {i}: tagged '{tag}' but no markdown cell immediately before it")
        elif BANNERS[tag] not in before:
            problems.append(f"cell {i}: tagged '{tag}' but the banner above it is missing or reworded")

    # the reverse direction: a banner with nothing tagged after it
    for i, c in enumerate(cells):
        if c["cell_type"] != "markdown":
            continue
        text = "".join(c["source"])
        for tag, banner in BANNERS.items():
            if banner not in text:
                continue
            nxt = cells[i + 1] if i + 1 < len(cells) else None
            if nxt is None or nxt["cell_type"] != "code" or tag not in tags_of(nxt):
                problems.append(f"cell {i}: shows the '{tag}' banner but the next cell is not tagged '{tag}'")
    return problems

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    total_cleared = 0
    if mode == "clear":
        for p in notebooks():
            n = clear(p)
            if n:
                print(f"  cleared/tidied {n:>2} cell(s)  {os.path.basename(p)}")
                total_cleared += n
        print(f"{total_cleared} cell(s) touched\n")

    failed = 0
    for p in notebooks():
        problems = check(p)
        tagged = sum(1 for c in json.load(open(p))["cells"] if c["cell_type"] == "code" and tags_of(c))
        status = "OK" if not problems else f"{len(problems)} PROBLEM(S)"
        print(f"  {os.path.basename(p):48s} tagged={tagged:>2}  {status}")
        for pr in problems:
            print(f"      {pr}")
        failed += len(problems)
    print(f"\n{'all consistent' if not failed else str(failed) + ' problem(s)'}")
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
