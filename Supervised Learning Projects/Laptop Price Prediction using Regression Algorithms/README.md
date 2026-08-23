# 💻 Laptop Price Prediction using Regression Algorithms

A machine-learning project focused on predicting the price of laptops based on their technical specifications and applying regression algorithms, feature engineering, and evaluation metrics.

---

## 📌 Project Overview

This project constructs an end-to-end pipeline: loading a dataset of laptop specifications (brand, screen size, CPU, RAM, memory, etc.), performing exploratory data analysis, engineering features, training regression models (Linear Regression, Random Forest, Gradient Boosting) and evaluating their performance. The goal is to build a model that can estimate a laptop’s fair price based on its configuration and understand which factors drive pricing.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes attributes such as company, type, inches, screen resolution, CPU, RAM, memory type, weight, and price target. See similar projects for context. ([Kaggle][1])

### 2. Exploratory Data Analysis (EDA)

* Distribution of laptop prices
* Boxplots of price by brand, type, CPU, memory type
* Correlation matrix of numeric features and price

### 3. Feature Engineering

* Encode categorical features (company, type, CPU brand) using one-hot or label encoding
* Derive features such as e.g., memory size category, weight bucket
* Log-transform skewed variables (e.g., price) if needed
* Split into training and test sets

### 4. Modelling

Regression algorithms used:

* **Linear Regression** (baseline)
* **Random Forest Regressor**
* **Gradient Boosting Regressor** / XGBoost
  Hyper-parameter tuning via grid search or random search

### 5. Evaluation

Metrics used:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² (coefficient of determination)
  Result: The best model achieved strong accuracy and good generalisation on unseen data.

### 6. Prediction & Insights

* Predictions generated for new laptop configurations
* Feature importance extracted from tree-based models to identify key drivers: e.g., RAM size, storage type (SSD vs HDD), CPU brand, screen size
* Business insights: Understand premium paid for certain brands/specs, help consumers estimate fair price

---

## 📁 Project Structure

```
Laptop-Price-Prediction/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   └── laptop_price_analysis.ipynb
│── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── models.py
│   └── evaluate.py
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Features such as **brand**, **RAM**, **memory type**, and **CPU spec** showed strong influence on price.
* Tree-based regressors (Random Forest / Gradient Boosting) outperformed linear regression due to capturing non-linear interactions.
* Log-transformation of target and some numeric features improved model fit and reduced skew in residuals.
* The project demonstrated how practical regression models can support consumers and retailers in price estimation.

---

## 🚀 Future Improvements

* Include external factors like release year, market region, currency, depreciation rate for richer modelling.
* Build a web app (e.g., using Streamlit) where users can input specs and get an estimated price.
* Use ensemble stacking or model blending to reduce error further.
* Add explainability (SHAP values) so users understand how each feature affected the predicted price.
* Monitor and update model as laptop market trends change (new specs, emerging brands).

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
