# Customer Segmentation Using Clustering

Discover actionable customer groups from recency, frequency, monetary and engagement behaviour.

## Overview

This portfolio project demonstrates a reproducible unsupervised-learning workflow with
transparent data assumptions, exploratory checks, appropriate diagnostics, interpretation
and responsible-use notes. The notebook is designed to run from top to bottom.

## Problem statement

- **Category:** Clustering
- **Goal:** Discover actionable customer groups from recency, frequency, monetary and engagement behaviour.
- **Data mode:** Verified demo mode
- **Primary evaluation:** Silhouette, Davies-Bouldin, Calinski-Harabasz and seed stability

## Dataset

- **Dataset:** Deterministic RFM-style demonstration data; schema supports Online Retail transactions.
- **Reference/source:** https://archive.ics.uci.edu/dataset/352/online+retail
- **Reproducibility:** The default notebook path is deterministic and uses a fixed seed.

Demonstration labels, where present, are hidden from fitting and used only after modelling
to audit whether the unsupervised output recovered meaningful structure.

## Project workflow

1. Validate schema, missingness, duplicates and feature ranges.
2. Explore the behaviour most relevant to the unsupervised objective.
3. Build a leakage-safe feature representation.
4. Compare or calibrate the unsupervised method.
5. Evaluate structure, stability, ranking quality or anomaly usefulness.
6. Profile and interpret outputs before proposing downstream use.

## Methodology

- Robust feature scaling
- K-Means selection
- PCA visualisation and segment profiling

## Evaluation

- Silhouette
- Davies-Bouldin
- Calinski-Harabasz and seed stability

Unsupervised metrics are read together rather than reduced to a single accuracy claim.
When hidden labels exist in demonstration data, they never influence model fitting.

## Verified results

The canonical notebook has been verified end to end in **verified demo mode**.
Results are generated at execution time and intentionally not hard-coded into this README.
Replace demonstration data only with licensed, privacy-safe data matching the documented schema.

## Repository structure

~~~text
├── customer_segmentation_clustering.ipynb
└── README.md
~~~

## How to run

From this project directory:

~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
jupyter lab "customer_segmentation_clustering.ipynb"
~~~

On Windows, activate the environment with <code>.venv\Scripts\activate</code>.

## Technologies

- Python 3.11+
- Pandas and NumPy
- Scikit-learn and SciPy
- Matplotlib and Seaborn
- Jupyter

## Learning outcomes

- Frame an unsupervised objective without inventing a target.
- Select diagnostics that match clustering, ranking, association or anomaly tasks.
- Separate model fitting from any hidden-label audit.
- Turn mathematical output into cautious, domain-readable findings.

## Future improvements

- Validate with a larger, newer and independently collected dataset.
- Add repeated-sample stability and drift monitoring.
- Review privacy, fairness and downstream decision risk.
- Package inference only after the evaluation contract is agreed.

## Author

**Tajamul Khan**

[GitHub](https://github.com/tajamulkhann) · [LinkedIn](https://www.linkedin.com/in/tajamulkhann/) · Instagram: <code>@tajamul.codes</code>

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.codes/" target="_blank">
<img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://topmate.io/tajamulkhan" target="_blank">
<img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0MCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white">
</a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f">
<img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>
<a href="https://t.me/tajamul_khan">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://substack.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719">
</a>
<a href="https://www.kaggle.com/tajamulkhan">
<img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
</a>
<a href="https://github.com/tajamulkhann">
<img src="https://img.shields.io/badge/Github-12100E?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://medium.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">
</a>
<a href="https://www.youtube.com">
<img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</a>
</div>
