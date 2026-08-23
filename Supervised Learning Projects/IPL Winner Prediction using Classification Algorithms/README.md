# 🏏 IPL Winner Prediction using Classification Algorithms

A machine learning project focused on predicting the winning team for matches in the Indian Premier League (IPL) using team statistics, match features, and classification models.

---

## 📌 Project Overview

This project builds a comprehensive pipeline: gathering historical IPL match data (teams, venue, toss, score, player stats), performing exploratory analysis to reveal patterns, engineering features relevant to match outcome, training classification models, and evaluating their performance. The goal is to predict the winning team and derive key factors that influence match results.

---

## 🧰 Tech Stack

* **Language:** Python
* **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn
* **Environment:** Jupyter Notebook / Google Colab

---

## 🔄 Workflow Summary

### 1. Data Collection

Dataset includes features such as: match date, venue, toss winner, batting first/second, teams playing, score statistics, recent team form, and target label indicating match winner.

### 2. Exploratory Data Analysis (EDA)

* Distribution of wins by team, venue, toss outcome
* Visualisations of team performance by venue, head-to-head matchups, toss decision impact
* Correlation heatmap of numeric features
* Identification of missing values or anomalies

### 3. Feature Engineering

* Encoding categorical variables (team names, venues, toss outcome)
* Creating derived features such as recent form (last 5 matches), average runs scored at venue, toss win lead performance
* Incorporating match-specific features (home/away, venue bounce rates)
* Splitting dataset into training and test sets with stratified sampling

### 4. Modeling

Classification algorithms applied:

* **Logistic Regression** (baseline)
* **Random Forest Classifier** (strong performer)
* **(Optional) Gradient Boosting / XGBoost** for elevated performance

### 5. Evaluation

Metrics employed to measure model performance:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC (where applicable)

**Result:** The top performing classifier achieved strong accuracy in predicting the winning team, with derived features like toss decision, recent form and venue advantage contributing highly.

### 6. Prediction & Insights

* Generated predictions for upcoming or unseen matches
* Analysed feature importance: recent team form, venue history, toss decision emerged as critical predictors
* Offered practical insights: teams winning toss at certain venues and batting first exhibited edge; recent form carried significant weight

---

## 📁 Project Structure

```
IPL-Winner-Prediction/
│── data/
│── notebooks/
│── src/
│── README.md
│── requirements.txt
```

---

## 📈 Key Findings

* Toss winners batting first at specific venues had higher win probabilities
* Recent performance indicators (last 5 matches) strongly influenced match outcome predictions
* Feature engineering (venue form, toss decision) significantly improved model performance over raw match stats
* The classification pipeline provides actionable insights for analysts, fans and fantasy players

---

## 🚀 Future Improvements

* Incorporate player-level data (batting/bowling form, match fitness, injuries) for richer feature set
* Use time-series or deep learning approaches (e.g., RNN) to model momentum across matches
* Build a web app or API for live match-winner prediction or fantasy insights
* Monitor model fairness across teams and venues, ensure no bias toward historically dominant teams
* Continuously retrain model with fresh match data each season for improved relevance

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
