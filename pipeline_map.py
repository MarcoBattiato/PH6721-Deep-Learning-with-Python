"""The course pipeline map.

Read top to bottom. Within a step, boxes stacked vertically happen one after the
other; boxes side by side happen in parallel. A step that iterates carries a
return arrow.

    pipeline_map({"7": "now", "8.1": "now"},          # what this notebook covers
                 notes={"5.1": "not needed for trees"},  # per-notebook comments
                 title="Where 04A sits in the pipeline")

States: 'now' · 'part' · 'done' · 'next' (the default).
Keys are "7" for a whole step or "7.2" for one sub-step; a sub-step key wins.
A step with no key inherits the strongest state its sub-steps carry.
A step drawn with a box beneath it takes "5.after" for that box, falling back to
the step's own state — the Pipeline of step 5 is covered later than its parts.
"""
import textwrap

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

STEPS = [
    dict(n=1,  title="Frame\nthe problem", mode="seq",
         subs=["the question, and the data you can get", "what to predict",
               "regression or classification", "which metric"]),
    dict(n=2,  title="Split", mode="seq",
         subs=["train / test", "validation or cross-validation"],
         note="split before you look — this is what prevents data snooping · "
              "time- or group-aware when rows are not independent"),
    dict(n=3,  title="Explore\nthe training part", mode="par",
         subs=["summaries", "distributions", "relationships", "correlation"]),
    dict(n=4,  title="Clean and impute", mode="par",
         subs=["missing values", "outliers"], note="fitted on training data only"),
    dict(n=5,  title="Features and\npreprocessing", mode="par",
         subs=["scaling", "encoding", "basis expansion", "feature selection"],
         after="assembled into one Pipeline"),
    dict(n=6,  title="Baseline", mode="par", subs=["the number to beat"]),
    dict(n=7,  title="Method and loss", mode="seq",
         subs=["the model family", "the loss", "the penalty"]),
    dict(n=8,  title="Train and select\n(model selection)", mode="loop",
         subs=["fit on training", "score on validation / CV", "error analysis",
               "adjust — hyperparameters, or another method"],
         note="repeat until it stops paying"),
    dict(n=9,  title="Final evaluation\n(model assessment)", mode="seq",
         subs=["the test set, once", "an uncertainty on the number"]),
    dict(n=10, title="Interpret\nand deliver", mode="par",
         subs=["what the model says", "what to report", "known limits"],
         after="(monitoring · retraining)", after_fixed="next",
         after_note="named, never taught in this course"),
]

C = {"now":  ("#1F4E79", "#FFFFFF", "#1F4E79"),
     "part": ("#D6E4F0", "#14395B", "#8FB3D4"),
     "done": ("#F0F2F5", "#9AA1AB", "#E0E4E9"),
     "next": ("#FFFFFF", "#AEB5BE", "#D4D9DF")}
INK, GREY, FAINT = "#1B2430", "#5A646F", "#C9CED5"
_RANK = {"next": 0, "done": 1, "part": 2, "now": 3}

GUT, X, W = 0.42, 2.75, 7.9          # spine x, content x, content width
H1, H2, VGAP, SGAP = 0.50, 0.74, 0.11, 0.40   # box heights (plain / with note)


def _state(st, s, k=None):
    if k is not None and f"{s['n']}.{k}" in st:
        return st[f"{s['n']}.{k}"]
    own = st.get(str(s["n"]), st.get(s["n"]))
    if k is not None or own:
        return own or "next"
    subs = [st[f"{s['n']}.{i+1}"] for i in range(len(s["subs"]))
            if f"{s['n']}.{i+1}" in st]
    return max(subs, key=lambda v: _RANK[v]) if subs else "next"


def _h(s, notes):
    """Height of one step block."""
    def rowh(keys):
        ns = [notes[k] for k in keys if notes.get(k)]
        if not ns:
            return H1
        wide = W if len(keys) == 1 else (W - 0.11 * (len(keys) - 1)) / len(keys)
        lines = max(textwrap.fill(n, max(14, int(wide / 0.058))).count("\n") + 1
                    for n in ns)
        return H2 + 0.17 * (lines - 1)
    if s["mode"] in ("seq", "loop"):
        tot = sum(rowh([f"{s['n']}.{i+1}"]) for i in range(len(s["subs"])))
        tot += VGAP * (len(s["subs"]) - 1)
    else:
        tot = rowh([f"{s['n']}.{i+1}" for i in range(len(s["subs"]))])
    if s.get("after"):
        tot += VGAP + H1
    if s.get("note"):
        tot += 0.28
    if s.get("after_note"):
        tot += 0.26
    return tot + SGAP


def _box(ax, x, y, w, h, label, kind, note=None):
    face, ink, edge = C[kind]
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle="round,pad=0.006,rounding_size=0.07",
                 facecolor=face, edgecolor=edge,
                 lw=1.5 if kind == "now" else 1.0,
                 linestyle="-" if kind != "next" else (0, (3.5, 2.6)), zorder=3))
    if note:
        wrapped = textwrap.fill(note, max(14, int(w / 0.058)))
        nl = wrapped.count("\n") + 1
        fs = 7.6 if nl < 3 else 6.9
        ax.text(x + w / 2, y + h * (0.70 if nl == 1 else 0.74), label,
                ha="center", va="center", fontsize=8.6, color=ink,
                fontweight="bold", zorder=4)
        ax.text(x + w / 2, y + h * (0.27 if nl == 1 else 0.24), wrapped,
                ha="center", va="center", fontsize=fs, color=ink, alpha=0.88,
                style="italic", zorder=4, linespacing=1.18)
    else:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=8.6, color=ink, fontweight="bold", zorder=4)


