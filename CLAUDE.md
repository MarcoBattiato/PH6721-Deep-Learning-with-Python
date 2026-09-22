# Working rules for this repository

PH6721 — *Deep Learning with Python* (NTU). Teaching notebooks delivered through Colab.

## 1. Literature first. Always.

**Every substantive statement in this course must come from the field's literature, not from a test
run here.** Textbooks, peer-reviewed papers, and the documentation of the library being used are the
sources. This is the standing rule, set by Marco on 2026-09-22, and it overrides any local result.

Why: a small experiment on one dataset does not generalise in machine learning, and it is far too
easy to write a confident sentence on the strength of one lucky run. The literature is where the
generalisation has already been done, and where the conditions under which a claim holds are stated.

**How to apply it:**

- **Search the literature before writing the claim**, not after. If a statement cannot be traced to
  a reputable source, it is not written — or it is written explicitly as a convention, a
  measurement on *this* dataset, or an open question, and labelled as such.
- **Own experiments are welcome on top of the literature, never instead of it.** The house style is:
  state what the literature establishes, cite it, and then demonstrate it on data the students can
  see. A measurement illustrates a documented statement; it does not license a new one.
- **A number measured here is a fact about this dataset.** "On these events, kNN lost 0.12 of ROC
  AUC to fifty noise columns" is allowed. "Nearest neighbours degrade with irrelevant features" needs
  a source, and has one.
- **Prefer:** the textbooks the course already leans on (ESL, ISLR, Bishop, Murphy, Géron, Prince,
  D2L), the primary paper for a named method, benchmark and review papers for comparative claims, and
  the scikit-learn documentation for what the code actually does. Say where each claim comes from.
- **When the literature disagrees with a local result, say so**, and report both. When the
  literature is silent, say that too — an honest gap is better than an invented rule.
- **Subagents inherit this rule.** Any agent spawned for review, drafting or checking must be told to
  work from the literature, and its findings must carry sources.

## 2. Everything else

The detailed conventions live in `Analysis/` and are not repeated here:

- `Analysis/Standards.md` — what makes material good; the rubric every notebook is judged against.
- `Analysis/StyleGuide.md` — how material is written: sections, figures, alert boxes, voice.
- `Outline/CourseOutline.md` — the agreed syllabus, the binding OBTL content, and the departures
  from it, with reasons.

Two rules worth stating here because breaking them is expensive:

- **Every number that appears in prose must be printed by a visible cell**, and must be checked
  against that cell's output before the notebook is committed.
- **Stage only the files you changed.** Other agents work in this repository at the same time; never
  `git add -A`, and never revert someone else's edit.
