# 💊 Drug Classification Using Classification Algorithms

A machine learning project focused on classifying drug categories based on patient clinical profiles and features, leveraging classification models to support decision-making.

---

## 📌 Project Overview

This project builds a full pipeline: ingest patient data including vitals, demographics and other clinical indicators; conduct exploratory analysis to understand patterns; create informative features; train classification models to predict drug category; and evaluate model performance. The goal is to accurately classify the appropriate drug type and extract insights driving classification decisions.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset capturing patient features such as age, sex, blood pressure levels, cholesterol levels, and other clinical measures plus the target drug category for each patient.

### 2. Exploratory Data Analysis (EDA)

* Distribution of drug categories across samples
* Feature distributions and comparisons between classes
* Correlation heatmap among clinical variables
* Identification of missing values, class imbalance and outliers

### 3. Feature Engineering

* Encoding categorical variables (e.g., sex, drug category)
* Creating derived features such as BP ratio, cholesterol threshold bins
* Scaling numerical features (standardization/normalization)
* Splitting into training and test sets with stratified sampling

### 4. Modeling

Classification algorithms implemented:

* **Logistic Regression** (baseline)
* **Random Forest Classifier** (strong performer)
* **(Optional) Gradient Boosting / XGBoost** for improved accuracy

### 5. Evaluation

Key metrics used to assess model performance:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC

**Result:** The best‐performing classifier achieved high accuracy in drug category prediction, demonstrating the effectiveness of patient clinical features for classification.

### 6. Prediction & Insights

* Generated predictions for unseen patient profiles
* Analysed feature importance to identify key clinical indicators influencing drug classification (e.g., BP levels, cholesterol)
* Provided business/clinical insights: how features influence drug recommendation and classification

---

## 📁 Project Structure

```
Drug-Classification/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Certain clinical indicators (e.g., elevated blood pressure, cholesterol level) emerged as strong predictors of particular drug categories
* Feature engineering (derived features & scaling) significantly improved classification performance
* The classification pipeline provided reliable predictions, enabling decision-making support for drug classification tasks

---

## 🚀 Future Improvements

* Expand dataset with more diverse patient populations and drug categories
* Incorporate advanced models such as ensemble stacking or deep learning based classifiers
* Deploy a web app (Flask/Streamlit) for clinicians to input patient profile and receive drug category prediction
* Integrate explainability tools (e.g., SHAP or LIME) to interpret model predictions and support clinical reasoning

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

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