def pipeline_map(state=None, notes=None, title="", lead=None, ax=None):
    st, nt = dict(state or {}), dict(notes or {})
    heights = [_h(s, nt) for s in STEPS]
    H = sum(heights)
    if ax is None:
        _, ax = plt.subplots(figsize=(11.2, 0.62 * H + 1.9))

    ax.plot([GUT, GUT], [0.30, H - 0.34], color="#E3E7EC", lw=2.4, zorder=0,
            solid_capstyle="round")

    top = H
    for s, hh in zip(STEPS, heights):
        kind = _state(st, s)
        face, _, edge = C[kind]
        blk_top = top - 0.10

        # --- content ---
        def _rh(keys):
            ns = [nt[k] for k in keys if nt.get(k)]
            if not ns:
                return H1
            wide = W if len(keys) == 1 else (W - 0.11 * (len(keys) - 1)) / len(keys)
            return H2 + 0.17 * (max(textwrap.fill(n, max(14, int(wide / 0.058)))
                                    .count("\n") + 1 for n in ns) - 1)

        y = blk_top - _rh([f"{s['n']}.{i+1}" for i in range(len(s["subs"]))]
                          if s["mode"] not in ("seq", "loop") else [f"{s['n']}.1"])
        inset = 0.58 if s["mode"] == "loop" else 0.0
        ys, first_y = [], None
        if s["mode"] in ("seq", "loop"):
            for i, lab in enumerate(s["subs"]):
                k = f"{s['n']}.{i+1}"
                bh = _rh([k])
                _box(ax, X + inset, y, W - inset, bh, lab, _state(st, s, i + 1), nt.get(k))
                ys.append((y, bh))
                if first_y is None:
                    first_y = y + bh
                if i < len(s["subs"]) - 1:
                    nxt = _rh([f"{s['n']}.{i+2}"])
                    y -= VGAP + nxt
            if s["mode"] == "loop":
                lk = _state(st, s, len(s["subs"]))
                col = C[lk][2] if lk != "next" else "#A9B1BA"
                ch = X + 0.24
                y0, y1 = ys[-1][0] + ys[-1][1] / 2, ys[0][0] + ys[0][1] / 2
                ax.plot([X + inset, ch, ch], [y0, y0, y1], color=col, lw=1.8,
                        solid_joinstyle="round", zorder=2)
                ax.add_patch(FancyArrowPatch((ch, y1 - 0.002), (X + inset, y1),
                             arrowstyle="-|>", mutation_scale=11, lw=1.8,
                             color=col, zorder=2))
                ax.text(ch - 0.14, (y0 + y1) / 2, "repeat", rotation=90,
                        fontsize=7.3, color=col, ha="center", va="center")
            bot = ys[-1][0]
        else:
            n = len(s["subs"])
            keys = [f"{s['n']}.{i+1}" for i in range(n)]
            bh = _rh(keys)
            bw = (W - 0.11 * (n - 1)) / n
            for i, lab in enumerate(s["subs"]):
                _box(ax, X + i * (bw + 0.11), y, bw, bh, lab,
                     _state(st, s, i + 1), nt.get(keys[i]))
            bot, first_y = y, y + bh

        if s.get("after"):
            ak = s.get("after_fixed") or st.get(f"{s['n']}.after", kind)
            bot -= VGAP + H1
            _box(ax, X, bot, W, H1, s["after"], ak)
        if s.get("note"):
            bot -= 0.26
            ax.text(X, bot + 0.06, s["note"], fontsize=7.5, color=GREY,
                    style="italic", va="center")
        if s.get("after_note"):
            bot -= 0.24
            ax.text(X, bot + 0.06, s["after_note"], fontsize=7.4, color=GREY,
                    style="italic", va="center")

        # --- badge and title, centred on the block ---
        mid = (first_y + bot) / 2
        ax.add_patch(Circle((GUT, mid), 0.155, zorder=5,
                     facecolor=face if kind != "next" else "#FFFFFF",
                     edgecolor=edge, lw=1.5 if kind == "now" else 1.1))
        ax.text(GUT, mid, str(s["n"]), ha="center", va="center",
                fontsize=7.6, zorder=6, fontweight="bold",
                color=C[kind][1] if kind in ("now", "part") else "#A2A9B2")
        ax.text(GUT + 0.32, mid, s["title"], ha="left", va="center",
                fontsize=9.9, linespacing=1.32,
                color=INK if kind in ("now", "part") else "#A2A9B2",
                fontweight="bold" if kind in ("now", "part") else "normal")
        top -= hh

    for k, (lab, kind) in enumerate([("this notebook", "now"), ("partly, here", "part"),
                                     ("already covered", "done"), ("a later class", "next")]):
        bx = GUT - 0.15 + k * 2.45
        _box(ax, bx, -0.80, 0.34, 0.26, "", kind)
        ax.text(bx + 0.44, -0.67, lab, fontsize=8.3, va="center", color=GREY)
    ax.text(GUT - 0.15, -1.22,
            "stacked = one after the other   ·   side by side = in parallel"
            "   ·   a step that loops carries a return arrow",
            fontsize=8.1, va="center", color=GREY, style="italic")

    if title:
        ax.set_title(title, fontsize=13.2, fontweight="bold", loc="left",
                     x=0.006, pad=24 if lead else 12)
    if lead:
        ax.text(GUT - 0.15, H + 0.46, lead, fontsize=9.3, color=GREY, style="italic")
    ax.set_xlim(-0.05, X + W + 0.35); ax.set_ylim(-1.55, H + 0.92); ax.axis("off")
    plt.tight_layout()
    return ax
