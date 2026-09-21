# Material outside the lectures

These notebooks are not delivered in class, and they carry their own numbering — deliberately
unlike the `NNx` of the taught hours — so that it is never unclear which week they belong to.

| Prefix | What it means | Assumed by later notebooks? |
|---|---|---|
| `S1`, `S2`, … | **Supplement** — expected reading, attached to a class but not lectured | yes |
| `X1`, `X2`, … | **Extra** — genuinely optional, a broader background for those who want it | never |

Nothing here is examinable, and no `X` notebook is ever a prerequisite for a taught hour.

## What is here, and when to read it

| | Read it after | Content |
|---|---|---|
| [`X1` — Choosing Features When Most of Them Are Useless](X1-FeatureSelection.ipynb) | **Class 5** | The winner's curse; why selection belongs inside the resampling loop; nested cross-validation; filter, wrapper and embedded selection compared on data whose truth is known; stability selection; what correlated features do to all of it. |
| [`X2` — Validation When Time and Trials Are Against You](X2-ValidationInTime.ipynb) | **Class 5**, after `X1` | Why a random split invents performance on ordered data; when k-fold *is* valid on a time series; purging and embargo; walk-forward validation; counting the trials behind a result; non-stationarity and monitoring. |

Both are written in the language of finance, because that is where low signal-to-noise, hundreds of
candidate features and a fixed arrow of time all appear at once. The methods are the course's own,
applied where its assumptions fail. Neither is investment advice.
