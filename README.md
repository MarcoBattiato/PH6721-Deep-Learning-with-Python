# PH6725 — Artificial Intelligence for Science

Course materials for **PH6725**, Nanyang Technological University, School of Physical and
Mathematical Sciences. 12 classes × 3 hours.

**Instructor:** Marco Battiato — marco.battiato.teaching@gmail.com

---

## Running the notebooks

Every notebook runs in **Google Colab** with no local installation. Click the
*Open in Colab* badge at the top of any notebook, then choose `Runtime → Run all`.

Notebooks load their data from public URLs or generate it in-code, so nothing needs to be
downloaded or uploaded first.

To run locally instead, you need Python 3.8 or newer with `numpy`, `pandas`, `matplotlib`,
`scikit-learn` and `seaborn`. Later classes additionally need `torch`, `umap-learn`, `xgboost`
and `rdkit`; those notebooks install what they need in a guarded cell.

## Contents

| Notebook | Topic |
|---|---|
| `Classes/00-test_python_jupyter` | Check that Python and Jupyter work |
| `Classes/01P-IntroToPython` | Python crash course (optional, for those new to Python) |
| **Class 1 — Introduction to AI for Science and Scientific Python** | |
| `Class_1/01A-IntroductionToAIForScience` | What AI, ML and DL are; the ML workflow |
| `Class_1/01B-PythonScientificComputing` | NumPy, vectorization, broadcasting |
| `Class_1/01C-DataHandlingAndVisualization` | pandas, exploratory data analysis, plotting |
| **Class 2 — Regression, Classification and Scientific Programming** | |
| `Class_2/02A-RegressionAndSupervisedLearning` | Supervised learning framework; linear regression |

The full 12-class plan is in [`Outline/CourseOutline_v2.md`](Outline/CourseOutline_v2.md).

## Working with the notebooks

Exercises appear in green boxes, each followed by a `STUDENT WORKSPACE` cell to write your
solution in. Edits you make in Colab are **not** saved back to this repository — use
`File → Save a copy in Drive` to keep your work.

## A note on the course administration files

The approved OBTL and the outline `.docx` files are excluded from this repository by
`.gitignore`. They contain internal approval records and colleagues' contact details, and should
not be published. Remove those lines from `.gitignore` only if this repository is private and you
are certain that is appropriate.
