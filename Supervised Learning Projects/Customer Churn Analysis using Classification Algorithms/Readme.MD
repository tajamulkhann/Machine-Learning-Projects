# 🔁 Customer Churn Analysis Using Classification Algorithms

A machine-learning project focused on predicting customer churn (i.e., which customers are likely to stop using a service) using classification models, feature engineering, and business-centric insights.

---

## 📌 Project Overview

This project develops a full pipeline: data ingestion of customer records, exploratory analysis, feature engineering (demographics, usage, contract, payment history), building classification models (Logistic Regression, Decision Tree, Random Forest etc.), evaluating and interpreting results, and delivering actionable insights for retention strategies.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Collected customer data with features such as: tenure, contract type, monthly charges, total charges, service usage, payment method, and a target column indicating churn (yes/no).

### 2. Exploratory Data Analysis (EDA)

* Plotted distributions of churn vs non-churn by tenure, monthly charges, contract type.
* Visualised correlations between features and churn through heatmap and boxplots.
* Checked class imbalance (often fewer churners than non-churners).

### 3. Feature Engineering

* Encoded categorical variables (e.g., contract type, payment method, gender) using label/one-hot encoding.
* Created derived features: e.g., average monthly charge, ratio of total charges to tenure, tenure buckets.
* Scaled numeric features where required for models.
* Split into training and test sets (e.g., 80/20) with stratification if class imbalance present.

### 4. Modeling

Implemented classification models:

* **Logistic Regression** as baseline
* **Decision Tree** for non-linear patterns
* **Random Forest Classifier** to improve performance and reduce overfitting
* Possibly tuned hyper-parameters (max_depth, n_estimators) via cross-validation

### 5. Evaluation

Performance metrics used include:

* Accuracy
* Precision / Recall / F1-score
* ROC-AUC
* Confusion matrix
  **Result:** The best model achieved higher recall (to catch churners) and good balance between precision and recall—helping prioritise retention resources.

### 6. Insights & Business Application

* Identified key churn-drivers: shorter tenure, high monthly charges, month-to-month contract type, digital payment method without automatic renewal.
* Provided recommendations: target early-tenure customers with month-to-month contracts, offer lower monthly charges or incentives, convert to annual contracts.
* Developed a retention strategy: monitor high-risk segments, deploy customised offers.

---

## 📁 Project Structure

```
Customer-Churn-Analysis-Classification/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Contract type and tenure emerged as the strongest predictors of churn.
* Derived features (e.g., charges per tenure year) improved model discrimination compared to raw features alone.
* Random Forest outperformed logistic regression due to capturing interaction effects and non-linearities.
* Class imbalance handling (via stratification or weighting) was crucial in achieving reasonable recall on churn class.

---

## 🚀 Future Improvements

* Incorporate sequential/temporal user-behaviour data (e.g., monthly usage, call logs) using time-series or RNN models.
* Explore ensemble/boosting algorithms (like XGBoost, LightGBM) for potentially higher accuracy and robustness.
* Deploy predictive model as a dashboard for business users, with real-time churn-risk scoring.
* Add explainability (e.g., SHAP values) so decision-makers understand which features drive churn predictions.
* Monitor and update model over time to handle concept-drift (customer behaviours changing over time).

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

---

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.datascientist/" target="_blank">
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
