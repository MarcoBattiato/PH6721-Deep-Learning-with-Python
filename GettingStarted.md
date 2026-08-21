# Getting to the course notebooks

**PH6721 — Deep Learning with Python** · NTU SPMS · Trimester 2, AY2026–27

Everything in this course runs in your browser through Google Colab. There is nothing to
install, and it works the same on Windows and on a Mac.

---

## Before you start

You need two things, and only two:

- **A Google account.** Your NTU account may work, depending on how it is configured. If it does
  not, any personal Gmail account is fine — Colab is free.
- **A web browser.** Google Chrome is the most reliable choice on both Windows and macOS. Edge,
  Firefox and Safari all work too.

> **You do not need** Python installed on your computer. Anaconda. Jupyter. A GitHub account. A
> fast machine. None of it — the code runs on Google's servers, not yours.

---

## The five steps

**1. Sign in to Google.**
Go to [colab.research.google.com](https://colab.research.google.com) and sign in. Do this first —
if you are already signed in when you open a notebook, everything afterwards is one click instead
of three.

**2. Open the course page.**
All the material lives at
[github.com/MarcoBattiato/PH6721-Deep-Learning-with-Python](https://github.com/MarcoBattiato/PH6721-Deep-Learning-with-Python).
Bookmark it. This page is always the current version — when a notebook is corrected or a new
class is added, it appears here automatically and you do not need a new link.

**3. Click into a notebook, then click the badge.**
Open the `Classes` folder, then the class you want, then the notebook file. GitHub shows the
notebook as a static page — readable, but nothing runs. At the very top is an **Open in Colab**
badge. Click it and the notebook opens in Colab, ready to run. You can also use the direct links
below.

**4. Dismiss the warning.**
Colab will say *"Warning: This notebook was not authored by Google."* This appears for every
notebook that did not come from Google, including all of ours. Click **Run anyway**.

**5. Run it.**
From the menu, choose **Runtime → Run all**. Every cell executes from the top; a Class 1 notebook
takes well under a minute. To run cells one at a time instead — which is how you should work
through them in class — click a cell and press <kbd>Shift</kbd>+<kbd>Enter</kbd>.

---

## Keeping your work

This is the one thing people get caught by, so it is worth reading twice.

When you open a notebook from the course page, Colab gives you a **temporary copy**. You can type
in it, change the code, run whatever you like — none of it affects the course material, and none
of it is visible to anyone else.

> ⚠️ **Your changes are not saved automatically.** Close the tab, or leave it idle for about 90
> minutes, and your edits are gone. The notebook has no memory of you between sessions.
>
> To keep anything, choose **File → Save a copy in Drive**. That puts your own version in your
> Google Drive, under a folder called *Colab Notebooks*, and from then on it saves as you work.

Do this at the *start* of a session you intend to write in, not at the end. It costs one click and
saves an evening.

If you press Save (<kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>S</kbd>) on a notebook opened from the course
page, Colab will tell you it cannot save there and offer to make the Drive copy for you. That
message is expected, not an error.

---

## Going straight to a class

Each link opens that notebook directly in Colab.

### Setup and Python refresher

| | Notebook | |
|---|---|---|
| `00` | [Check your setup](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/00-test_python_jupyter.ipynb) | Confirm Python and Jupyter are working |
| `01P` | [Python crash course](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/01P-IntroToPython.ipynb) | Optional — start here if Python is new to you |

### Class 1 · Introduction and Scientific Python

| | Notebook | |
|---|---|---|
| `01A` | [Introduction to AI for Science](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/Class_1/01A-IntroductionToAIForScience.ipynb) | What AI, ML and deep learning actually are |
| `01B` | [Python and Scientific Computing](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/Class_1/01B-PythonScientificComputing.ipynb) | NumPy, vectorization, broadcasting |
| `01C` | [Data Handling and Visualization](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/Class_1/01C-DataHandlingAndVisualization.ipynb) | pandas, exploring data, plotting |

### Class 2 · Learning from Data

| | Notebook | |
|---|---|---|
| `02A` | [Regression and Supervised Learning](https://colab.research.google.com/github/MarcoBattiato/PH6721-Deep-Learning-with-Python/blob/main/Classes/Class_2/02A-RegressionAndSupervisedLearning.ipynb) | Fitting models, least squares, residuals |

Later classes appear on the course page as we reach them.

---

## Windows and Mac

Colab runs in a browser, so almost everything is identical on both. There are three differences
worth knowing.

| To do this | Windows | macOS |
|---|---|---|
| Run every cell | <kbd>Ctrl</kbd>+<kbd>F9</kbd> | <kbd>⌘</kbd>+<kbd>F9</kbd> |
| Run the current cell, stay on it | <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | <kbd>⌘</kbd>+<kbd>Enter</kbd> |
| Open a link in a new tab | <kbd>Ctrl</kbd>+click | <kbd>⌘</kbd>+click |
| Right-click a cell | Right-click | <kbd>Control</kbd>+click, or a two-finger tap |

<kbd>Shift</kbd>+<kbd>Enter</kbd> — run a cell and move to the next — is the same on both, and is
the one you will use most.

Every menu path in this guide (**Runtime → Run all**, **File → Save a copy in Drive**) is
identical on both platforms, so when in doubt, use the menu rather than a shortcut.

---

## If something goes wrong

**"Cannot save changes" when I press Save.**
Expected. You are looking at the shared course copy, which you cannot write to. Choose
**File → Save a copy in Drive** to get your own.

**A cell fails with `NameError` or `not defined`.**
Almost always because earlier cells have not been run in this session. Notebooks run top to bottom
and each cell depends on the ones above it. Use **Runtime → Run all** and try again.

**Everything I ran has disappeared.**
The runtime disconnected — this happens after roughly 90 minutes idle, or 12 hours at most.
Nothing is broken; run the notebook again from the top.

**The notebook asks for input and nothing happens.**
Some cells in the Python crash course ask you to type an answer. A small text box appears under
the cell — click into it, type, and press <kbd>Enter</kbd>. Until you do, the notebook waits.

**My NTU Google account will not open Colab.**
Some NTU accounts have Colab restricted. Sign in with a personal Gmail account instead; there is
no difference in what you can do.

**Something in a notebook looks wrong.**
Please tell me — errors, typos, cells that will not run. Email
<marco.battiato.teaching@gmail.com> with the notebook name and which section. Corrections go up on
the course page and you get them automatically next time you open it.

---

## What you can and cannot change

You can do anything you like inside your own copy of a notebook: edit code, break it, rewrite it,
add cells. Experimenting is the point, and there is no way to damage the course material by doing
it.

What you cannot do is alter the shared version. The course page is read-only to everyone but me,
so your work stays yours and everyone else keeps a clean copy. The only thing at risk is your own
unsaved work — see *Keeping your work* above.

---

PH6721 Deep Learning with Python · Marco Battiato · <marco.battiato.teaching@gmail.com>
