# Drug Type Classification

Predict the prescribed drug category from age, sex, blood pressure, cholesterol and sodium-to-potassium ratio.

## Overview

This project is a focused, reproducible classification case study. The notebook covers data checks, meaningful exploratory analysis, leakage-safe preprocessing, a dummy baseline, cross-validated model comparison, untouched holdout evaluation and model interpretation.

## Problem statement

- **Task:** Classification
- **Target:** `Drug`
- **Primary metric:** Macro F1
- **Goal:** Predict the prescribed drug category from age, sex, blood pressure, cholesterol and sodium-to-potassium ratio.

## Dataset

- **Availability:** Download required: place `drug200.csv` in this directory
- **Recorded source:** The original project stored a shortened dataset link; download drug200.csv and place it beside the notebook.
- **Target:** `Drug`

Dataset licensing and usage conditions remain with the original publisher. Large or externally hosted data is intentionally not duplicated here.

## Project workflow

```text
Data validation
      ↓
Focused EDA
      ↓
Train / holdout split
      ↓
Pipeline-based preprocessing
      ↓
Baseline and cross-validation
      ↓
Holdout evaluation
      ↓
Error analysis and interpretation
```

## Modelling decisions

- Multiclass macro F1 gives each drug class equal importance.
- Categorical values are one-hot encoded inside validation folds.

### Models compared

- Logistic Regression
- Random Forest
- AdaBoost

## Evaluation

The notebook evaluates macro F1 and accuracy, with class-level precision/recall and a confusion matrix.

## Verified results

The dataset is not committed, so the refurbished notebook was statically validated but not executed. Results are intentionally omitted until the recorded dataset is downloaded and the notebook runs end to end.

## Repository structure

```text
├── drug_classification.ipynb
└── README.md
```

## How to run

From this project directory:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
jupyter lab 'drug_classification.ipynb'
```

If the dataset is not included, download it from the recorded source and use the exact filename shown above. Run notebook cells from top to bottom.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Jupyter

## Future improvements

- Validate on a newer or independently collected dataset.
- Add domain-specific error costs and decision thresholds.
- Track data drift and subgroup performance before deployment.
- Package the fitted pipeline only after data and licensing checks.

## Author

**Tajamul Khan**

[GitHub](https://github.com/tajamulkhann) · [LinkedIn](https://www.linkedin.com/in/tajamulkhann/) · Instagram: `@tajamul.codes`

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
