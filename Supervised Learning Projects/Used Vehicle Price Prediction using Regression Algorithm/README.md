# 🚗 Used Vehicle Price Prediction using Regression Algorithms

A machine learning project focused on estimating the selling price of used vehicles by leveraging regression models built on vehicle specifications, condition, and market factors.

---

## 📌 Project Overview

This project implements an end-to-end workflow: data collection of used vehicle listings (brand, model, year, mileage, condition, transmission, fuel type), exploratory data analysis to understand pricing patterns, feature engineering, training regression models (Linear Regression, Random Forest, Gradient Boosting), and evaluating performance. The goal is to accurately predict a used vehicle’s market price and derive insights into factors driving price.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes used vehicle listings featuring attributes such as: brand, model, year, mileage, transmission type, fuel type, vehicle condition, location, and the target variable being selling price.

### 2. Exploratory Data Analysis (EDA)

* Visualised price distributions and outliers
* Boxplots of price by brand/model, condition, fuel type
* Scatterplots of price vs mileage, age of vehicle
* Correlation matrix of numeric features and price

### 3. Feature Engineering

* Encoded categorical features (brand, model, transmission, fuel type) via one-hot or label encoding
* Derived features such as age of vehicle (current year − manufacture year), mileage per year, price per mileage unit
* Log-transformed skewed variables (e.g., price and mileage) if needed
* Split data into training and test sets

### 4. Modelling

Regression algorithms used:

* **Linear Regression** (baseline)
* **Random Forest Regressor**
* **Gradient Boosting Regressor** or **XGBoost** for improved performance
  Hyper-parameter tuning via GridSearchCV/RandomizedSearchCV (e.g., n_estimators, max_depth, learning_rate)

### 5. Evaluation

Metrics employed:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² (coefficient of determination)
  **Result:** The top performing model achieved good generalisation, accurately estimating used vehicle price within a reasonable error margin.

### 6. Prediction & Insights

* Predictions generated for new vehicle listings and compared predicted vs actual price
* Analysed feature importances: vehicle age, mileage, brand/model, condition emerged as strongest predictors
* Business insights: buyers and sellers can estimate fair market price; dealerships can optimise pricing strategy

---

## 📁 Project Structure

```
Used-Vehicle-Price-Prediction/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   └── used_vehicle_price_analysis.ipynb
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

* Vehicle age and mileage have the largest impact on resale price, with older cars and higher mileage predicting lower prices
* Model and brand also influence price significantly — premium brands command higher resale value
* Tree-based regressors (Random Forest / Gradient Boosting) outperformed linear regression by capturing non-linear interactions
* Log-transforming price helped reduce skew and improved model fit

---

## 🚀 Future Improvements

* Integrate external market factors such as vehicle demand trends, regional pricing differences, currency/inflation effects
* Deploy as a web app (using Flask or Streamlit) allowing users to enter vehicle specs and receive a price estimate
* Use ensemble methods (stacking/blending) to further reduce prediction error
* Incorporate explainability (e.g., SHAP values) to provide transparency in pricing decisions
* Monitor model drift over time as vehicle market dynamics evolve (new models, regulations, electric vehicles, etc.)

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
