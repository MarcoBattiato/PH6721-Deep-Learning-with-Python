# PH6725 — Artificial Intelligence for Science

**Course outline v2** — derived from the approved OBTL (Annex A, approved 05-06-2026).

12 classes × 3 hours of content (3.25 h scheduled slot × 12 = 39 contact hours).
Delivery: 3 Jupyter notebooks per class, one per hour (`NNA`, `NNB`, `NNC`).

---

## Design basis

This outline is generated from the **approved OBTL's Course Content section**, which elaborates
the five ILOs and is the binding specification. The week-by-week Planned Schedule in the OBTL is
followed essentially one-to-one, with two deliberate departures documented below.

### Binding content checklist

| ILO | Mandated content | Delivered in |
|---|---|---|
| 1 | Linear regression | 2A |
| 1 | Logistic regression | 2B |
| 1 | Support vector machines | 4B |
| 1 | Decision trees | 5A |
| 1 | Random forests | 5B |
| 1 | Gradient boosting | 5C |
| 1 | ROC, AUC, precision, recall, F1 | 3C |
| 2 | Multilayer perceptron (MLP) | 7A |
| 2 | Convolutional neural networks | 8B, 8C |
| 2 | Recurrent neural networks | 10B |
| 2 | Long short-term memory (LSTM) | 10C |
| 2 | Transformers, BERT | 11A–11C |
| 3 | Principal component analysis | 6A |
| 3 | Isomap | 6B |
| 3 | Locally linear embedding (LLE) | 6B |
| 3 | Laplacian eigenmaps | 6B |
| 3 | t-SNE | 6C |
| 3 | UMAP | 6C |
| 4 | Featurization, feature construction | 9A, 12B |
| 4 | Tokenization | 9A |
| 4 | Embeddings | 9B, 12B, 12C |
| 4 | Visualization | 1C, 6C, 9C |
| 4 | Drug discovery | 12B |
| 4 | Materials design | 12C |
| 5 | Python scientific computing | 1B, throughout |
| 5 | LLM-assisted coding ("vibe coding") | 2C, recurring |
| 5 | Building and deploying ML models | throughout |

### Departures from the OBTL Planned Schedule

**1. Exploratory Data Analysis moves from week 5 to Class 1, Hour 3.**
The OBTL places EDA after three weeks of supervised learning, which requires students to fit
models to data they have not been taught to load or inspect. Moving it into Class 1 restores the
natural order and frees one slot.

**2. That freed slot becomes Class 3, "Generalization, Model Selection and Metrics."**
The approved OBTL contains no train/validation/test split, no overfitting or bias–variance
discussion, no cross-validation and no regularization anywhere in its schedule or content, while
still requiring ROC/AUC/precision/recall/F1 under ILO 1. Metrics without a held-out set is not a
teachable position. This class supplies the missing foundation and absorbs the "model accuracy"
theme from the OBTL's week 3.

Every topic named in the OBTL Course Content is still covered. No mandated item is dropped.

### Additions beyond the approved content

- **Data leakage and cross-validation methodology** (3A) — the most common failure mode in
  published scientific machine learning.
- **Training deep networks in practice** (8A) — optimizers, learning rates, initialization,
  dropout, batch normalization. The OBTL teaches backpropagation and then five weeks of
  architectures with no coverage of how training is actually made to work.
- **Message passing on molecular graphs** (12B) — one hour, admitted under the OBTL's own week-12
  title "Domain-Specific Embeddings and learning". Drug discovery cannot be taught honestly
  without it.

---

## Class-by-class

### Part I — Foundations (Classes 1–3)

#### Class 1 — Introduction to AI for Science and Scientific Python `[OBTL wk 1 + 5]`
| | Notebook | Content |
|---|---|---|
| H1 | `01A` | What AI, ML and DL are; ML as a toolbox; inductive bias; supervised/unsupervised/representation learning; scientific applications; the ML workflow |
| H2 | `01B` | Jupyter; NumPy arrays, indexing, slicing, shapes; vectorization; broadcasting |
| H3 | `01C` | pandas; loading data; dataset anatomy; missing values; summaries; distributions, relationships, groups; correlation |

