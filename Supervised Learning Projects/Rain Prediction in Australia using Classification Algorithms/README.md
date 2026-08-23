# 🌦️ Rain Prediction in Australia Using Classification Algorithms

A machine-learning project focused on predicting whether it will rain the next day in Australia using meteorological features and classification models.

---

## 📌 Project Overview

This project builds a full pipeline: loading historical weather data for Australian locations, exploratory data analysis, feature engineering (temperature, humidity, wind, rainfall history, etc.), model training (classification algorithms), evaluation metrics and insight extraction. The goal is to predict the binary outcome of “RainTomorrow” and provide actionable insights for weather-aware planning.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

The dataset includes daily weather observations for various Australian locations: features like MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustSpeed, Humidity3pm, Pressure9am, and a target column “RainTomorrow” (Yes/No).

### 2. Exploratory Data Analysis (EDA)

* Distribution of “RainTomorrow = Yes” vs “No”
* Boxplots & histograms for features (e.g., rainfall, humidity) by target class
* Correlation matrix of numeric features with the target and amongst themselves
* Handling missing values, outlier detection, balancing the dataset

### 3. Feature Engineering

* Encoding categorical location/season variables
* Creating derived features: e.g., previous day rainfall flag, variation between MinTemp & MaxTemp, wind direction encoding
* Scaling numeric features where required (StandardScaler/MinMax)
* Splitting dataset into training and test sets (stratified by target)

### 4. Modeling

Classification algorithms implemented:

* **Logistic Regression** (baseline)
* **Random Forest Classifier** (strong performer)
* **Gradient Boosting / XGBoost** for advanced performance
  Hyper-parameter tuning via GridSearchCV/RandomizedSearchCV for parameters like n_estimators, max_depth, learning_rate

### 5. Evaluation

Performance metrics used include:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC
  **Result:** The best model achieved good recall on the “RainTomorrow = Yes” class (important for catching rainfall) and balanced precision and recall for practical use.

### 6. Insights & Business Application

* Important predictors identified: humidity at 3 pm, rainfall today, wind gust speed, pressure at 9 am and previous day rainfall.
* When humidity is high and there was rainfall today, the likelihood of rain tomorrow increases.
* Practical recommendation: Use prediction to inform outdoor event planning, agriculture scheduling, and weather-alert systems.

---

## 📁 Project Structure

```
Rain-Prediction-Australia/
│── data/
│   ├── raw/
│   └── processed/
│── notebooks/
│   └── rain_prediction_analysis.ipynb
│── src/
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate.py
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Humidity and previous day rainfall were among the top predictors for rain tomorrow.
* Tree-based classifiers like Random Forest and Gradient Boosting outperformed logistic regression due to ability to model non-linear interactions.
* Balancing data (e.g., via oversampling the “Yes” class or using class weights) improved recall for rainfall prediction.
* Feature scaling and careful missing-value handling improved model stability.

---

## 🚀 Future Improvements

* Incorporate **time-series features**: sequences of weather data over previous days, roll-windows of rainfall and temperature.
* Explore **ensemble stacking** of classification models (Random Forest + XGBoost + LightGBM) to improve accuracy.
* Deploy as a web service/dashboard where users input location + recent weather and get probability of rain tomorrow.
* Integrate **explainability tools** (SHAP values) so users understand which features contributed most to each prediction.
* Use additional data sources: satellite imagery, radar data, micro-climate sensors, and expand geography beyond Australia.

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
