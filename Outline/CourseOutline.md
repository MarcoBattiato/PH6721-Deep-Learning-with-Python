# PH6721 — Deep Learning with Python

**Course outline** — derived from the approved OBTL (`PH6721 - Annex A.pdf`, approved 16-07-2026).

12 classes × 3 hours of content (39 contact hours). Trimester 2, AY2026-2027.
Delivery: 3 Jupyter notebooks per class, one per hour (`NNA`, `NNB`, `NNC`), except where an hour's material is split across two (`01C` and `01D`).

---

## Design basis

This outline follows the approved OBTL's **Course Content** section, which defines ten thematic
blocks and is the binding specification, together with its indicative twelve-week Planned
Schedule. One deliberate departure from the Planned Schedule is documented below.

### Binding content checklist

| Block | Mandated content | Delivered in |
|---|---|---|
| 1 | AI / ML / DL overview, scientific applications | 1A |
| 1 | Scientific computing workflows, Python tools | 1B |
| 1 | Data handling and visualization | 1C |
| 2 | Regression, model fitting | 2A |
| 2 | Classification | 2B |
| 2 | Train-test splits, validation, over/underfitting | 2C |
| 2 | Bias-variance tradeoff | 3B |
| 2 | Regularization techniques | 3C |
| 2 | Performance metrics, regression and classification | 3A |
| 3 | Decision trees | 4A |
| 3 | Random forests, ensemble learning | 4B |
| 3 | Gradient boosting | 4C |
| 3 | Support vector machines | 5A |
| 3 | Kernel methods | 5B |
| 3 | Clustering techniques | 5C |
| 4 | Curse of dimensionality | 6A |
| 4 | Principal component analysis | 6A |
| 4 | Nonlinear dimensionality reduction (t-SNE, UMAP) | 6B, 6C |
| 4 | Similarity measures | **5A** (the metric, where the methods first need it) and **9A** (cosine similarity in embedding spaces) |
| 4 | Autoencoders, latent representations | 9B |
| 4 | Contrastive learning, embeddings, feature learning | 9C |
| 5 | Perceptrons, multilayer networks, activation functions | 7A |
| 5 | Universal approximation | 7A |
| 5 | Backpropagation, gradient-based optimization | 7B |
| 5 | Practical implementation of deep learning models | 7C |
| 5 | Training dynamics | 8A, 8B |
| 5 | Regularization methods for deep networks | 8C |
| 6 | Image representations, convolutions, pooling, feature maps | 10A, 10B |
| 6 | Modern CNN architectures | 10C |
| 6 | Scientific, medical, astronomical **and materials-science** imaging | 10C |
| 7 | Sequential data | 11A |
| 7 | Recurrent neural networks, LSTMs | 11A |
| 7 | Attention, self-attention, positional encoding | 11B |
| 7 | Transformer architectures **for sequence and language modeling** | 11C, with tokens/vocabulary/embeddings and the next-token objective in 12A |
| 8 | Pretraining, fine-tuning, transfer learning | 12A |
| 8 | Foundation models, multimodal learning | 12A |
| 8 | **Applications of large-scale pretrained models to scientific domains** | 12A |
| 9 | Graph-structured data, GNNs, message passing, **graph convolutions** | 12B |
| 9 | Applications to molecules, materials, biological systems, **interaction networks** | 12B |
| 10 | **AI for scientific discovery**: method selection across data modalities, model evaluation, real-world applications; course synthesis | 12C |

### Departure from the Planned Schedule

**Weeks 7, 8 and 9 are rotated.**

The approved Planned Schedule places *Representation Learning: Autoencoders and Contrastive
Learning* at Week 7, before *Neural Networks and Backpropagation* at Week 8. Autoencoders are
neural networks and contrastive learning is trained by backpropagation, so as scheduled students
would meet encoders, latent spaces and decoders a week before being told what a perceptron is or
how a gradient propagates backwards.