**Status: built.** `01C` sections 8–13 still need expanding to match sections 1–7.

#### Class 2 — Regression, Classification and Scientific Programming `[OBTL wk 2]`
| | Notebook | Content |
|---|---|---|
| H1 | `02A` | The supervised learning framework; linear regression; least squares; fitting as optimization; least squares as Gaussian maximum likelihood |
| H2 | `02B` | Binary classification; logistic regression; decision boundaries; the sigmoid and cross-entropy loss |
| H3 | `02C` | LLM-assisted scientific programming: prompting for scientific code, verifying output, debugging, and failure modes (hallucinated APIs, silently wrong numerics, plausible-but-wrong statistics) |

#### Class 3 — Generalization, Model Selection and Metrics `[new — absorbs "model accuracy"]`
| | Notebook | Content |
|---|---|---|
| H1 | `03A` | Train/validation/test; cross-validation; **data leakage**; reproducibility and random seeds |
| H2 | `03B` | Polynomial regression → overfitting → bias–variance tradeoff → L1/L2 regularization, as one continuous narrative |
| H3 | `03C` | MSE, MAE, R²; confusion matrix; **precision, recall, F1**; **ROC and AUC**; class imbalance |

### Part II — Classical Machine Learning (Classes 4–5)

#### Class 4 — Distance and Margin `[OBTL wk 3]`
| | Notebook | Content |
|---|---|---|
| H1 | `04A` | K-nearest neighbours; distance metrics; scaling; first look at the curse of dimensionality |
| H2 | `04B` | **Support vector machines**: margins, support vectors, soft margins; kernels and the RBF kernel |
| H3 | `04C` | Clustering: k-means, hierarchical, DBSCAN; validating clusters; phase discovery and anomaly detection |

#### Class 5 — Trees, Forests and Boosting `[OBTL wk 4]`
| | Notebook | Content |
|---|---|---|
| H1 | `05A` | **Decision trees**: recursive partitioning, entropy, information gain, pruning |
| H2 | `05B` | **Random forests**: bagging, ensembles, feature importance and its pitfalls |
| H3 | `05C` | **Gradient boosting**; XGBoost; when boosting beats deep learning on tabular scientific data |

> **Midterm — week 6, covering Classes 1–5.** Matches the OBTL's stated scope.

### Part III — Representation and Manifold Learning (Class 6)

#### Class 6 — Manifold Learning `[OBTL wk 6]`
| | Notebook | Content |
|---|---|---|
| H1 | `06A` | Curse of dimensionality; the manifold hypothesis; **PCA**: covariance, eigenvectors, explained variance |
| H2 | `06B` | **Isomap**, **locally linear embedding**, **Laplacian eigenmaps** — presented through their shared graph-Laplacian structure |
| H3 | `06C` | **t-SNE** and **UMAP**; reading embedding plots critically; what these visualizations do and do not mean |

### Part IV — Deep Learning (Classes 7–8)

#### Class 7 — Neural Networks and Backpropagation `[OBTL wk 7]`
| | Notebook | Content |
|---|---|---|
| H1 | `07A` | Perceptron; limits of linear models; **MLP**; activation functions; universal approximation |
| H2 | `07B` | Loss surfaces; **gradient descent**; **backpropagation**; the chain rule and computational graphs |
| H3 | `07C` | PyTorch on-ramp: tensors, autograd, modules; a first MLP trained end to end |

#### Class 8 — Computer Vision `[OBTL wk 8]`
| | Notebook | Content |
|---|---|---|
| H1 | `08A` | Training deep networks in practice: SGD, momentum, Adam; learning rates; initialization; dropout; batch normalization; early stopping |
| H2 | `08B` | Images as tensors; **convolution**; pooling; feature maps; receptive fields |
| H3 | `08C` | Modern CNN architectures; data augmentation; transfer learning for images; microscopy, astronomy, medical imaging |

