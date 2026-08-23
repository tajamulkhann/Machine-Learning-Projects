# Supervised Learning Projects

A curated portfolio of **29 supervised machine learning projects** covering classification, regression, time-aware validation and natural language processing.

Every project now has a portable notebook, a project-specific README, leakage-safe Scikit-learn pipelines, reproducible splits, a dummy baseline, appropriate metrics and a clear dataset acquisition path. Performance claims are never invented: notebooks calculate results only from the data available at execution time.

## Project directory

| # | Project | Type | Core models | Data | QA |
|---:|---|---|---|---|---|
| 01 | [Airbnb Stock Price Prediction](Airbnb%20Stock%20Price%20Prediction/) | Regression | Naive previous close, Ridge Regression, Random Forest | Included | Executed |
| 02 | [Airline Passenger Satisfaction Classification](Airline%20Satisfaction%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 03 | [Airline Delay Classification](Airlines%20Delay%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 04 | [Banknote Authentication Classification](Banknote%20Authentication%20Using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 05 | [Breast Cancer Diagnostic Classification](Breast%20Cancer%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Support Vector Machine, Random Forest | Included | Executed |
| 06 | [Chronic Kidney Disease Classification](Chronic%20Kidney%20Disease%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, K-Nearest Neighbors, Random Forest | Download | Static |
| 07 | [Credit Score Classification](Credit%20Score%20Prediction%20using%20Classification%20Algorithm/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 08 | [Customer Churn Analysis with Logistic Regression](Customer%20Churn%20Analysis%20using%20Logistic%20Regression/) | Classification | Logistic Regression | Included | Executed |
| 09 | [Customer Churn Classification](Customer%20Churn%20Analysis%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 10 | [Customer Review Sentiment Classification](Customer%20Satisfaction%20Analysis%20using%20Classification%20Algorithms/) | Classification | Multinomial Naive Bayes, Logistic Regression | Download | Static |
| 11 | [Diabetes Classification with Tree and Boosting Models](Diabetes%20Prediction%20using%20Classification%20and%20Boosting%20Algorithm/) | Classification | Decision Tree, Random Forest, AdaBoost | Download | Static |
| 12 | [Diamond Price Regression](Diamond%20Price%20Prediction%20using%20Regressor%20Algorithms/) | Regression | Ridge Regression, Decision Tree, Random Forest | Download | Static |
| 13 | [Drug Type Classification](Drug%20Classification%20Using%20Classification%20Algorithms/) | Classification | Logistic Regression, Random Forest, AdaBoost | Download | Static |
| 14 | [E-Commerce Shipping Outcome Classification](E-Commerce%20Shipping%20Prediction%20using%20Classification%20Algorithm/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 15 | [Heart Disease Classification](Heart%20Disease%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 16 | [Hotel Booking Status Classification](Hotel%20Reservation%20Booking%20Status%20Prediction%20using%20Classification%20Algorithm/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 17 | [New York Housing Project Cost Regression](Housing%20Cost%20Prediction%20using%20Regression%20Algorithms/) | Regression | Ridge Regression, Decision Tree, Random Forest | Download | Static |
| 18 | [IPL Match Winner Classification](IPL%20Winner%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Random Forest | Download | Static |
| 19 | [Insurance Premium Regression](Insurance%20Premium%20Prediction%20using%20Regression%20Algorithms/) | Regression | Linear Regression, Random Forest, Gradient Boosting | Included | Executed |
| 20 | [Kidney Stone Classification](Kidney%20Stone%20Prediction%20using%20Classification%20Algorithm/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 21 | [Laptop Price Regression](Laptop%20Price%20Prediction%20using%20Regression%20Algorithms/) | Regression | Ridge Regression, Decision Tree, Random Forest | Download | Static |
| 22 | [Loan Approval Classification](Loan%20Approval%20Prediction%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 23 | [Next-Day Rain Classification in Australia](Rain%20Prediction%20in%20Australia%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 24 | [Rainfall Amount Regression in Australia](Rainfall%20Amount%20Prediction%20using%20Regression%20Algorithms/) | Regression | Ridge Regression, Decision Tree, Random Forest | Included | Executed |
| 25 | [Data Science Salary Regression](Salary%20Prediction%20for%20Data%20Science%20Jobs%20using%20Regression%20Algorithms/) | Regression | Ridge Regression, Decision Tree, Random Forest | Download | Static |
| 26 | [Stroke Risk Classification](Stroke%20Prediction%20using%20Machine%20Learning%20Classification%20Algorithm/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |
| 27 | [Telemarketing Campaign Response Classification](Telemarketing%20Campaign%20Response%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Included | Executed |
| 28 | [Used Vehicle Price Regression](Used%20Vehicle%20Price%20Prediction%20using%20Regression%20Algorithm/) | Regression | Ridge Regression, Decision Tree, Random Forest | Download | Static |
| 29 | [Vehicle Insurance Claim Fraud Classification](Vehicle%20Insurance%20Claim%20Fraud%20Detection%20using%20Classification%20Algorithms/) | Classification | Logistic Regression, Decision Tree, Random Forest | Download | Static |

## Shared methodology

- Preprocessing is fitted inside pipelines and cross-validation folds.
- Final holdout data is untouched until model selection is complete.
- Classification projects report macro F1 and class-level errors, not accuracy alone.
- Regression projects report MAE, RMSE, R² and residual diagnostics.
- Dated projects use chronological validation where the original random split would leak future context.
- Sensitive identifiers and obvious post-outcome fields are excluded from modelling.

## Run a project

```bash
git clone https://github.com/tajamulkhann/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/Supervised Learning Projects"
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Projects marked **Download** include the expected filename and recorded source in their README. Respect the source dataset's licence and usage terms.

**QA legend:** Executed = the notebook completed against the committed dataset. Static = every code cell compiles and the notebook structure passed validation, but runtime metrics are intentionally omitted because the dataset is not committed.

## Author

**Tajamul Khan**

## Let's Connect <img src="https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.codes/" target="_blank">
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