| Week | Approved schedule | This outline |
|---|---|---|
| 7 | Representation Learning | **Neural Networks and Backpropagation** |
| 8 | Neural Networks and Backpropagation | **Training Deep Networks** |
| 9 | Training Deep Networks | **Representation Learning** |

This preserves every topic and every ILO mapping, and produces a coherent progression: neural
networks, then how to train them, then what they learn. The Course Content section imposes no
ordering between blocks 4 and 5, so only the indicative schedule changes.

**Class 1 is delivered in four notebooks rather than three.**

The approved delivery is one notebook per contact hour. Class 1's third hour — data handling and
visualization — was written as a single notebook and came to 33 subsections and roughly 150 minutes
of material, which is neither teachable in an hour nor navigable as a reference afterwards. It is
split at the point where no section refers across the boundary:

| Hour | Approved shape | This outline |
|---|---|---|
| 3 | one notebook, `01C` | **`01C` — pandas, loading, anatomy, missing values, summaries** |
| 3 | — | **`01D` — distributions, relationships, groups, correlation, pitfalls** |

No content is added or dropped and no ILO mapping changes; the hour's material is the same material
in two files. The split is recorded here rather than left silent because the *"one notebook per
hour"* convention is otherwise load-bearing — `NNA`/`NNB`/`NNC` is how every other class is
addressed, and `01D` is the one exception to it.

Class 1 remains over its three-hour budget after the split. That is a separate problem, tracked in
`Analysis/Timing.md`, and it is not solved by how the material is filed.

**`04A` teaches one impurity measure, not two.**

The Class 4 row above originally read *"recursive partitioning, entropy, information gain,
pruning"*. `04A` uses the Gini index throughout and does not mention entropy at all.

The comparison was written, measured and then cut. It is a technical aside about an implementation
detail of a method that is not the course's subject, and its conclusion is that the choice does not
matter: the two criteria rank a pair of splits differently in about 2% of cases, and the difference
is invisible in accuracy. It cost teaching time it could not repay, and its likely effect on a
student was uncertainty about which measure to use. Nothing in the OBTL's Course Content requires
a particular impurity measure — block 3 asks for decision trees — so no mandated content is lost.

The material is kept, unpublished, at `discarded/04A-Discarded-GiniVsEntropy.ipynb`.

### Notes on scope

- The course title emphasises deep learning, while the approved Course Content mandates a
  substantial classical machine learning foundation in blocks 2–4. The early classes are
  therefore framed explicitly as building toward deep learning, so students understand why they
  precede it. Neural networks begin in Class 7.
- Isomap, locally linear embedding and Laplacian eigenmaps are **not** required by this OBTL
  (Week 6 names only PCA, t-SNE and UMAP). They appear briefly as context in 6B rather than as
  taught methods.
- A **dedicated NLP class** is not in this OBTL, and BERT is not taught as an architecture. But
  block 7's wording is *"transformer architectures for sequence and language modeling"*, and
  language modelling cannot be stated without a token, a vocabulary, an embedding table and a
  next-token objective. Those are taught in `12A`, where they are needed anyway: "pretraining" is
  meaningless until the student knows what objective is being pretrained on. A free second payoff —
  word-embedding geometry is the canonical demonstration that a learned space has metric structure,
  which is what `09A` is about.
- The OBTL's block 9 phrase *"interaction networks"* sits inside an **application** list —
  "molecules, materials, biological systems, and interaction networks" — so it is read here as a
  data domain (protein–protein interaction networks, reaction networks), not as the Battaglia et al.
  architecture. `12B` satisfies it with a named example rather than a second architecture.
- K-nearest neighbours is not mandated. It is retained briefly in 5A as the simplest way to
  introduce distance-based reasoning before support vector machines.

---

## Class-by-class

### Part I — Foundations (Classes 1–3)

