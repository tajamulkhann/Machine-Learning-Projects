# 📊 Customer Churn Analysis Using Regression Algorithm

A machine learning project focused on analyzing customer churn and predicting churn probability using regression techniques and business-centric data.

---

## 📌 Project Overview

This project implements a full workflow: ingesting customer account, usage, and demographic data; conducting exploratory analysis to identify churn patterns; engineering features and applying regression models to estimate churn probability; and interpreting outcomes for business action. The objective is to quantify churn risk and provide actionable insights for retention strategies.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset containing features like customer demographics, subscription details, usage metrics, tenure, payment behavior, and a target indicating churn (or churn probability/regression target).

### 2. Exploratory Data Analysis (EDA)

* Distribution of churn vs non-churn customers
* Visualizations of usage, tenure, payment behavior across churn status
* Correlation matrix and identifying key predictors
* Handling class imbalance or target skewness

### 3. Feature Engineering

* Encoding categorical variables (e.g., plan type, region)
* Creating derived features like tenure buckets, usage growth rate, payment lateness ratio
* Scaling/normalizing features if required by regression algorithm
* Splitting into training and validation sets

### 4. Modeling

Regression algorithms applied:

* **Linear Regression** (baseline)
* **Random Forest Regressor** or **Gradient Boosting Regressor** (better performance)
* Converting churn classification problem into probability/regression output

### 5. Evaluation

Metrics used include:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² score
* Interpretation of predicted probabilities and thresholds for decision-making

**Result:** The selected regression model provided accurate churn risk estimation and delivered business-actionable output by ranking customers by risk.

### 6. Prediction & Insights

* Generated churn-risk scores for each customer
* Identified top‐risk segments and key features influencing churn (e.g., tenure, payment lateness, usage decline)
* Recommended targeted retention strategies based on score and feature importance

---

## 📁 Project Structure

```
Customer-Churn-Analysis/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Customers with shorter tenure, increased payment lateness and sharp drop in usage had higher churn risk
* Derived features (e.g., usage change rate, payment lateness ratio) strongly improved model performance
* Regression approach allowed ranking customers by risk rather than simple binary classification
* Business teams can now prioritise retention efforts using churn risk scores

---

## 🚀 Future Improvements

* Integrate time-series or event-sequence modelling to capture churn patterns over time
* Deploy model as interactive dashboard or API for real-time churn risk monitoring
* Include external behavioural data (e.g., customer support interactions, social sentiment) to enhance prediction
* Implement feedback loop with live data to continuously update and calibrate risk model

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
