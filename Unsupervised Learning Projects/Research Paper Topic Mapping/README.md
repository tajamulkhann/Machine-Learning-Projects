# Research Paper Topic Mapping

Map paper abstracts into interpretable research themes and surface nearby work through vector similarity.

## Project status

- **Portfolio decision:** New
- **Learning type:** Unsupervised learning
- **Core method:** TF-IDF, K-Means, cosine similarity, and SVD
- **Execution:** Notebook executed successfully with outputs committed

## Problem statement

The project demonstrates how patterns, similarities, communities, or anomalies can be discovered without using a prediction target during model fitting. Results are interpreted as exploratory signals rather than ground truth.

## Dataset

A deterministic domain-shaped text corpus is generated inside the notebook. Hidden generator topics are used only for post-hoc diagnostics.

The notebook documents its data contract, reproducible seed, quality checks, and any synthetic proxy labels used only for retrospective diagnostics.

## Workflow

```text
Data validation
      ↓
Feature representation and scaling
      ↓
Unsupervised model comparison
      ↓
Internal metrics and stability checks
      ↓
Interpretation, visualization, and limitations
```

## Evaluation

The notebook uses method-appropriate evidence such as silhouette score, Davies-Bouldin index, cluster stability, retrieval similarity, graph structure, anomaly-score diagnostics, and post-hoc synthetic checks. No demo result is presented as a production benchmark.

## Repository structure

```text
├── research_paper_topic_mapping.ipynb
└── README.md
```

## How to run

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r "Unsupervised Learning Projects/requirements.txt"
jupyter lab "Unsupervised Learning Projects/Research Paper Topic Mapping/research_paper_topic_mapping.ipynb"
```

Run the notebook from top to bottom. Saved outputs are included for review.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Jupyter

## Responsible use

Discovered groups and anomaly flags do not establish identity, intent, causality, risk, or business impact. Production use requires domain review, representative data, privacy controls, monitoring, and decision-specific evaluation.

## Author

**Tajamul Khan** — Data Scientist and AI Engineer

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