#### Class 1 — Introduction to AI for Science and Scientific Python `[wk 1]`
| | Notebook | Content |
|---|---|---|
| H1 | `01A` | What AI, ML and DL are; ML as a toolbox; inductive bias; supervised, unsupervised and representation learning; the ML workflow |
| H2 | `01B` | Jupyter; NumPy arrays, indexing, slicing, shapes; vectorization; broadcasting |
| H3 | `01C` | pandas; loading data; dataset anatomy; missing values; summaries |
| H3 (cont.) | `01D` | distributions, relationships, groups; correlation; a mini case study; common pitfalls |

**Status: built.**

#### Class 2 — Learning from Data: Regression, Classification and Generalization `[wk 2]`
| | Notebook | Content |
|---|---|---|
| H1 | `02A` | Supervised learning framework; linear regression; least squares; least squares as Gaussian maximum likelihood |
| H2 | `02B` | Binary classification; logistic regression; decision boundaries; cross-entropy loss |
| H3 | `02C` | Train/validation/test; cross-validation; **data leakage**; overfitting and underfitting; reproducibility |

**Status: built.**

#### Class 3 — Bias-Variance Tradeoff, Regularization and Metrics `[wk 3]`
| | Notebook | Content |
|---|---|---|
| H1 | `03A` | Regression metrics (MSE, MAE, R²); classification metrics; confusion matrix, precision, recall, F1, ROC, AUC; class imbalance |
| H2 | `03B` | Polynomial regression → the bias-variance tradeoff, developed as one continuous narrative |
| H3 | `03C` | **Feature scaling** (why the coefficient size must be comparable); L1 and L2 regularization; ridge and lasso; feature selection; hyperparameter search |

**Status: built.**

### Part II — Classical Machine Learning (Classes 4–5)

#### Class 4 — Decision Trees, Random Forests and Gradient Boosting `[wk 4]`
| | Notebook | Content |
|---|---|---|
| H1 | `04A` | Decision trees: recursive partitioning, impurity, information gain, pruning |
| H2 | `04B` | Random forests: bagging, ensembles, feature importance and its pitfalls; **extremely randomised trees as a two-line corollary of the decorrelation argument** |
| H3 | `04C` | Gradient boosting; XGBoost; when boosting beats deep learning on tabular scientific data. **Use `HistGradientBoostingClassifier` as the primary demo** — LightGBM's algorithm, in the Colab base image, and it handles NaNs and categorical columns natively. **Partial dependence and ICE** (one `PartialDependenceDisplay` call), and **SHAP named** if not taught |

> `04C`'s headline claim — *when boosting beats deep learning on tabular data* — is a genuine
> strength of this course and is made by none of the reference texts. Anchor it to Grinsztajn,
> Oyallon & Varoquaux (NeurIPS 2022) and Shwartz-Ziv & Armon (2022), or it reads as folklore.
>
> `04B` §7 demolishes impurity importance and half-demolishes permutation importance, leaving the
> student with a *ranking* and no way to ask **how** a feature acts. That is what partial dependence
> is for, and it is one call.

**Status: `04A` and `04B` built.**

#### Class 5 — Support Vector Machines, Kernel Methods and Clustering `[wk 5]`
| | Notebook | Content |
|---|---|---|
| H1 | `05A` | Distance and the metric (and that distances need scaling, where trees did not); k-nearest neighbours; margins and support vectors; **the soft margin and `C`**; **hinge loss** |
| H2 | `05B` | Kernel methods; the kernel trick; RBF kernels; kernel ridge regression; **the Gaussian process posterior mean is kernel ridge regression — the new object is the predictive variance** |
| H3 | `05C` | Clustering: k-means, hierarchical, DBSCAN; **Gaussian mixtures as soft k-means**; choosing k honestly (inertia, silhouette, and that the objective cannot choose it); phase discovery and anomaly detection |

