"""PH6721 cross-references — verify that every cited section actually exists.

The notebooks cite each other by section number, and 00B's symbol index is one
long table of such citations. Those numbers are an API: renaming or renumbering
a section silently breaks every reference to it, and nothing else in the repo
notices.

Four citation forms are recognised, all of them already in use:

    `02A` §8.4        another notebook, explicit section
    `02A` section 8.4 the same, spelled out
    §6.1              a section number on its own
    section 9.4       the same, spelled out
    `01C`             a notebook with no section

A bare number normally means "this notebook". Where it does not resolve there,
the checker retries against any notebook named in the same cell, which is what
makes 00A's mapping table work: its rows say "§6.1" under a heading that names
00B. A citation that resolves nowhere is reported.

Usage:
    python check_section_refs.py check    # validate, exit 1 on any problem
    python check_section_refs.py list     # print the sections of each notebook
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADING = re.compile(r'^#{1,3}\s+(\d+(?:\.\d+)?)\.?\s+\S')
# A notebook is named either in backticks or, inside the exercise boxes, in <code> tags.
NAMED = r'(?:`(?P<a>\d\d[A-Z])`|<code>(?P<b>\d\d[A-Z])</code>)'
NOTEBOOK_CODE = re.compile(r'`(\d\d[A-Z])`|<code>(\d\d[A-Z])</code>')
EXPLICIT = re.compile(NAMED + r'\s*(?:§\s*|sections?\s+)(?P<n>\d+(?:\.\d+)?)')
BARE = re.compile(r'§\s*(\d+(?:\.\d+)?)|\bsections?\s+(\d+(?:\.\d+)?)', re.I)
# "sections 3 to 7", "§3.2, §3.3", "sections 9.2 and 9.3"
FOLLOW_ON = re.compile(r'\s*(?:,|and|to|-|–)\s*§?\s*(\d+(?:\.\d+)?)', re.I)


def notebooks():
    for p in sorted(glob.glob(f"{ROOT}/Classes/**/*.ipynb", recursive=True)):
        if "checkpoint" in p or "_archive" in p:
            continue
        yield p


def code_of(path):
    return os.path.basename(path)[:3]


def sections_of(path):
    """Every numbered section heading in one notebook."""
    found = set()
    for c in json.load(open(path))["cells"]:
        if c["cell_type"] != "markdown":
            continue
        for line in "".join(c["source"]).splitlines():
            m = HEADING.match(line)
            if m:
                found.add(m.group(1))
    return found


def citations(text):
    """Yield (target_or_None, section, quoted) for every citation in one cell."""
    for m in EXPLICIT.finditer(text):
        yield m.group("a") or m.group("b"), m.group("n"), m.group(0)
    # Bare numbers, skipping any already consumed by an explicit citation.
    taken = {m.span("n") for m in EXPLICIT.finditer(text)}
    for m in BARE.finditer(text):
        number = m.group(1) or m.group(2)
        span = m.span(1) if m.group(1) else m.span(2)
        if span in taken:
            continue
        yield None, number, m.group(0).strip()
        # pick up "and 9.3", ", §3.3", "to 7" trailing the same citation
        pos = m.end()
        while True:
            f = FOLLOW_ON.match(text, pos)
            if not f:
                break
            yield None, f.group(1), f.group(0).strip()
            pos = f.end()


def check(path, index, planned, forward):
    """Problems with the citations in one notebook."""
    here = code_of(path)
    nb = json.load(open(path))
    problems, count = [], 0

    for i, c in enumerate(nb["cells"]):
        if c["cell_type"] != "markdown":
            continue
        text = "".join(c["source"])
        named = {a or b for a, b in NOTEBOOK_CODE.findall(text)}
        mentioned = sorted(named - {here})

        for name in sorted(named):
            if name not in index:
                if name in planned:
                    forward.add(f"`{here}` cites `{name}`, which the outline plans but which is not built yet")
                else:
                    problems.append(f"cell {i}: cites notebook `{name}`, which does not exist "
                                    f"and is not in the outline")

        for target, number, quoted in citations(text):
            count += 1
            if target is not None:
                if target not in index:
                    continue                  # already reported above, or a planned notebook
                elif number not in index[target]:
                    problems.append(f"cell {i}: '{quoted}' — `{target}` has no section {number}")
                continue
            if number in index[here]:
                continue
            elsewhere = [n for n in mentioned if number in index.get(n, ())]
            if len(elsewhere) == 1:
                continue                      # resolved from the cell's own context
            if elsewhere:
                problems.append(f"cell {i}: '{quoted}' is ambiguous — could be {', '.join(elsewhere)}")
            else:
                problems.append(f"cell {i}: '{quoted}' — no section {number} in `{here}`"
                                + (f" or in {', '.join(mentioned)}" if mentioned else ""))
    return problems, count


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    index = {code_of(p): sections_of(p) for p in notebooks()}
    # Notebooks the outline plans but which are not written yet: a reference
    # forward to one of those is intentional, not a broken link.
    outline = os.path.join(ROOT, "Outline", "CourseOutline.md")
    planned = set()
    if os.path.exists(outline):
        planned = {a or b for a, b in NOTEBOOK_CODE.findall(open(outline).read())}
    forward = set()

    if mode == "list":
        for p in notebooks():
            got = sorted(index[code_of(p)], key=lambda s: [int(n) for n in s.split(".")])
            print(f"  {os.path.basename(p):48s} {' '.join(got) if got else '(no numbered sections)'}")
        return

    failed = 0
    for p in notebooks():
        problems, count = check(p, index, planned, forward)
        status = "OK" if not problems else f"{len(problems)} PROBLEM(S)"
        print(f"  {os.path.basename(p):48s} refs={count:>3}  {status}")
        for pr in problems:
            print(f"      {pr}")
        failed += len(problems)
    for f in sorted(forward):
        print(f"  note: {f}")
    print(f"\n{'all references resolve' if not failed else str(failed) + ' problem(s)'}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
