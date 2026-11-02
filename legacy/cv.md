---
layout: single
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download my [Résumé](https://drive.google.com/file/d/1W4F2QAnfqPmzn4NHtSJGOR6PySqPds7q/view?usp=sharing).

Education
======
* [University of Toronto](https://www.utoronto.ca/), Toronto, Ontario, Canada, Sept. 2025 – Dec. 2026 (Expected)
  
  Master of Science in Applied Computing
  
  * Coursework: Computational Imaging, Machine Learning, Causal Inference, Computational Models of Semantic Change.
* [University of Waterloo](https://uwaterloo.ca/), Waterloo, Ontario, Canada, Sept. 2020 – Apr. 2025
  
  Bachelor of Mathematics in Computer Science & Statistics, Minor in Computational Mathematics
  
  * GPA: 90.36%, obtained Academic Excellent Standing and Term Distinction for all terms.
  * Coursework: Artificial Intelligence, Machine Learning, Algorithms and Data Structure, Computational Inference, Operating System, and User Interface.

EXPERIENCE
======

### Undergraduate Tutor

*[University of Waterloo](https://uwaterloo.ca/), Waterloo, Ontario, Canada*, Sept. 2024 - Apr. 2025

* Provide academic support to undergraduate students, enhancing their understanding of concepts in algebra, calculus, and computer science.
* Develop and deliver personalized tutoring sessions tailored to individual student needs, resulting in improved academic performance and confidence.

### Undergraduate Research Assistant

*[University of Waterloo](https://uwaterloo.ca/), Waterloo, Ontario, Canada*, Jan. 2024 - Apr. 2025

Supervisor: [Prof. Pascal Poupart](https://cs.uwaterloo.ca/~ppoupart/)

* Co-designed a **transformer-based** tabular architecture ("basis transformers") to handle heterogeneous columns, text features, and missing or noisy values; lifted median $R^2$ by +0.338 with the lowest variance across 34 OpenML-CTR23 tasks while using 5x fewer parameters than the best baseline.
* Performed end-to-end **EDA** on **T4** (1.34TB) and **OpenML benchmarks** (**PCA, leakage checks, type inference**); encoded invariances (hierarchical structure, numeric representation) that stabilized results across datasets.
* Implemented robust preprocessing and augmentation for mixed-type tables (numeric tokenization, text column embeddings, few-shot reference sampling); improved generalization to unseen schemas without metadata beyond column names.
* Built and maintained a rigorous experimentation pipeline using **Python** with **PyTorch**, **Transformers**, and **TensorFlow** for baselines; reported reproducible $R^2$ and F1 metrics with best-checkpoint selection.
* Scaled training and evaluation on A100 GPUs with **HuggingFace Accelerate** and **Slurm**; reduced run-to-run variance and enabled zero-shot and few-shot experiments across seeds and datasets for reliable comparisons.

### Undergraduate Research Scientist

*[Vector Institute](https://vectorinstitute.ai/), Toronto, Ontario, Canada*, May. 2024 - Aug. 2024

Supervisor: [Prof. Pascal Poupart](https://cs.uwaterloo.ca/~ppoupart/)

* Developed a Contextual RBF-Histogram algorithm using **Python** for **contextual bandits** (RBF-kernel–weighted reward bins) to select the best arm per context, achieving 55.6% correct arm selection on a test set of 2K data points.
* Formulated and implemented a **contextual multi-armed bandit (CMAB)** procedure for sequential decision-making, using an RBF reward for greedy arm selection and **XGBoost** for label generation, with online data aggregation to improve the policy.
* Evaluated on datasets over 10K rows, producing diagnostic plots to measure uncertainty and explainability.

### Full Stack Developer (Co-op)

*[Aterlo Networks](https://aterlo.com/), Waterloo, Ontario, Canada*, May. 2023 - Dec. 2023

* Engineered OOP **Python** data models and a cloud ingestion pipeline for multi-agent network telemetry, supporting 10M+ fixed-wireless/fiber devices across 20+ customer sites and reducing network load by 15%.
* Automated unit-test generation with **Python unittest and mock** (diff detection and docs) for thousands of models, accelerating regression coverage and team adoption; tool was integrated into workflows.
* Designed and shipped a responsive device information card UI (**JS/TS/Node, CSS**) surfacing port stats and connected-device counts across all supported routers/APs, validated via simulation on phone/tablet/desktop.
* Implemented semaphore-based session locking for **SSH** device tooling to prevent concurrent writes, stabilizing **APIs** under load and cutting failure modes from overlapping sessions.
* Built a **Protobuf** to **UML** generator and wired it into **Bitbucket CI**, visualizing internal **API message** relationships to speed schema reviews and clarify service contracts across **Python/JS** codebases.
* Reverse-engineered legacy devices (no manuals) using **cURL** and vendor CLIs; instrumented **Google Cloud queries** and dashboards to isolate model-specific logic defects and shorten debug cycles.

### Data Engineer (Co-op)

*[Tesla](https://www.tesla.com/), Shanghai, China*, Mar. 2022 - Aug. 2022

* Built an end-to-end **Django** and **MySQL** portal for recruiting data (1K+ rows, 40+ fields, 20 users); added **SSO**, **RBAC**, and row-level access to eliminate overwrites and lift team throughput 50%.
* Implemented **CRUD**, advanced **SQL** filters, and **Bokeh** interactive tables/charts; automated sub-team weekly summaries with email digests, saving hours of manual reporting each week across 5 groups.
* Containerized with **Docker** and deployed on **Kubernetes**; delivered reproducible dev/prod environments and reliable releases while coordinating access/compliance with 3+ departments.
* Built **PySpark** and **Airflow ELT** joining vision and telematics for seat-belt detection analysis; disentangled true unbuckled behavior from detector failures, flagging 20% of 10M+ events as potential model misses.
* Published curated **MySQL** gold tables and SQL-ready reports powering safety analytics and offline model evaluation; accelerated root-cause triage and focused model iteration on highest-impact scenarios.
* Bootstrapped **Excel/VBA macros** (data validation, dropdowns, summary generation) to stabilize the legacy sheet pre-migration, reducing data-entry errors and transition risk.

### Machine Learning Engineer (Co-op)

*[iFlytek](https://www.iflytek.com/en/), Beijing, China*, Sept. 2021 - Dec. 2021

* Engineered an ensemble of seven Chinese paraphrase-generation algorithms (**Python, jieba, LTP**), delivering 95.8% precision and 99.2% recall while preserving fluency and maximizing semantic diversity.
* Built a **BERT back-translation** pipeline to augment training data and diversify candidates, strengthening model generalization across domains.
* Preprocessed 1M+ sentences with generative models via a scalable, reproducible data pipeline, enabling large-scale training and evaluation.
* Applied semantic role labeling, POS/NER, and dependency parsing (**LTP**) to enforce linguistic constraints during generation, improving readability and grammaticality of outputs.
* Established an evaluation framework tracking precision and recall, creating objective quality gates for release decisions.
* Synthesized and presented state-of-the-art research on paraphrase generation and semantic similarity, informing algorithm selection and prioritizing high-impact experiments.

AWARD, SCHOLARSHIP, and GRANT
======
* [2024] ($7,500) Vector Institute Research Grant
* [2024] ($1,500) University of Waterloo President’s Research Award
* [2022] ($3,000) University of Waterloo CS International Student Upper‐Year Scholarship
* [2021] ($2,000) University of Waterloo President’s Scholarship of Distinction
