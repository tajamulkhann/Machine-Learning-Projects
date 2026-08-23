# 🔍 Fraudulent Transaction Detection

A machine learning project focused on detecting fraudulent transactions using unsupervised/anomaly‐detection techniques and transaction data.

---

## 📌 Project Overview

This project implements a full pipeline: ingesting transaction data, performing exploratory analysis to understand normal vs anomalous behavior, engineering features that capture irregularities, applying unsupervised anomaly detection models, and evaluating detection efficacy. The objective is to identify likely fraud cases without relying extensively on labelled fraud data, thereby supporting real-time fraud monitoring and investigations.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab
* **Techniques:** Unsupervised models such as Isolation Forest, Local Outlier Factor, Autoencoders (anomaly detection) ([MDPI][1])

---

## 🔄 Workflow Summary

### 1. Data Collection

Transaction dataset containing features such as transaction amount, time, merchant category, account history, geographical location, and other behavioural signals.
Possible challenge: severe class imbalance (fraud cases being rare) typical in fraud detection domains. ([Wikipedia][2])

### 2. Exploratory Data Analysis (EDA)

* Distribution of transaction values, frequencies, merchant categories.
* Visualisations of anomaly indicators (e.g., unusually large amounts, unusual time/location patterns).
* Checking feature correlations, missing values, outliers, and data imbalances.

### 3. Feature Engineering

* Derived features such as: amount relative to average for user, transaction frequency per account, deviation from normal spending behaviour, time‐of‐day/day‐of‐week features.
* Encoding categorical variables (merchant type, region).
* Scaling numerical features.
* Possibly reducing dimensionality or combining features for anomaly detection.

### 4. Modeling (Unsupervised / Anomaly Detection)

* Fit unsupervised anomaly detection models, e.g., Isolation Forest, Local Outlier Factor, Autoencoders, One-Class SVM. These treat fraud as “rare anomalies” rather than defined classes. ([Medium][3])
* Choose thresholds for anomaly score (e.g., top 1% highest anomaly scores flagged for investigation).
* Possibly ensemble multiple models (OR‐ensemble) to improve recall of anomalies.

### 5. Evaluation & Insights

* Evaluate by measuring recall (detection of known fraud cases), precision (false alarms), possibly ROC/AUC if labels available.
* Analyse flagged anomaly cases: what features triggered the anomaly, pattern of flagged accounts.
* Provide insights such as: transaction patterns that frequently trigger flags, types of merchants or regions with more anomalies.

---

## 📁 Project Structure

```
Fraudulent-Transaction-Detection/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Behavioural signals such as high deviation from account baseline spending and transactions outside typical time / location windows were strong anomaly indicators.
* Unsupervised models identified many flagged transactions for further investigation; thresholds tuned to balance true-fraud capture vs alert volume.
* Feature engineering (especially user- or account-level rolling features) significantly improved anomaly detection performance over raw transaction features.
* The pipeline supports fraud-investigation teams by providing prioritized alerts rather than classifying every transaction.

---

## 🚀 Future Improvements

* Incorporate supervised or semi-supervised learning when fraud labels become available, for hybrid modelling.
* Integrate streaming data architecture (real-time feature engineering and model scoring) for live fraud detection.
* Add explainability (e.g., SHAP values) for anomaly flags so investigators understand why a transaction was flagged.
* Periodically retrain and recalibrate model to detect evolving fraud patterns and avoid model drift.
* Expand feature set to include device-fingerprint, geolocation drift, merchant network anomalies for richer detection.

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
