---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
redirect_from:
  - /project
---

{% include base_path %}

### Enhancing Causal Inference in Observational Data Using Expectation-Maximization Algorithms

Jan. 2025 ‐ Apr. 2025

* Designed an **EM-based causal inference** framework that jointly estimates a latent confounder $U$ and ATE under parametric **SCM** assumptions, enabling unbiased estimation with hidden confounding.
* Implemented three **E-step** variants (**Newton–Raphson, Monte Carlo, and closed-form**) using **R** and benchmarked on IHDP; Newton–Raphson converged fastest and reached **ATE** about 4.0248 vs. true 4.0297 after 200 iterations.
* Built an augmented propensity model using $\hat U + X$ and an outcome model; achieved **AUC** $0.7434$, **RMSE** $2.45\times 10^{-9}$, and reduced ATE bias by $42.55\% (0.00854 \to 0.00491)$, evidencing effective recovery of latent confounding.

### Compositional Attention with Intermediate Step Supervision

Jan. 2025 ‐ Apr. 2025

* Proposed and implemented a **Compositional Attention mechanism** that combines function-embedding into **Transformer self-attention** for function-composition tasks, outperforming a standard self-attention baseline on held-out compositions.
* Constructed a simulated benchmark with 2K samples and 8-dim inputs, evaluated on a test set of unseen composition patterns, enabling rigorous generalization assessment.
* Introduced an auxiliary loss to study supervision levels in compositional reasoning, finding a train–test trade-off.