### Part V — Language, Sequences and Attention (Classes 9–11)

#### Class 9 — Text, Tokenization and Embeddings `[OBTL wk 9]`
| | Notebook | Content |
|---|---|---|
| H1 | `09A` | Text as data; **tokenization**; vocabularies; subword tokenization |
| H2 | `09B` | **Embeddings**: word vectors, similarity, cosine distance; autoencoders and latent spaces |
| H3 | `09C` | **Visualizing embeddings**; embedding arithmetic; what embedding geometry encodes |

#### Class 10 — Sequence Modelling `[OBTL wk 10]`
| | Notebook | Content |
|---|---|---|
| H1 | `10A` | Sequential scientific data; time series; trajectories; windowing and forecasting setup |
| H2 | `10B` | **Recurrent neural networks**; hidden states; backprop through time; vanishing gradients |
| H3 | `10C` | **LSTM** and gating; GRU; where recurrence still wins, and where it fails |

#### Class 11 — Transformers `[OBTL wk 11]`
| | Notebook | Content |
|---|---|---|
| H1 | `11A` | **Attention**; queries, keys, values; self-attention as learned routing |
| H2 | `11B` | **Transformer** architecture; multi-head attention; positional encoding; residual stream |
| H3 | `11C` | **BERT** and masked language modelling; pretraining and fine-tuning; **LLMs** and scaling |

### Part VI — Scientific Applications (Class 12)

#### Class 12 — Domain-Specific Embeddings and Learning `[OBTL wk 12]`
| | Notebook | Content |
|---|---|---|
| H1 | `12A` | Transfer learning and foundation models; pretraining for science; protein and multimodal models |
| H2 | `12B` | **Drug discovery**: SMILES, molecular fingerprints, molecules as graphs, message passing |
| H3 | `12C` | **Materials design**: structure representations, property prediction; course synthesis |

**Course synthesis (12C):** tabular → trees and boosting · high-dimensional → PCA and manifold
learning · images → CNNs · sequences → RNNs and transformers · molecules and materials → graphs
and domain embeddings.

> **Final exam — week 13, covering all material.**

---

## Assessment (per approved OBTL)

| Component | Weight | Timing | Notes |
|---|---|---|---|
| Class participation (Wooclap) | 10% | Weekly | 5–10 questions per lecture |
| Midterm | 10% | Week 6 | Classes 1–5; restricted open, one A4 double-sided sheet |
| Final project | 40% | — | Presentation 70% + interactive notebook 30%; topic due week 4 |
| Final exam | 40% | Week 13 | All material; restricted open, one A4 double-sided sheet |

**Outstanding:** the rubrics file `PH6725 - Appendix 1 to 4.pdf`, referenced by the approved OBTL,
is not present in this folder and will be needed.

---

## Recurring notebook conventions

Established by the Class 1 notebooks and to be carried through:

- Header block with course code, class/notebook/hour, instructor and contact details
- **Learning objectives** cell opening each notebook
- Numbered sections with `#` / `##` headings
- Inline mini-exercises in `<div class="alert alert-success">` boxes
- `STUDENT WORKSPACE` code cells following each exercise
- Matplotlib-drawn conceptual figures rather than external images
- **Key takeaways** and **Optional preparation for the next notebook** closing cells
- Recurring LLM-assisted coding prompts (from Class 2 onward)

## Technical targets

- Notebooks must run on **Google Colab** (per the OBTL's Technology-Enhanced Learning section)
- Guarded `pip install` cells for anything outside the Colab base image
  (`umap-learn`, `xgboost`, `rdkit`, `torch-geometric`)
- The local anaconda environment is Python 3.8.5 with 2020-era packages and lacks `umap`,
  `xgboost`, `plotly` and `torch_geometric`; Colab is the reference environment
- Datasets loaded from URL or generated in-notebook, so nothing depends on local files
