# ✈️ Airline Satisfaction Prediction using Classification Algorithms

A machine learning project aimed at predicting passenger satisfaction on airlines by leveraging classification models, feature engineering, and airline‐survey data.

---

## 📌 Project Overview

This project delivers a full pipeline for churn-style classification: loading and preprocessing airline survey data, exploring passenger behavior and flight attributes, crafting meaningful features, training classification models, and evaluating their performance. The objective is to understand what drives passenger satisfaction and build a model to predict whether a passenger is satisfied or not.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Survey data capturing passenger ratings and flight attributes (e.g., airline, class, delay, service quality, and whether the passenger was satisfied).

### 2. Exploratory Data Analysis (EDA)

* Distribution of satisfaction vs. dissatisfaction
* Relationship between flight attributes (e.g., class, delay, seat comfort) and satisfaction
* Correlation heatmaps and feature distributions
* Identification of key patterns and anomalies

### 3. Feature Engineering

* Encoding categorical features (e.g., airline, class)
* Creating derived features such as delay bins, travel type categories
* Scaling numerical features where needed for model compatibility
* Splitting into training and test sets ensuring stratified sampling

### 4. Modeling

Classification algorithms applied:

* **Logistic Regression** (baseline model)
* **Random Forest Classifier** (strong performer)
* **(Optionally) Gradient Boosting / XGBoost** for enhancement

### 5. Evaluation

Metrics used to measure model performance:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC

**Result:** The Random Forest (or ensemble) classifier achieved the best performance in predicting passenger satisfaction, driven by engineered features like delay and service ratings.

### 6. Prediction & Insights

* Generated predictions on unseen data to classify passenger satisfaction
* Derived feature importance to interpret which flight aspects most impact satisfaction
* Provided recommendations for airline service improvements based on findings

---

## 📁 Project Structure

```
Airline-Satisfaction-Prediction/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Significant delay and limited seat comfort strongly correlate with dissatisfaction
* Service-related features (e.g., in-flight service rating) deliver high predictive power
* Categorical features like travel class and airline type influence satisfaction once encoded properly
* Feature engineering boosts classifier performance compared to using raw data only

---

## 🚀 Future Improvements

* Incorporate advanced models such as Deep Learning (e.g., neural networks)
* Use cross-validation pipelines and hyperparameter tuning (GridSearch / RandomSearch)
* Deploy model via a web app (Flask / Streamlit) for real-time satisfaction prediction
* Enhance dataset with external factors (e.g., weather, flight route, seasonality)
* Perform A/B testing or live prediction on actual passenger feedback data

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

