# 💼 Salary Prediction for Data Science Jobs using Regression Algorithms

A machine-learning project focused on predicting salaries for data-science roles using regression models built on job features and market data.

---

## 📌 Project Overview

This project builds an end-to-end pipeline: collecting job listing data (e.g., job role, experience, skills, location), exploratory analysis, feature engineering, training regression models, and evaluating their performance. The goal is to estimate data science job salaries and identify key salary-driving features for job seekers, HR and industry insight.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Job dataset features could include job title, years of experience, primary skills (e.g., Python, SQL, ML), location, company size, education level, and the target variable being salary (e.g., annual USD).

### 2. Exploratory Data Analysis (EDA)

* Visualisations: salary distribution, boxplots by location or skillset
* Correlation matrix of numeric features and salary
* Identification of outliers (very high salaries), feature skewness

### 3. Feature Engineering

* Encode categorical variables (job title, location, skills) via one-hot encoding or ordinal mapping
* Create derived features: e.g., “number of required skills”, “senior role flag”, “remote vs onsite”
* Log-transform salary target if skewed
* Split into training/test sets

### 4. Modelling

Regression algorithms employed:

* **Linear Regression** (baseline)
* **Random Forest Regressor** (strong performer)
* **Gradient Boosting Regressor** / XGBoost for advanced performance
  Hyper-parameter tuning via grid/random search (n_estimators, learning_rate, max_depth)

### 5. Evaluation

Performance metrics used:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² (coefficient of determination)
  **Result:** The top model achieved strong predictive results and provided insights into salary drivers.

### 6. Prediction & Insights

* Made salary predictions for new job listings based on features
* Analysed feature importances: years of experience, location, number of skills, company size emerged as strong predictors
* Provided recommendations for job seekers: focus on key skills or locations with higher salary potential

---

## 📁 Project Structure

```
Salary-Prediction-Data-Science-Jobs/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   └── salary_prediction_analysis.ipynb
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

* Years of experience and job location were the most influential factors in salary prediction
* Candidates with multiple key skills (e.g., ML + SQL + Python) tend to have higher predicted salaries
* Tree-based regressors like Random Forest and Gradient Boosting outperformed linear regression due to capturing non-linear interactions
* Log-transforming salary target improved model residuals and prediction stability

---

## 🚀 Future Improvements

* Include additional market/industry features: company revenue, demand trend, cost-of-living index for location
* Deploy as a web app where job seekers enter role details and obtain a salary estimate
* Use ensemble stacking/blending to further reduce prediction error
* Incorporate explainability (SHAP, LIME) so candidates/employers understand what drives the salary estimate
* Monitor salary-market drift and periodically retrain model with updated job-listing data

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
