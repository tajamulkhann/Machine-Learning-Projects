# 😊 Customer Satisfaction Analysis using Classification Algorithms

A machine learning project focused on predicting customer satisfaction using classification models, survey and business data, and feature engineering.

---

## 📌 Project Overview

This project builds a complete workflow: data ingest of customer survey and interaction metrics, exploratory analysis to uncover satisfaction drivers, feature engineering to create meaningful variables, building classification models and evaluating their performance. The objective is to accurately predict whether a customer is satisfied and derive actionable business insights.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset contains customer survey responses, interaction logs (usage, service calls), demographic and account attributes, and a target indicating satisfaction status.

### 2. Exploratory Data Analysis (EDA)

* Distribution of satisfied vs dissatisfied customers
* Visualisation of key features (e.g., interaction frequency, service quality ratings) across target classes
* Correlation matrix and feature relationships
* Identification of missing values, class imbalance and outliers

### 3. Feature Engineering

* Encoding categorical variables (e.g., region, plan type, feedback category)
* Creating derived features such as service calls per month, average rating change, tenure buckets
* Scaling/normalizing numerical features where required
* Splitting into training and test sets, using stratified sampling

### 4. Modeling

Classification algorithms applied:

* **Logistic Regression** (baseline)
* **Random Forest Classifier** (strong performer)
* **(Optional) Gradient Boosting / XGBoost** for further improvement

### 5. Evaluation

Key metrics used to assess model performance:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC

**Result:** The Random Forest (or chosen classifier) achieved high predictive accuracy, with engineered features significantly boosting model performance.

### 6. Prediction & Insights

* Generated predictions on unseen customer data for satisfaction status
* Analysed feature importance to identify key drivers (e.g., number of service calls, feedback rating, interaction frequency)
* Provided actionable business recommendations: e.g., targeting high-risk customers with service improvements, proactive engagement strategies

---

## 📁 Project Structure

```
Customer-Satisfaction-Analysis/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Customers with higher interaction frequency, lower service-call count, and higher feedback ratings are more likely to be satisfied
* Derived variables such as “service calls per month” and “rating change over last quarter” emerged as strong predictors
* Feature engineering improved classifier performance compared to raw data only
* The classification model provided reliable predictions, enabling business teams to identify and act on satisfaction risk early

---

## 🚀 Future Improvements

* Expand dataset with more diverse customer segments (geographies, product types) and longitudinal data
* Use advanced modelling such as ensemble stacking, deep learning (e.g., neural networks) or automated ML pipelines
* Deploy model via a web interface (Flask/Streamlit) for real-time prediction and dashboarding
* Integrate customer behavioural data from additional sources (social media sentiment, support chat logs)
* Monitor and analyse model fairness across demographic groups and adjust strategy accordingly

---

## 🧑‍💻 Author

**[Tajamul Khan](https://www.linkedin.com/in/tajamulkhann/) – Data Scientist & AI Engineer**

## Let’s Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

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
