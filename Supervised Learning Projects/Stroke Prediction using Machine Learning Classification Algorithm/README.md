# 🧬 Stroke Prediction using Machine Learning Classification Algorithm

A machine-learning project focused on predicting the likelihood of a stroke using classification models and patient demographic, lifestyle, and medical data.

---

## 📌 Project Overview

This project builds an end-to-end pipeline: loading patient data (age, gender, hypertension, heart disease, smoking status, BMI, etc.), performing exploratory analysis, engineering features, training classification models (e.g., Logistic Regression, Random Forest, XGBoost), evaluating their performance, and deriving actionable insights for health interventions. The goal is to classify patients into high vs low risk of stroke and support early preventive care.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes features such as: age, gender, hypertension, heart disease, ever married, work type, residence type, average glucose level, BMI, smoking status, and target variable “stroke” (0/1 or yes/no).

### 2. Exploratory Data Analysis (EDA)

* Distribution of stroke vs non-stroke patients by age, BMI, glucose level
* Boxplots and histograms for key features grouped by target
* Correlation matrix among numeric features and relation to stroke
* Check missing values, class imbalance (strokes are rarer)

### 3. Feature Engineering

* Encode categorical features (gender, work type, smoking status) via one-hot encoding or label encoding
* Create derived features such as BMI category, glucose level buckets, combined risk score (e.g., hypertension + heart disease)
* Scale numeric features if required
* Handle class imbalance via oversampling, undersampling, or class weights
* Split data into training and test sets (e.g., 80/20) with stratification

### 4. Modeling

Classification algorithms used:

* **Logistic Regression** (baseline)
* **Random Forest Classifier** (strong performer)
* **XGBoost / LightGBM** for advanced performance
  Hyper-parameter tuning via GridSearchCV/RandomizedSearchCV (e.g., n_estimators, max_depth, learning_rate)

### 5. Evaluation

Metrics used:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC
  **Result:** The best model achieved high recall and acceptable precision, enabling identification of patients at risk of stroke for early intervention.

### 6. Insights & Application

* Key risk-factors: age, average glucose level, BMI, hypertension, heart disease emerged as strong predictors
* Practical recommendations: healthcare providers may prioritise screening for patients with elevated glucose, higher BMI, and combined hypertension + heart-disease history
* Model supports early risk stratification and targeted patient monitoring

---

## 📁 Project Structure

```
Stroke-Prediction-ML-Classification/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   └── stroke_prediction_analysis.ipynb
│── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── evaluate.py
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Patients with hypertension and heart disease together had markedly higher predicted risk of stroke.
* Deriving combined risk features (e.g., hypertension + heart-disease flag) improved model discrimination.
* Tree-based classifiers like Random Forest and XGBoost outperformed Logistic Regression due to capturing complex interactions.
* Managing class imbalance (e.g., via SMOTE or class weighting) was critical to achieve strong recall for the minority ‘stroke’ class.

---

## 🚀 Future Improvements

* Incorporate longitudinal data (e.g., yearly health records, lifestyle change logs) to improve prediction of future strokes.
* Deploy as a clinical web/app interface where patient data can be input and risk score returned in real time.
* Include interpretability/explainability (e.g., SHAP values) so clinicians understand which factors drove the prediction.
* Monitor model performance over time in production, adjust for population shift or new risk-factors.
* Link to intervention module: when high risk flagged, automatic referral to specialist, lifestyle recommendation or alert system.

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
