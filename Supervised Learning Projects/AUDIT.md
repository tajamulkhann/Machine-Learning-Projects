# Supervised Portfolio Audit

Audit date: 24 August 2026
Owner: Tajamul Khan

## Decision criteria

Each original project was reviewed for notebook completeness, saved outputs, dataset availability or source instructions, path portability, duplicate work, problem framing, modeling validity, documentation, and stored runtime errors.

A project was classified as **Maintained** when its original notebook already provided a useful, readable workflow with saved evidence and no material structural problem. Those notebooks were not rewritten. Their README branding alone was synchronized to the locked creator block.

A project was classified as **Refurbished** only when the audit found a material issue that reduced reproducibility, correctness, or portfolio value.

## Maintained projects — 18

1. Airline Satisfaction Prediction using Classification Algorithms
2. Airlines Delay Prediction using Classification Algorithms
3. Banknote Authentication Using Classification Algorithms
4. Breast Cancer Prediction using Classification Algorithms
5. Chronic Kidney Disease Prediction Using Classifiation Algorithms
6. Credit Score Prediction using Classification Algorithm
7. Diabetes Prediction using Classification and Boosting Algorithm
8. Diamond Price Prediction using Regressor Algorithms
9. Drug Classification Using Classification Algorithms
10. E-Commerce Shipping Prediction using Classification Algorithm
11. Heart Disease Prediction using Classification Algorithms
12. Hotel Reservation Booking Status Prediction using Classification Algorithm
13. Kidney Stone Prediction using Classification Algorithm
14. Laptop Price Prediction using Regression Algorithms
15. Salary Prediction for Data Science Jobs using Regression Algorithms
16. Stroke Prediction using Machine Learning Classification Algorithm
17. Used Vehicle Price Prediction using Regression Algorithm
18. Vehicle Insurance Claim Fraud Detection using Classification Algorithms

## Refurbished projects — 11

| Project | Material audit finding | Resolution |
|---|---|---|
| Airbnb Stock Price Prediction | Stock dataset was stored in the airline-satisfaction folder; time-series evaluation needed a naive benchmark | Moved the data, used chronological validation, and compared against previous-close and median baselines |
| Customer Churn Analysis using Classification Algorithms | Nonstandard README name and single-model rough workflow | Added a canonical notebook, leakage-safe pipeline, baseline, CV, holdout diagnostics, and README |
| Customer Churn Analysis using Logistic Regression | Folder called a binary churn problem “regression,” creating misleading framing | Corrected the title to logistic regression and rebuilt probability-based classification evaluation |
| Customer Satisfaction Analysis using Classification Algorithms | Dataset absent, README nonstandard, and notebook stored an execution error | Rebuilt as a deterministic text-classification demonstration with realistic ambiguity and saved outputs |
| Housing Cost Prediction using Regression Algorithms | Notebook pinned obsolete NumPy and depended on an unavailable dataset | Rebuilt as a portable housing-cost regression workflow with reproducible domain-shaped data |
| IPL Winner Prediction using Classification Algorithms | Hard-coded personal Google Drive path and no committed dataset | Rebuilt with pre-match-only features, deterministic demo data, and no post-match leakage |
| Insurance Premium Prediction using Regression Algorithms | Dataset filename mismatch and stale exported PDF | Corrected the data contract, rebuilt the pipeline, executed on committed data, and removed stale export |
| Loan Approval Prediction using Classification Algorithms | Hard-coded Kaggle path despite committed train/test files | Replaced with portable path resolution, class-aware validation, and holdout diagnostics |
| Rain Prediction in Australia using Classification Algorithms | Filename mismatch broke execution on case-sensitive systems | Corrected portable data loading and rebuilt the classification pipeline |
| Rainfall Amount Prediction using Regression Algorithms | Original “regression” notebook duplicated the rain/no-rain classifier | Reframed the target as rainfall amount and added genuine regression metrics and diagnostics |
| Telemarketing Campaign Response using Classification Algorithms | Two duplicate notebooks and incorrect regression framing for a binary response | Consolidated to one canonical classification notebook with baseline, CV, and holdout evaluation |

## New projects — 21

The expansion adds high-interest supervised use cases across NLP, risk, healthcare, operations, pricing, agriculture, and forecasting:

1. AI Resume Screening and Candidate Fit Prediction
2. Fake News Detection with NLP
3. Phishing URL Detection
4. Email Spam Detection
5. Toxic Comment Classification
6. Customer Support Ticket Routing
7. Product Review Sentiment Analysis
8. Employee Attrition Risk Prediction
9. Credit Card Default Risk Prediction
10. Hospital Readmission Risk Prediction
11. E-Commerce Purchase Intention Prediction
12. Predictive Maintenance Failure Prediction
13. Traffic Accident Severity Prediction
14. Insurance Claim Severity Prediction
15. Customer Lifetime Value Prediction
16. Food Delivery ETA Prediction
17. Flight Fare Prediction
18. Crop Yield Prediction
19. Supply Chain Cost Prediction
20. Retail Demand Forecasting
21. Energy Consumption Forecasting

## Execution policy

- Original maintained notebooks retain their existing outputs.
- All 11 refurbished notebooks were executed after repair.
- All 21 new notebooks were executed end to end.
- Outputs, plots, model comparisons, and diagnostics are intentionally committed for portfolio reviewers.
- Deterministic demo results are labeled as demonstrations and are not presented as production benchmarks.
