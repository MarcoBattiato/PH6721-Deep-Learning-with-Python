# PH6721 — Deep Learning with Python

**Course outline** — derived from the approved OBTL (`PH6721 - Annex A.pdf`, approved 16-07-2026).

12 classes × 3 hours of content (39 contact hours). Trimester 2, AY2026-2027.
Delivery: 3 Jupyter notebooks per class, one per hour (`NNA`, `NNB`, `NNC`).

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
| 4 | Similarity measures | 9A |
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
| 6 | Scientific, medical, astronomical imaging | 10C |
| 7 | Sequential data | 11A |
| 7 | Recurrent neural networks, LSTMs | 11A |
| 7 | Attention, self-attention, positional encoding | 11B |
| 7 | Transformer architectures | 11C |
| 8 | Pretraining, fine-tuning, transfer learning | 12A |
| 8 | Foundation models, multimodal learning | 12A |
| 9 | Graph-structured data, GNNs, message passing | 12B |
| 9 | Applications to molecules, materials, biological systems | 12B |
| 10 | Method selection across data modalities; course synthesis | 12C |

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

### Notes on scope

- The course title emphasises deep learning, while the approved Course Content mandates a
  substantial classical machine learning foundation in blocks 2–4. The early classes are
  therefore framed explicitly as building toward deep learning, so students understand why they
  precede it. Neural networks begin in Class 7.
- Isomap, locally linear embedding and Laplacian eigenmaps are **not** required by this OBTL
  (Week 6 names only PCA, t-SNE and UMAP). They appear briefly as context in 6B rather than as
  taught methods.
- Tokenization, BERT and a dedicated NLP class are **not** in this OBTL. Sequence modelling is
  covered under block 7 without a language-processing focus.
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
| H3 | `01C` | pandas; loading data; dataset anatomy; missing values; summaries; distributions, relationships, groups; correlation |

**Status: built.**

#### Class 2 — Learning from Data: Regression, Classification and Generalization `[wk 2]`
| | Notebook | Content |
|---|---|---|
| H1 | `02A` | Supervised learning framework; linear regression; least squares; least squares as Gaussian maximum likelihood |
| H2 | `02B` | Binary classification; logistic regression; decision boundaries; cross-entropy loss |
| H3 | `02C` | Train/validation/test; cross-validation; **data leakage**; overfitting and underfitting; reproducibility |

**Status: `02A` built.**

#### Class 3 — Bias-Variance Tradeoff, Regularization and Metrics `[wk 3]`
| | Notebook | Content |
|---|---|---|
| H1 | `03A` | Regression metrics (MSE, MAE, R²); classification metrics; confusion matrix, precision, recall, F1, ROC, AUC; class imbalance |
| H2 | `03B` | Polynomial regression → the bias-variance tradeoff, developed as one continuous narrative |
| H3 | `03C` | L1 and L2 regularization; ridge and lasso; feature selection; hyperparameter search |

### Part II — Classical Machine Learning (Classes 4–5)

#### Class 4 — Decision Trees, Random Forests and Gradient Boosting `[wk 4]`
| | Notebook | Content |
|---|---|---|
| H1 | `04A` | Decision trees: recursive partitioning, entropy, information gain, pruning |
| H2 | `04B` | Random forests: bagging, ensembles, feature importance and its pitfalls |
| H3 | `04C` | Gradient boosting; XGBoost; when boosting beats deep learning on tabular scientific data |

#### Class 5 — Support Vector Machines, Kernel Methods and Clustering `[wk 5]`
| | Notebook | Content |
|---|---|---|
| H1 | `05A` | Distance-based reasoning; k-nearest neighbours; margins and support vectors |
| H2 | `05B` | Kernel methods; the kernel trick; RBF kernels; kernel ridge regression |
| H3 | `05C` | Clustering: k-means, hierarchical, DBSCAN; validating clusters; phase discovery and anomaly detection |

> **Midterm — Week 6, covering Classes 1–5** (per Appendix 2).