> **Class 5 has a spine, and it is worth stating in the hour:** *learning from distances — the
> supervised half, then the unsupervised half.* An RBF kernel $\exp(-\gamma\lVert x-x'\rVert^2)$
> and DBSCAN's $\varepsilon$-ball are the same neighbourhood idea at two scales. Opening `05C` with
> "now for something different" throws that away.
>
> `05A` carries the metric because `05C`'s DBSCAN, `06B`'s t-SNE and `06C`'s UMAP all need it first,
> and the OBTL's "similarity measures" is mapped to `09A`, three classes too late. `09A` is
> therefore re-scoped to *cosine similarity in learned embedding spaces*, which is what it is
> actually for.
>
> `05A`'s soft margin and `C` are not optional garnish: without them the SVM is **the only model in
> the course with no flexibility dial**, breaking a spine built five times over (`02C`'s degree,
> `03B`, `03C`'s $\alpha$, `04A`'s depth and `ccp_alpha`, `04B`'s `max_features`). Present it as
> ISLR §9.5 does — *loss + penalty*, hinge where logistic regression uses log loss, same L2 penalty
> — so it arrives as a variation on `02B` and `03C` rather than as a new machine. That also
> discharges `03A` §8's promise about SVM scores in the same figure.

> **Midterm — Week 6, covering Classes 1–5** (per Appendix 2).

### Part III — Dimensionality Reduction (Class 6)

#### Class 6 — Dimensionality Reduction: PCA, t-SNE and UMAP `[wk 6]`
| | Notebook | Content |
|---|---|---|
| H1 | `06A` | Curse of dimensionality — **argued through `05A`'s kNN rather than abstractly**; the manifold hypothesis; **PCA**: covariance, eigenvectors, explained variance, **and why the features must be scaled first** (the exact inversion of `04A` §11.1, and a callback to `03C` §2); components are unique only up to sign. **PCA is diagonalising a symmetric positive-semidefinite matrix — normal modes, principal axes of the inertia tensor** |
| H2 | `06B` | **t-SNE**: neighbour embeddings, perplexity; brief context on Isomap and LLE |
| H3 | `06C` | **UMAP**; comparing methods; reading embedding plots critically. *`umap-learn` is the one dependency in the course with a live numba/numpy conflict risk — give it the `try`/`except` fallback of `01C` §3.2* |

### Part IV — Deep Learning Foundations (Classes 7–9)

#### Class 7 — Neural Networks and Backpropagation `[wk 8 → 7]`
| | Notebook | Content |
|---|---|---|
| H1 | `07A` | Perceptron; limits of linear models; MLPs; activation functions; universal approximation |
| H2 | `07B` | Loss surfaces; gradient descent (and why badly scaled features make it slow); **backpropagation**; the chain rule and computational graphs |
| H3 | `07C` | PyTorch: tensors, autograd, modules; **`Dataset`/`DataLoader`, mini-batching, device placement**; a first network trained end to end. **Autograd differentiates with respect to *inputs* too** — forces from an energy model, sensitivity, differentiable simulation |

> `07C`'s training loop is an **API**, in the same sense the section numbers are: Classes 8 to 12
> reuse it verbatim. Mini-batching is a prerequisite for `08A`'s SGD and momentum, and device
> placement is a prerequisite for anything in Classes 10 to 12 running on Colab at all. It is
> recorded in *Recurring notebook conventions* below.

#### Class 8 — Training Deep Networks `[wk 9 → 8]`
| | Notebook | Content |
|---|---|---|
| H1 | `08A` | Optimizers: SGD, momentum, Adam; learning rates, schedules and **warmup**; **AdamW — weight decay is not L2 under Adam**, and `08C` teaches weight decay, so the interaction is a live trap |
| H2 | `08B` | Training dynamics: initialization, vanishing and exploding gradients, batch normalization, **layer normalization** (`11C`'s residual blocks are defined by it, and BN degrades at the small batch sizes expensive scientific data forces); **skip connections pointed forward to `10C` as the direct answer to vanishing gradients** |
| H3 | `08C` | Regularization for deep networks: dropout, weight decay, early stopping, data augmentation. **Double descent.** **Hyperparameter practice for deep nets, stated as a conflict** with `02C`/`03C`. **Uncertainty**: temperature scaling, deep ensembles, MC dropout, conformal prediction named. **Run-to-run variance** — a single training run is a sample, not a measurement |

> **`08C`'s double descent is not an extra; it repairs something.** `03B` teaches the bias–variance
> U-curve and `02C` teaches it as the reason to hold data out. Class 8 then trains a model with more
> parameters than data to near-zero training error and never says why `03B`'s law did not fire —
> six weeks of a taught statement left standing without its exception. Forward-flag it from `07A`,
> immediately after universal approximation.
>
> **`08C`'s uncertainty block discharges `03A` §8's promise** that deep networks are the
> over-confident case, which no content row currently pays.
>
> **The hyperparameter item is a conflict, not an omission.** `02C` and `03C` teach k-fold CV and
> `GridSearchCV` as *the* model-selection procedure; deep learning quietly abandons both for a
> single validation split, random search and early stopping. Unsaid, students will run 5-fold CV on
> a CNN and lose a week.

#### Class 9 — Representation Learning: Autoencoders and Contrastive Learning `[wk 7 → 9]`
| | Notebook | Content |
|---|---|---|
| H1 | `09A` | What a learned representation is; similarity measures; cosine distance; embedding spaces |
| H2 | `09B` | **Autoencoders**: encoder, latent space, decoder; undercomplete and denoising; autoencoders versus PCA; **reconstruction error as an anomaly detector** — discharging `05C`'s promise, and the basis of model-independent new-physics searches |
| H3 | `09C` | **Contrastive learning**: positive and negative pairs; embeddings; self-supervision |

### Part V — Modern Architectures (Classes 10–12)

#### Class 10 — Deep Learning for Images: Convolutional Neural Networks `[wk 10]`
| | Notebook | Content |
|---|---|---|
| H1 | `10A` | Images as tensors; why fully connected layers fail on images; convolution — **and that a convolution *is* the imposition of translation equivariance**, which is the `01A` §2.6 inductive-bias thread made concrete |
| H2 | `10B` | Pooling; feature maps; receptive fields; what filters learn |
| H3 | `10C` | Modern CNN architectures **and residual connections**; **transfer learning, taught here and only here**; dense prediction and U-Net; Grad-CAM; microscopy, medical imaging, astronomy, materials |

#### Class 11 — Sequence Models and Transformers `[wk 11]`
| | Notebook | Content |
|---|---|---|
| H1 | `11A` | Sequential scientific data; **a persistence/ARMA baseline first, so the network has something to beat**; **RNNs**, hidden states, vanishing gradients, **gradient clipping**; **LSTM** and gating; **1D CNNs for sequences**, often the right answer for spectra and sensor traces and far cheaper |
| H2 | `11B` | **Attention** and self-attention; queries, keys, values; positional encoding — **needed precisely because self-attention is permutation-equivariant**, without which the encoding reads as an arbitrary hack |
| H3 | `11C` | The **transformer** architecture; multi-head attention; residual stream |

#### Class 12 — Foundation Models, Transfer Learning, GNNs and Synthesis `[wk 12]`
| | Notebook | Content |
|---|---|---|
| H1 | `12A` | Pretraining and fine-tuning; **foundation models**; multimodal learning; **scaling**; **tokens, vocabulary, embedding tables and the next-token objective** |
| H2 | `12B` | Graph-structured data; **graph neural networks**; **message passing** *(a ~20-line layer in plain PyTorch — `torch-geometric` installs are slow and version-fragile on Colab)*; **graph convolutions**; molecules, materials, biological systems, interaction networks |
| H3 | `12C` | Choosing a method for a data modality; course synthesis |

**Course synthesis (12C):** tabular → trees and boosting · high-dimensional → PCA and manifold
methods · images → CNNs · sequences → RNNs and transformers · graphs → GNNs.

**`12C` is block 10, not a recap.** The modality map above is better than any of the reference texts
offers — none of them closes with one — but it is a modality table, not a discovery framework. Four
rows complete it, a slide each, all inside block 10's own title *AI for Scientific Discovery*:

| If you have… | Reach for |
|---|---|
| a simulator you can query | a surrogate / emulator, and active learning |
| small data needing error bars | a Gaussian process, or a deep ensemble |
| a known symmetry | an equivariant architecture |
| a wanted *equation*, not a prediction | symbolic regression — SINDy, PySR, AI Feynman |

Plus one sentence on **extrapolation and domain shift** — `04A` taught that trees cannot
extrapolate, deep networks cannot reliably either, and that governs whether a materials model can be
trusted off its training chemistry — and one on **simulation-based / likelihood-free inference**,
which is how much of HEP and cosmology now uses machine learning.

> **Final exam — Week 13, covering all material** (per Appendix 4).

---

## Assessment (per approved OBTL)

| Component | Weight | Timing | Notes |
|---|---|---|---|
| Class participation (Wooclap) | 10% | Weekly | 5–10 questions per lecture; `min(10x/7, 1)` scoring |
| Midterm | 10% | Week 6 | Classes 1–5; restricted open, one A4 double-sided sheet |
| Final project | 40% | — | Presentation 70% + interactive notebook 30%; topic due end of Week 4 |
| Final exam | 40% | Week 13 | All material; restricted open, one A4 double-sided sheet |

Project groups are roughly 5 students. Topics should be consulted on around Week 3 and confirmed
by end of Week 4. The notebook component is graded on being executable and bug-free, properly
documented, and on demonstrating the methods well.

## Defects noted in the approved OBTL

For correction at the next revision. None affect teaching.

1. The assessment table maps the Final Project to **ILO 1-5**, but the course defines only four
   ILOs. The Learning and Teaching Approach section repeats "(ILO 1–5)".
2. **Appendix 1** states "you get the full **15%** for in-class participation" while the
   component is worth 10%.
3. **Appendix 3** refers to "peer evaluation above", but no peer evaluation scheme is described.
4. The **NTU2025 education initiatives** table has nothing selected.
5. The Course Aims are written throughout in "AI for scientific applications" language, which
   sits oddly beneath a title of "Deep Learning with Python".

---

## Threads that run across classes

Recorded so that a notebook written in Class 10 knows what Class 2 started, and so that a later
reviewer does not read a deliberate arrangement as an omission.

### Uncertainty — the one thread the course was missing

No model in the original outline reported its own uncertainty, in a course whose own thesis
(`02A` §6.1) is that *"regression here is parameter estimation"*. A physics MSc is expected to write
$k = 24.9 \pm 0.4\ \mathrm{N/m}$. Three places now carry it, at rising cost:

1. **`02A` §7.2.1** — `np.polyfit(..., cov=True)`, propagated to the spring constant. Built.
2. **`05B`** — the Gaussian process posterior mean *is* kernel ridge regression, which `05B` already
   plans; the only new object is the predictive variance. GPs are the dominant ML method in physics
   and chemistry — interatomic potentials, Bayesian optimisation of experiments, simulation
   emulators.
3. **`08C`** — temperature scaling, deep ensembles, MC dropout, conformal prediction named. This is
   what discharges `03A` §8's promise that deep networks are the over-confident case.

### Equivariance and symmetry — one principle, three homes

Not a block. `10A` (convolution is translation equivariance), `11B` (self-attention is permutation
equivariant, which is *why* positional encoding exists) and `12B` (message passing is permutation
equivariance on graphs, with SchNet / NequIP / MACE as the mandated payoff). Three architectures
that otherwise look unrelated become one idea, and it extends `01A` §2.6's inductive-bias thread.

### The flexibility dial

Built five times — `02C`'s degree, `03B`, `03C`'s $\alpha$, `04A`'s depth and `ccp_alpha`, `04B`'s
`max_features` — and it must not break at `05A`. See the note under Class 5.

### Loss functions are inherited, deliberately

Classes 7 onward never assign losses to networks: MSE comes from `02A`, cross-entropy from `02B` §5
via the Bernoulli MLE, and softmax from `02B` §10.2. Prince spends a whole chapter on this; here it
is a payoff on work already done. **This is a choice, not an oversight.** `07A`/`07C` still owe the
statement that a classification network ends in a softmax layer.

---

## Ordering decisions that depart from the textbooks, and why they stay

Recorded under Standard I.3 so that a later reviewer does not "fix" them.

1. **Bias–variance arrives late**, after the U-curve that motivates it, rather than abstractly as in
   ISLR ch. 2.
2. **Regularization is motivated by bias–variance**, not by subset selection as in ISLR ch. 6. More
   honest about what the penalty does.
3. **Leakage gets a full hour, before any metric or penalty.** No textbook gives it that position;
   it is the failure mode students actually hit.
4. **Unsupervised before neural networks is forced, not convenient.** `09B` plans "autoencoders
   versus PCA", which is impossible if PCA comes after Class 9.
5. **Trees → SVM matches ISLR** (ch. 8 → ch. 9). Géron's SVM-first is book organisation; following
   it would be worse, because `04A` §11.2 sets up kernels by showing a tree's staircase failing on a
   circle.
6. **`09C` is planned around a non-image modality** — spectra, light curves, sensor traces. The
   canonical contrastive demonstration is SimCLR-style image augmentation, which needs Class 10.
   The OBTL does not require images there, and non-image data suits this audience better.

### Exclusions, named so they read as choices

Keep excluding, and say so in `12C`: AdaBoost as a historical entry; SVM regression (`05B`'s kernel
ridge regression is the better vehicle — *say so*); the representer theorem as a theorem, though the
statement $f(x)=\sum_i \alpha_i k(x, x_i)$ is one line and is a Green's-function statement in a
physicist's own language; spectral clustering; kernel PCA (one sentence — it is literally Class 5
composed with Class 6); random projections; stacking; Isomap/LLE; BART; reinforcement learning.

Two the outline was silent on rather than defending:

- **Generative models — VAE, GAN, diffusion.** Excluded as a taught block; **named in `12C`**.
  `09B`'s autoencoder is one sentence from a VAE, and diffusion is now the dominant generative
  family in the physical sciences (lattice-field sampling, RFdiffusion, MatterGen). Otherwise
  `12C`'s map has a hole where a quarter of modern deep learning sits.
- **PINNs and neural operators — the biggest genuine absence for this audience**, and correctly
  excluded as a block: an honest treatment needs 45–60 minutes and there is no free hour. None of
  the reference texts covers them either, which is precisely where *standard DL textbook* and *DL
  for physicists* diverge. Three cheap substitutes: a 15-minute demo in `07C` riding on its
  autograd-with-respect-to-inputs item; **an advertised project track** — the project is 40% and
  topics are due end of Week 4, so this costs zero contact hours and is where it belongs; and a
  slide in `12C`.

---

## Recurring notebook conventions

- Header block with course code, class/notebook/hour, instructor and contact details
- **Learning objectives** cell opening each notebook
- Numbered sections with `#` / `##` headings
- Inline mini-exercises in `<div class="alert alert-success">` boxes
- `STUDENT WORKSPACE` code cells following each exercise
- Matplotlib-drawn conceptual figures rather than external images
- **Key takeaways** and **Optional preparation for the next notebook** closing cells
- Recurring prompts on using an LLM to write and check scientific code

### Cells that must ship without output

Executing a notebook stores every result, which silently gives away the answer to any cell the
student is meant to work out first. Such cells carry a **tag** in their metadata, and the markdown
cell immediately above carries the matching **banner**:

| Tag | Banner in the markdown above | Why |
|---|---|---|
| `predict` | **Think about your answer before running this cell.** | The student should predict the result first |
| `run-fresh` | **Run this cell yourself. Its output is not stored in the notebook.** | A stored output would mislead — a setup check must prove *their* environment works |

The tag is what the tooling acts on; the banner is what the student reads. Neither substitutes for
the other, and a validator reports any cell that has one without the other, so the two cannot
drift apart.

**This runs after every execution**, because executing re-stores the outputs:

```
python notebook_markers.py clear     # clear tagged outputs, strip execution timings, validate
python notebook_markers.py check     # validate only; exits non-zero on any mismatch
```

The same step strips the per-cell `execution` timing metadata that nbconvert injects, which
otherwise changes on every run and makes notebook diffs unreadable.

### Section numbers are an API

Notebooks cite one another by section number — `02A` §8.4, or a bare §6.1 within a notebook — and
`00B`'s symbol index is one long table of such citations. Renumbering or retitling a section
silently breaks every reference to it, and a reader only finds out by following one.

```
python check_section_refs.py check   # every citation resolves; exits non-zero otherwise
python check_section_refs.py list     # the sections each notebook defines
```

It recognises the four forms already in use (`02A` §8.4, `02A` section 8.4, §6.1, section 9.4) in
backticks or `<code>` tags. A bare number means the current notebook, falling back to any notebook
named in the same cell — which is what makes `00A`'s question-to-section table resolve against
`00B`. A citation to a notebook the outline plans but that is not written yet is reported as a
note, not a failure, so forward references such as `02B`'s pointer to `03C` are allowed.

## Technical targets

- Notebooks must run on **Google Colab** (per the OBTL's Technology-Enhanced Learning section)
- Guarded `pip install` cells for anything outside the Colab base image
  (`umap-learn`, `xgboost`, `rdkit`, `torch-geometric`)
- Datasets loaded from URL or generated in-notebook, so nothing depends on local files
- Every notebook must run top to bottom without error, and must validate against current
  `nbformat` so it opens in Colab
- **Anything that trains must reach a visible result in roughly one to two minutes on a free Colab
  runtime.** This is a design constraint, not a discovery to be made during authoring: it dictates
  the dataset for the CNN in Class 10 (FashionMNIST or a CIFAR-10 subset), for the transformer in
  Class 11 (a small character-level corpus) and for the GNN in Class 12 (a QM9 subset), and it
  constrains what those classes can claim to have demonstrated.
- **`07C`'s training loop is a reusable template.** Classes 8 to 12 use it verbatim rather than
  writing their own. It is an API in the same sense as the section numbers below.

---

## Open, for Marco

Two decisions worth taking explicitly before `07A` is drafted, because no later trim recovers them.

**1. Competence or literacy, per class.** The Class 7–12 material maps to roughly sixty numbered
D2L sections in eighteen contact hours — about three times D2L's own pace. A defensible split:
Classes 7–8 competence · Class 9 competence · Class 10 competence on transfer learning, literacy on
architectures · Classes 11–12 literacy. Writing it down also protects the Week 13 exam from asking
Class 11 questions the hours could not support.

**2. Classes 7–12 should be written at a lower density than Classes 1–4.** `Analysis/Timing.md`
records the mechanism: *notebooks acquire minutes during review rounds, because review adds
explanation and almost never removes any.* Classes 1 and 2 are already over budget by that route.

On length generally: the current plan is to build each class fully and then prune by **marking
sections optional**, as `03A` §§8–9 and `04A` §§3.2, 4.1 already do, rather than by writing thin.
Class 11 is the densest hour in the course — `11A` alone is roughly forty pages of D2L — and is the
first place that pruning should look. Two content-neutral recoveries are already made above:
scaling moved from `11C` to `12A`, where it belongs as a foundation-model fact, and transfer
learning taught once in `10C` rather than twice.
