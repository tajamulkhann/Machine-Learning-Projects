# 🛡️ Insurance Premium Prediction using Regression Algorithms

A machine learning project focused on estimating insurance premium costs using regression models, insured demographics, policy attributes, and historical claims data.

---

## 📌 Project Overview

This project covers the complete workflow: ingesting data on insured individuals (age, sex, BMI, smoking status, region, prior claims), performing exploratory data analysis to uncover cost determinants, engineering new features, building regression models, and evaluating their performance. The objective is to provide accurate premium estimations and insights into cost-drivers.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes variables like: age, sex, BMI, smoking status, children, region, prior insurance claims, policy type, and a target variable for annual premium cost.

### 2. Exploratory Data Analysis (EDA)

* Distribution of premium cost values across demographics
* Visualizations of premium vs features such as age, BMI, smoking status
* Correlation matrix to identify key relationships
* Detection of missing values, outliers and skewed target distribution

### 3. Feature Engineering

* Encoding categorical variables (e.g., sex, smoking status, region)
* Creating derived features like BMI category, smoker × age interaction, number of dependents bucket
* Log-transforming skewed target or heavy-tailed features
* Scaling numerical features for regression compatibility
* Splitting dataset into training and test sets

### 4. Modeling

Regression algorithms applied include:

* **Linear Regression** (baseline)
* **Random Forest Regressor** or **Gradient Boosting Regressor** (strong performers)
* **(Optional) XGBoost / LightGBM** for improved estimation

### 5. Evaluation

Metrics used to assess model performance:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² score
* Residuals analysis and distribution

**Result:** The top performing regression model achieved low error rates and high R², demonstrating reliable premium estimates and highlighting key cost-drivers such as smoking status, BMI and age.

### 6. Prediction & Insights

* Generated premium estimates for new policyholder profiles
* Analysed feature importance: age, smoking status, BMI category emerged as leading predictors
* Provided actionable insights: smokers and higher BMI categories significantly raise premium cost; demographic segmentation for risk-based pricing

---

## 📁 Project Structure

```
Insurance-Premium-Prediction/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Smoker status had the most significant impact on premium cost, followed by BMI and age
* Interaction features and derived feature transformations improved estimation accuracy
* Regression models such as Random Forest and Gradient Boosting outperformed linear baseline
* The prediction framework supports insurers with data-driven premium pricing and risk assessment

---

## 🚀 Future Improvements

* Include additional data such as claims history, policy duration, and external health indicators (e.g., fitness tracker data)
* Explore deep learning and sequence models (e.g., for recurring claims or longitudinal insured behavior)
* Deploy as a web or mobile app (Flask/Streamlit) for real-time premium prediction and quoting
* Implement fairness and bias analysis to ensure equitable pricing across demographics
* Enable continuous model update with real-world feedback and claim-outcome data

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