### Part III — Dimensionality Reduction (Class 6)

#### Class 6 — Dimensionality Reduction: PCA, t-SNE and UMAP `[wk 6]`
| | Notebook | Content |
|---|---|---|
| H1 | `06A` | Curse of dimensionality; the manifold hypothesis; **PCA**: covariance, eigenvectors, explained variance |
| H2 | `06B` | **t-SNE**: neighbour embeddings, perplexity; brief context on Isomap and LLE |
| H3 | `06C` | **UMAP**; comparing methods; reading embedding plots critically |

### Part IV — Deep Learning Foundations (Classes 7–9)

#### Class 7 — Neural Networks and Backpropagation `[wk 8 → 7]`
| | Notebook | Content |
|---|---|---|
| H1 | `07A` | Perceptron; limits of linear models; MLPs; activation functions; universal approximation |
| H2 | `07B` | Loss surfaces; gradient descent; **backpropagation**; the chain rule and computational graphs |
| H3 | `07C` | PyTorch: tensors, autograd, modules; a first network trained end to end |

#### Class 8 — Training Deep Networks `[wk 9 → 8]`
| | Notebook | Content |
|---|---|---|
| H1 | `08A` | Optimizers: SGD, momentum, Adam; learning rates and schedules |
| H2 | `08B` | Training dynamics: initialization, vanishing and exploding gradients, batch normalization |
| H3 | `08C` | Regularization for deep networks: dropout, weight decay, early stopping, data augmentation |

#### Class 9 — Representation Learning: Autoencoders and Contrastive Learning `[wk 7 → 9]`
| | Notebook | Content |
|---|---|---|
| H1 | `09A` | What a learned representation is; similarity measures; cosine distance; embedding spaces |
| H2 | `09B` | **Autoencoders**: encoder, latent space, decoder; undercomplete and denoising; autoencoders versus PCA |
| H3 | `09C` | **Contrastive learning**: positive and negative pairs; embeddings; self-supervision |

### Part V — Modern Architectures (Classes 10–12)

#### Class 10 — Deep Learning for Images: Convolutional Neural Networks `[wk 10]`
| | Notebook | Content |
|---|---|---|
| H1 | `10A` | Images as tensors; why fully connected layers fail on images; convolution |
| H2 | `10B` | Pooling; feature maps; receptive fields; what filters learn |
| H3 | `10C` | Modern CNN architectures; transfer learning for images; microscopy, medical imaging, astronomy, materials |

#### Class 11 — Sequence Models and Transformers `[wk 11]`
| | Notebook | Content |
|---|---|---|
| H1 | `11A` | Sequential scientific data; **RNNs**, hidden states, vanishing gradients; **LSTM** and gating |
| H2 | `11B` | **Attention** and self-attention; queries, keys, values; positional encoding |
| H3 | `11C` | The **transformer** architecture; multi-head attention; residual stream; scaling |

#### Class 12 — Foundation Models, Transfer Learning, GNNs and Synthesis `[wk 12]`
| | Notebook | Content |
|---|---|---|
| H1 | `12A` | Pretraining and fine-tuning; **transfer learning**; **foundation models**; multimodal learning |
| H2 | `12B` | Graph-structured data; **graph neural networks**; **message passing**; molecules, materials, biological systems |
| H3 | `12C` | Choosing a method for a data modality; course synthesis |

**Course synthesis (12C):** tabular → trees and boosting · high-dimensional → PCA and manifold
methods · images → CNNs · sequences → RNNs and transformers · graphs → GNNs.

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

## Technical targets

- Notebooks must run on **Google Colab** (per the OBTL's Technology-Enhanced Learning section)
- Guarded `pip install` cells for anything outside the Colab base image
  (`umap-learn`, `xgboost`, `rdkit`, `torch-geometric`)
- Datasets loaded from URL or generated in-notebook, so nothing depends on local files
- Every notebook must run top to bottom without error, and must validate against current
  `nbformat` so it opens in Colab
