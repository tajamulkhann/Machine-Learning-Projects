#!/usr/bin/env python3
"""Build the selective supervised-learning portfolio expansion.

The script creates 21 reproducible portfolio projects, refreshes the supervised
index, and preserves Tajamul Khan's locked connection block verbatim.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPERVISED = ROOT / "Supervised Learning Projects"
RANDOM_STATE = 42


def locked_connect_block() -> str:
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    marker = "## Let's Connect"
    if marker not in root_readme:
        raise RuntimeError("The locked Let's Connect block is missing from README.md")
    return marker + root_readme.split(marker, 1)[1].rstrip() + "\n"


CONNECT = locked_connect_block()


def markdown(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.strip() + "\n",
    }


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.strip() + "\n",
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


COMMON_IMPORTS = """
import platform
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn

warnings.filterwarnings("ignore")
RANDOM_STATE = 42
rng = np.random.default_rng(RANDOM_STATE)
sns.set_theme(style="whitegrid", palette="deep")

print(f"Python: {platform.python_version()}")
print(f"pandas: {pd.__version__} | NumPy: {np.__version__} | scikit-learn: {sklearn.__version__}")
print(f"Random seed: {RANDOM_STATE}")
"""


TEXT_PROJECTS = [
    {
        "title": "AI Resume Screening and Candidate Fit Prediction",
        "slug": "ai_resume_screening_candidate_fit",
        "summary": "Prioritize resumes for human review using transparent NLP features rather than opaque keyword filtering.",
        "text_column": "resume_text",
        "target": "fit_decision",
        "topics": {
            "shortlist": ["python", "sql", "machine learning", "deployment", "experimentation", "stakeholder", "cloud", "analytics"],
            "review": ["beginner", "coursework", "support", "documentation", "operations", "manual", "internship", "learning"],
        },
    },
    {
        "title": "Fake News Detection with NLP",
        "slug": "fake_news_detection_nlp",
        "summary": "Classify news-like text while documenting uncertainty, source verification, and the limits of linguistic signals.",
        "text_column": "article_text",
        "target": "news_label",
        "topics": {
            "credible": ["report", "evidence", "official", "research", "statement", "verified", "source", "data"],
            "misleading": ["shocking", "secret", "miracle", "exposed", "urgent", "unbelievable", "viral", "hidden"],
        },
    },
    {
        "title": "Phishing URL Detection",
        "slug": "phishing_url_detection",
        "summary": "Flag suspicious URLs using character and token patterns, with recall emphasized for security triage.",
        "text_column": "url_text",
        "target": "url_label",
        "topics": {
            "legitimate": ["https", "account", "docs", "support", "company", "secure", "help", "profile"],
            "phishing": ["verify-now", "free-prize", "login-update", "urgent", "bonus", "claim", "password", "suspicious-domain"],
        },
    },
    {
        "title": "Email Spam Detection",
        "slug": "email_spam_detection",
        "summary": "Build a precision-aware spam classifier that demonstrates modern text pipelines and threshold trade-offs.",
        "text_column": "email_text",
        "target": "email_label",
        "topics": {
            "ham": ["meeting", "project", "schedule", "review", "team", "document", "update", "tomorrow"],
            "spam": ["winner", "cash", "offer", "click", "limited", "free", "prize", "deal"],
        },
    },
    {
        "title": "Toxic Comment Classification",
        "slug": "toxic_comment_classification",
        "summary": "Detect harmful comments for moderation queues while highlighting context, fairness, and appeal workflows.",
        "text_column": "comment_text",
        "target": "moderation_label",
        "topics": {
            "constructive": ["helpful", "consider", "evidence", "suggestion", "respect", "clarify", "improve", "discussion"],
            "toxic": ["idiot", "hate", "worthless", "stupid", "attack", "awful", "trash", "shut-up"],
        },
    },
    {
        "title": "Customer Support Ticket Routing",
        "slug": "customer_support_ticket_routing",
        "summary": "Route incoming support tickets to the right team with a multiclass NLP model and interpretable terms.",
        "text_column": "ticket_text",
        "target": "support_team",
        "topics": {
            "billing": ["invoice", "refund", "charge", "payment", "subscription", "receipt", "price", "billing"],
            "technical": ["error", "crash", "login", "api", "timeout", "bug", "install", "technical"],
            "delivery": ["shipment", "tracking", "courier", "package", "late", "address", "dispatch", "delivery"],
            "account": ["profile", "password", "access", "email", "security", "verification", "account", "locked"],
        },
    },
    {
        "title": "Product Review Sentiment Analysis",
        "slug": "product_review_sentiment",
        "summary": "Convert customer reviews into sentiment signals for product teams without hiding class-level performance.",
        "text_column": "review_text",
        "target": "sentiment",
        "topics": {
            "negative": ["broken", "slow", "poor", "refund", "disappointed", "bad", "late", "unusable"],
            "neutral": ["average", "standard", "expected", "okay", "normal", "basic", "fine", "regular"],
            "positive": ["excellent", "fast", "useful", "quality", "recommend", "perfect", "happy", "reliable"],
        },
    },
]


CLASSIFICATION_PROJECTS = [
    {
        "title": "Employee Attrition Risk Prediction",
        "slug": "employee_attrition_risk",
        "summary": "Estimate voluntary attrition risk for workforce planning without treating predictions as employment decisions.",
        "target": "attrition",
        "numeric": ["monthly_income", "years_at_company", "overtime_hours", "job_satisfaction", "commute_km", "training_hours"],
        "categorical": {"department": ["engineering", "sales", "operations", "finance"], "work_mode": ["office", "hybrid", "remote"]},
    },
    {
        "title": "Credit Card Default Risk Prediction",
        "slug": "credit_card_default_risk",
        "summary": "Predict payment default probability with calibrated evaluation and explicit responsible-lending limitations.",
        "target": "defaulted",
        "numeric": ["credit_limit", "utilization", "late_payments", "income", "debt_ratio", "account_age_months"],
        "categorical": {"employment_type": ["salaried", "self_employed", "contract"], "region": ["north", "south", "east", "west"]},
    },
    {
        "title": "Hospital Readmission Risk Prediction",
        "slug": "hospital_readmission_risk",
        "summary": "Identify patients who may need additional post-discharge support using recall-aware evaluation.",
        "target": "readmitted_30d",
        "numeric": ["age", "length_of_stay", "prior_admissions", "medication_count", "lab_risk_score", "followup_days"],
        "categorical": {"admission_type": ["emergency", "elective", "urgent"], "discharge_route": ["home", "rehab", "care_center"]},
    },
    {
        "title": "E-Commerce Purchase Intention Prediction",
        "slug": "ecommerce_purchase_intention",
        "summary": "Predict session conversion intent from browsing behavior for better experimentation and merchandising.",
        "target": "purchased",
        "numeric": ["pages_viewed", "session_minutes", "cart_items", "discount_pct", "prior_orders", "days_since_last_visit"],
        "categorical": {"device": ["mobile", "desktop", "tablet"], "traffic_source": ["search", "social", "email", "direct"]},
    },
    {
        "title": "Predictive Maintenance Failure Prediction",
        "slug": "predictive_maintenance_failure",
        "summary": "Predict near-term equipment failures from operating conditions with failure recall and intervention costs in view.",
        "target": "failure_next_cycle",
        "numeric": ["temperature", "vibration", "pressure", "runtime_hours", "load_pct", "days_since_service"],
        "categorical": {"machine_type": ["pump", "compressor", "motor"], "shift": ["day", "evening", "night"]},
    },
    {
        "title": "Traffic Accident Severity Prediction",
        "slug": "traffic_accident_severity",
        "summary": "Predict severe accident risk to support planning—not automated enforcement—from weather and road context.",
        "target": "severe_accident",
        "numeric": ["speed_limit", "visibility_km", "traffic_density", "driver_age", "vehicles_involved", "response_minutes"],
        "categorical": {"weather": ["clear", "rain", "fog"], "road_type": ["urban", "highway", "rural"]},
    },
]


REGRESSION_PROJECTS = [
    {
        "title": "Insurance Claim Severity Prediction",
        "slug": "insurance_claim_severity",
        "summary": "Estimate claim cost severity for reserving workflows with robust error metrics and human review.",
        "target": "claim_cost",
        "numeric": ["vehicle_age", "driver_age", "annual_mileage", "prior_claims", "repair_hours", "damage_score"],
        "categorical": {"vehicle_type": ["sedan", "suv", "truck"], "claim_channel": ["app", "agent", "call_center"]},
    },
    {
        "title": "Customer Lifetime Value Prediction",
        "slug": "customer_lifetime_value",
        "summary": "Estimate customer lifetime value for retention prioritization while separating prediction from causal impact.",
        "target": "lifetime_value",
        "numeric": ["orders_12m", "avg_order_value", "tenure_months", "return_rate", "support_tickets", "engagement_score"],
        "categorical": {"segment": ["consumer", "small_business", "enterprise"], "acquisition_channel": ["search", "referral", "partner", "social"]},
    },
    {
        "title": "Food Delivery ETA Prediction",
        "slug": "food_delivery_eta",
        "summary": "Predict delivery time from distance, preparation, traffic, weather, and courier context.",
        "target": "eta_minutes",
        "numeric": ["distance_km", "prep_minutes", "traffic_index", "courier_rating", "active_orders", "rain_mm"],
        "categorical": {"vehicle": ["bike", "scooter", "car"], "time_window": ["breakfast", "lunch", "dinner", "late_night"]},
    },
    {
        "title": "Flight Fare Prediction",
        "slug": "flight_fare_prediction",
        "summary": "Estimate flight fares from booking lead time, route, schedule, stops, and demand signals.",
        "target": "fare",
        "numeric": ["days_before_departure", "distance_km", "duration_minutes", "stops", "demand_index", "remaining_seats"],
        "categorical": {"cabin": ["economy", "premium", "business"], "departure_slot": ["morning", "afternoon", "evening", "night"]},
    },
    {
        "title": "Crop Yield Prediction",
        "slug": "crop_yield_prediction",
        "summary": "Predict crop yield from environmental and farm-management features with uncertainty-aware interpretation.",
        "target": "yield_tonnes_per_hectare",
        "numeric": ["rainfall_mm", "temperature_c", "soil_ph", "fertilizer_kg", "irrigation_hours", "sunlight_hours"],
        "categorical": {"crop": ["rice", "wheat", "maize"], "soil_type": ["clay", "loam", "sandy"]},
    },
    {
        "title": "Supply Chain Cost Prediction",
        "slug": "supply_chain_cost_prediction",
        "summary": "Predict logistics cost for budgeting and network planning using operational, route, and service features.",
        "target": "logistics_cost",
        "numeric": ["distance_km", "weight_kg", "fuel_index", "handling_hours", "inventory_days", "delay_hours"],
        "categorical": {"transport_mode": ["road", "rail", "sea", "air"], "service_level": ["standard", "priority", "express"]},
    },
]


FORECAST_PROJECTS = [
    {
        "title": "Retail Demand Forecasting",
        "slug": "retail_demand_forecasting",
        "summary": "Forecast daily unit demand with chronological validation, calendar signals, promotions, and a naive baseline.",
        "target": "units_sold",
        "driver": "promotion_pct",
    },
    {
        "title": "Energy Consumption Forecasting",
        "slug": "energy_consumption_forecasting",
        "summary": "Forecast daily energy demand from weather, calendar, and lag features using time-aware validation.",
        "target": "energy_mwh",
        "driver": "temperature_c",
    },
]


REPAIRED_DEMO_PROJECTS = {
    "text": [
        {
            "title": "Customer Satisfaction Analysis using Classification Algorithms",
            "slug": "customer_review_sentiment_classification",
            "summary": "Classify customer feedback into satisfaction levels with transparent NLP baselines and class-aware metrics.",
            "text_column": "customer_review",
            "target": "satisfaction",
            "topics": {
                "dissatisfied": ["broken", "slow", "refund", "poor", "late", "unhelpful", "bad", "disappointed"],
                "neutral": ["average", "standard", "expected", "okay", "normal", "basic", "fine", "regular"],
                "satisfied": ["excellent", "fast", "helpful", "quality", "recommend", "perfect", "happy", "reliable"],
            },
        }
    ],
    "classification": [
        {
            "title": "IPL Winner Prediction using Classification Algorithms",
            "slug": "ipl_winner_classification",
            "summary": "Predict whether the listed home-side team wins an IPL-style match from pre-match context without using post-match leakage.",
            "target": "home_team_won",
            "numeric": ["home_recent_win_pct", "away_recent_win_pct", "home_net_run_rate", "away_net_run_rate", "toss_advantage", "rest_days"],
            "categorical": {"venue_type": ["home", "neutral", "away"], "match_stage": ["league", "qualifier", "playoff"]},
        }
    ],
    "regression": [
        {
            "title": "Housing Cost Prediction using Regression Algorithms",
            "slug": "new_york_housing_cost_regression",
            "summary": "Estimate monthly housing cost from size, location, building, amenity, and market features with honest error analysis.",
            "target": "monthly_housing_cost",
            "numeric": ["area_sqft", "bedrooms", "bathrooms", "building_age", "transit_score", "amenity_score"],
            "categorical": {"borough": ["manhattan", "brooklyn", "queens", "bronx"], "property_type": ["studio", "apartment", "townhouse"]},
        }
    ],
}


def text_cells(cfg: dict) -> list[dict]:
    topics = json.dumps(cfg["topics"], indent=2)
    return [
        markdown(f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\nThis notebook uses deterministic demo text so the complete workflow runs without private or externally hosted data. Labels are used only for supervised training and evaluation."),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Build the documented demo dataset"),
        code(f"""
TOPICS = {topics}
COMMON_WORDS = ["customer", "service", "today", "online", "request", "information", "please", "system"]
rows = []
for label, vocabulary in TOPICS.items():
    for row_id in range(180):
        signal = rng.choice(vocabulary, size=6, replace=True).tolist()
        context = rng.choice(COMMON_WORDS, size=4, replace=True).tolist()
        other_labels = [name for name in TOPICS if name != label]
        cross_noise = []
        if rng.random() < 0.35:
            other = rng.choice(other_labels)
            cross_noise = rng.choice(TOPICS[other], size=3, replace=True).tolist()
        tokens = signal + context + cross_noise
        rng.shuffle(tokens)
        observed_label = rng.choice(other_labels) if rng.random() < 0.08 else label
        rows.append({{"{cfg['text_column']}": " ".join(tokens), "{cfg['target']}": observed_label}})

data = pd.DataFrame(rows).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
print(f"Dataset shape: {{data.shape[0]:,}} rows × {{data.shape[1]}} columns")
display(data.head())
display(data["{cfg['target']}"].value_counts().rename("count").to_frame())
"""),
        markdown("## 3. Data quality and exploratory analysis"),
        code(f"""
quality = pd.DataFrame({{
    "dtype": data.dtypes.astype(str),
    "missing": data.isna().sum(),
    "unique": data.nunique(),
}})
display(quality)
data["text_length"] = data["{cfg['text_column']}"].str.split().str.len()
sns.boxplot(data=data, x="{cfg['target']}", y="text_length", color="#60a5fa")
plt.title("Document length by class")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
"""),
        markdown("## 4. Leakage-safe split, baseline, and candidate models"),
        code(f"""
from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, f1_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

X_train, X_test, y_train, y_test = train_test_split(
    data["{cfg['text_column']}"], data["{cfg['target']}"], test_size=0.25,
    random_state=RANDOM_STATE, stratify=data["{cfg['target']}"],
)
models = {{
    "Majority baseline": Pipeline([("tfidf", TfidfVectorizer()), ("model", DummyClassifier(strategy="prior"))]),
    "Multinomial Naive Bayes": Pipeline([("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)), ("model", MultinomialNB(alpha=0.6))]),
    "Logistic Regression": Pipeline([("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)), ("model", LogisticRegression(max_iter=2000, random_state=RANDOM_STATE))]),
}}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
comparison = []
for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=cv, scoring="f1_macro", n_jobs=1)
    comparison.append({{"model": name, "cv_macro_f1": scores["test_score"].mean(), "cv_std": scores["test_score"].std()}})
comparison = pd.DataFrame(comparison).sort_values("cv_macro_f1", ascending=False).reset_index(drop=True)
display(comparison.round(4))
"""),
        markdown("## 5. Holdout evaluation"),
        code("""
best_name = comparison.iloc[0]["model"]
best_model = models[best_name].fit(X_train, y_train)
predictions = best_model.predict(X_test)
print(f"Selected model: {best_name}")
print(f"Holdout accuracy: {accuracy_score(y_test, predictions):.4f}")
print(f"Holdout macro F1: {f1_score(y_test, predictions, average='macro'):.4f}")
display(pd.DataFrame(classification_report(y_test, predictions, output_dict=True, zero_division=0)).T.round(4))
ConfusionMatrixDisplay.from_predictions(y_test, predictions, cmap="Blues", xticks_rotation=30)
plt.title(f"Confusion matrix — {best_name}")
plt.tight_layout()
plt.show()
"""),
        markdown("## 6. Model interpretation and sample predictions"),
        code("""
if best_name == "Logistic Regression":
    vectorizer = best_model.named_steps["tfidf"]
    classifier = best_model.named_steps["model"]
    terms = np.asarray(vectorizer.get_feature_names_out())
    rows = []
    coefficients = classifier.coef_ if len(classifier.classes_) > 2 else np.vstack([-classifier.coef_[0], classifier.coef_[0]])
    for class_name, weights in zip(classifier.classes_, coefficients):
        for term, weight in zip(terms[np.argsort(weights)[-8:]], np.sort(weights)[-8:]):
            rows.append({"class": class_name, "term": term, "weight": weight})
    display(pd.DataFrame(rows).sort_values(["class", "weight"], ascending=[True, False]).round(3))

sample = pd.DataFrame({"text": X_test.iloc[:8], "actual": y_test.iloc[:8], "predicted": predictions[:8]})
display(sample)
"""),
        markdown("## 7. Responsible-use notes and next steps\n\n- Replace deterministic demo text with versioned, licensed, representative data.\n- Review class definitions, annotation quality, subgroup performance, and threshold costs with domain experts.\n- Keep humans in the loop for hiring, moderation, security, healthcare, finance, and other consequential decisions.\n- Monitor vocabulary drift and abstain when confidence or data quality is low."),
    ]


def tabular_cells(cfg: dict, classification: bool) -> list[dict]:
    numeric = json.dumps(cfg["numeric"])
    categorical = json.dumps(cfg["categorical"], indent=2)
    task = "classification" if classification else "regression"
    generate_target = f"""
numeric_signal = sum((i + 1) * (data[name] - data[name].mean()) / (data[name].std() + 1e-9) for i, name in enumerate(NUMERIC_FEATURES))
category_signal = sum(data[name].astype("category").cat.codes * (0.25 + 0.10 * i) for i, name in enumerate(CATEGORICAL_FEATURES))
latent = numeric_signal + category_signal + rng.normal(0, 2.2, len(data))
data["{cfg['target']}"] = np.where(latent > np.quantile(latent, 0.60), "yes", "no")
""" if classification else f"""
numeric_signal = sum((i + 1) * (data[name] - data[name].mean()) / (data[name].std() + 1e-9) for i, name in enumerate(NUMERIC_FEATURES))
category_signal = sum(data[name].astype("category").cat.codes * (8 + 2 * i) for i, name in enumerate(CATEGORICAL_FEATURES))
nonlinear = 4.5 * np.sin(data[NUMERIC_FEATURES[0]] / (data[NUMERIC_FEATURES[0]].std() + 1e-9))
data["{cfg['target']}"] = 120 + 22 * numeric_signal + category_signal + nonlinear + rng.normal(0, 18, len(data))
data["{cfg['target']}"] = data["{cfg['target']}"].clip(lower=1)
"""
    if classification:
        modeling = """
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

X = data[NUMERIC_FEATURES + CATEGORICAL_FEATURES]
y = data[TARGET]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE, stratify=y)

numeric_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
categorical_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])
preprocessor = ColumnTransformer([("numeric", numeric_pipe, NUMERIC_FEATURES), ("categorical", categorical_pipe, CATEGORICAL_FEATURES)])
models = {
    "Majority baseline": DummyClassifier(strategy="prior"),
    "Logistic Regression": LogisticRegression(max_iter=2000, class_weight="balanced", random_state=RANDOM_STATE),
    "Random Forest": RandomForestClassifier(n_estimators=180, min_samples_leaf=3, class_weight="balanced", random_state=RANDOM_STATE, n_jobs=1),
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
comparison = []
for name, estimator in models.items():
    candidate = Pipeline([("preprocessor", preprocessor), ("model", estimator)])
    scores = cross_validate(candidate, X_train, y_train, cv=cv, scoring="f1_macro", n_jobs=1)
    comparison.append({"model": name, "cv_macro_f1": scores["test_score"].mean(), "cv_std": scores["test_score"].std()})
comparison = pd.DataFrame(comparison).sort_values("cv_macro_f1", ascending=False).reset_index(drop=True)
display(comparison.round(4))
"""
        evaluation = """
best_name = comparison.iloc[0]["model"]
best_pipeline = Pipeline([("preprocessor", preprocessor), ("model", models[best_name])]).fit(X_train, y_train)
predictions = best_pipeline.predict(X_test)
probabilities = best_pipeline.predict_proba(X_test)[:, list(best_pipeline.classes_).index("yes")]
print(f"Selected model: {best_name}")
print(f"Holdout accuracy: {accuracy_score(y_test, predictions):.4f}")
print(f"Holdout macro F1: {f1_score(y_test, predictions, average='macro'):.4f}")
print(f"Holdout ROC AUC: {roc_auc_score((y_test == 'yes').astype(int), probabilities):.4f}")
display(pd.DataFrame(classification_report(y_test, predictions, output_dict=True, zero_division=0)).T.round(4))
ConfusionMatrixDisplay.from_predictions(y_test, predictions, cmap="Blues")
plt.title(f"Confusion matrix — {best_name}")
plt.tight_layout()
plt.show()
"""
    else:
        modeling = """
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

X = data[NUMERIC_FEATURES + CATEGORICAL_FEATURES]
y = data[TARGET]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=RANDOM_STATE)

numeric_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
categorical_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])
preprocessor = ColumnTransformer([("numeric", numeric_pipe, NUMERIC_FEATURES), ("categorical", categorical_pipe, CATEGORICAL_FEATURES)])
models = {
    "Median baseline": DummyRegressor(strategy="median"),
    "Ridge Regression": Ridge(alpha=2.0),
    "Random Forest": RandomForestRegressor(n_estimators=180, min_samples_leaf=3, random_state=RANDOM_STATE, n_jobs=1),
}
cv = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
comparison = []
for name, estimator in models.items():
    candidate = Pipeline([("preprocessor", preprocessor), ("model", estimator)])
    scores = cross_validate(candidate, X_train, y_train, cv=cv, scoring="neg_mean_absolute_error", n_jobs=1)
    comparison.append({"model": name, "cv_mae": -scores["test_score"].mean(), "cv_std": scores["test_score"].std()})
comparison = pd.DataFrame(comparison).sort_values("cv_mae").reset_index(drop=True)
display(comparison.round(3))
"""
        evaluation = """
best_name = comparison.iloc[0]["model"]
best_pipeline = Pipeline([("preprocessor", preprocessor), ("model", models[best_name])]).fit(X_train, y_train)
predictions = best_pipeline.predict(X_test)
print(f"Selected model: {best_name}")
print(f"Holdout MAE: {mean_absolute_error(y_test, predictions):.3f}")
print(f"Holdout RMSE: {mean_squared_error(y_test, predictions) ** 0.5:.3f}")
print(f"Holdout R²: {r2_score(y_test, predictions):.4f}")
evaluation = pd.DataFrame({"actual": y_test.to_numpy(), "predicted": predictions})
display(evaluation.head(10).round(3))
sns.scatterplot(data=evaluation, x="actual", y="predicted", alpha=0.65)
limits = [evaluation.min().min(), evaluation.max().max()]
plt.plot(limits, limits, "--", color="black", label="Perfect prediction")
plt.title(f"Actual vs predicted — {best_name}")
plt.legend()
plt.tight_layout()
plt.show()
"""
    return [
        markdown(f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\nThis notebook uses a deterministic, domain-shaped demo dataset so the end-to-end {task} workflow is executable without private data. Reported metrics describe this demo only."),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Data contract and deterministic demo data"),
        code(f"""
NUMERIC_FEATURES = {numeric}
CATEGORICAL_VALUES = {categorical}
CATEGORICAL_FEATURES = list(CATEGORICAL_VALUES)
TARGET = "{cfg['target']}"
N_ROWS = 1400

data = pd.DataFrame()
for i, name in enumerate(NUMERIC_FEATURES):
    center = 25 + 18 * i
    spread = 6 + 3 * i
    values = rng.normal(center, spread, N_ROWS)
    data[name] = np.maximum(values, 0).round(3)
for name, values in CATEGORICAL_VALUES.items():
    data[name] = rng.choice(values, size=N_ROWS)
{generate_target}

for column in NUMERIC_FEATURES[:2]:
    missing_rows = rng.choice(data.index, size=18, replace=False)
    data.loc[missing_rows, column] = np.nan

print(f"Dataset shape: {{data.shape[0]:,}} rows × {{data.shape[1]}} columns")
display(data.head())
"""),
        markdown("## 3. Data quality and exploratory analysis"),
        code(f"""
overview = pd.DataFrame({{
    "dtype": data.dtypes.astype(str),
    "missing": data.isna().sum(),
    "missing_pct": (100 * data.isna().mean()).round(2),
    "unique": data.nunique(dropna=False),
}})
display(overview)
display(data[NUMERIC_FEATURES + [TARGET]].describe().T.round(3))
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(data=data, x=NUMERIC_FEATURES[0], kde=True, ax=axes[0], color="#2563eb")
sns.histplot(data=data, x=TARGET, ax=axes[1], color="#0f766e")
axes[0].set_title(f"Distribution of {{NUMERIC_FEATURES[0]}}")
axes[1].set_title("Target distribution")
plt.tight_layout()
plt.show()
"""),
        markdown("## 4. Leakage-safe preprocessing, baseline, and model comparison"),
        code(modeling),
        markdown("## 5. Holdout evaluation"),
        code(evaluation),
        markdown("## 6. Permutation importance and diagnostics"),
        code("""
from sklearn.inspection import permutation_importance

sample_size = min(500, len(X_test))
X_explain = X_test.sample(sample_size, random_state=RANDOM_STATE)
y_explain = y_test.loc[X_explain.index]
importance = permutation_importance(best_pipeline, X_explain, y_explain, n_repeats=5, random_state=RANDOM_STATE, n_jobs=1)
importance_df = pd.DataFrame({
    "feature": X_explain.columns,
    "importance_mean": importance.importances_mean,
    "importance_std": importance.importances_std,
}).sort_values("importance_mean", ascending=False)
display(importance_df.round(4))
sns.barplot(data=importance_df, x="importance_mean", y="feature", color="#2563eb")
plt.title("Permutation importance on the holdout sample")
plt.tight_layout()
plt.show()
"""),
        markdown("## 7. Limitations and next steps\n\n- Replace demo data with licensed, representative, versioned production data.\n- Review target definition, leakage risks, subgroup behavior, calibration, and domain error costs.\n- Add uncertainty estimates, drift monitoring, human-review policies, and retraining criteria before deployment.\n- Treat feature importance as model behavior—not causality."),
    ]


def forecast_cells(cfg: dict) -> list[dict]:
    energy = cfg["target"].startswith("energy")
    target_formula = (
        "180 + 3.2 * data['temperature_c'] + 22 * data['is_weekend'] + 16 * np.sin(2 * np.pi * data['day_of_year'] / 365)"
        if energy
        else "115 + 2.7 * data['promotion_pct'] - 18 * data['is_weekend'] + 24 * np.sin(2 * np.pi * data['day_of_year'] / 365)"
    )
    driver_generation = (
        "data['temperature_c'] = 24 + 9 * np.sin(2 * np.pi * data['day_of_year'] / 365) + rng.normal(0, 2.5, N_DAYS)"
        if energy
        else "data['promotion_pct'] = np.where(rng.random(N_DAYS) < 0.22, rng.choice([5, 10, 15, 20], N_DAYS), 0)"
    )
    return [
        markdown(f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\nThe notebook uses a deterministic demo series and chronological validation. Metrics are illustrative, not claims about a real retailer or utility."),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Build the time-indexed demo dataset"),
        code(f"""
N_DAYS = 900
data = pd.DataFrame({{"date": pd.date_range("2024-01-01", periods=N_DAYS, freq="D")}})
data["day_of_year"] = data["date"].dt.dayofyear
data["day_of_week"] = data["date"].dt.dayofweek
data["is_weekend"] = (data["day_of_week"] >= 5).astype(int)
{driver_generation}
data["{cfg['target']}"] = {target_formula} + rng.normal(0, 10, N_DAYS)
data["lag_1"] = data["{cfg['target']}"].shift(1)
data["lag_7"] = data["{cfg['target']}"].shift(7)
data["rolling_7"] = data["{cfg['target']}"].shift(1).rolling(7).mean()
data = data.dropna().reset_index(drop=True)
print(f"Series range: {{data['date'].min().date()}} to {{data['date'].max().date()}}")
print(f"Usable observations: {{len(data):,}}")
display(data.head())
"""),
        markdown("## 3. Time-series exploration"),
        code(f"""
display(data.describe(include="all").T.round(3))
plt.figure(figsize=(12, 4))
plt.plot(data["date"], data["{cfg['target']}"], color="#2563eb", linewidth=1)
plt.title("Target history")
plt.xlabel("Date")
plt.ylabel("{cfg['target']}")
plt.tight_layout()
plt.show()
"""),
        markdown("## 4. Chronological split and time-aware validation"),
        code(f"""
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

FEATURES = ["day_of_year", "day_of_week", "is_weekend", "{cfg['driver']}", "lag_1", "lag_7", "rolling_7"]
TARGET = "{cfg['target']}"
split_at = int(len(data) * 0.80)
train, test = data.iloc[:split_at], data.iloc[split_at:]
X_train, y_train = train[FEATURES], train[TARGET]
X_test, y_test = test[FEATURES], test[TARGET]

models = {{
    "Mean baseline": DummyRegressor(strategy="mean"),
    "Ridge Regression": Pipeline([("scale", StandardScaler()), ("model", Ridge(alpha=2.0))]),
    "Random Forest": RandomForestRegressor(n_estimators=180, min_samples_leaf=3, random_state=RANDOM_STATE, n_jobs=1),
}}
cv = TimeSeriesSplit(n_splits=5)
comparison = []
for name, model in models.items():
    scores = cross_validate(model, X_train, y_train, cv=cv, scoring="neg_mean_absolute_error", n_jobs=1)
    comparison.append({{"model": name, "cv_mae": -scores["test_score"].mean(), "cv_std": scores["test_score"].std()}})
comparison = pd.DataFrame(comparison).sort_values("cv_mae").reset_index(drop=True)
display(comparison.round(3))
"""),
        markdown("## 5. Holdout forecast and baseline comparison"),
        code("""
best_name = comparison.iloc[0]["model"]
best_model = models[best_name].fit(X_train, y_train)
predictions = best_model.predict(X_test)
naive = X_test["lag_7"].to_numpy()
results = pd.DataFrame({
    "model": ["Seasonal lag-7 baseline", best_name],
    "MAE": [mean_absolute_error(y_test, naive), mean_absolute_error(y_test, predictions)],
    "RMSE": [mean_squared_error(y_test, naive) ** 0.5, mean_squared_error(y_test, predictions) ** 0.5],
    "R2": [r2_score(y_test, naive), r2_score(y_test, predictions)],
})
display(results.round(3))

forecast = test[["date", TARGET]].copy()
forecast["prediction"] = predictions
plt.figure(figsize=(12, 4))
plt.plot(forecast["date"], forecast[TARGET], label="Actual")
plt.plot(forecast["date"], forecast["prediction"], label=best_name)
plt.title("Chronological holdout forecast")
plt.legend()
plt.tight_layout()
plt.show()
"""),
        markdown("## 6. Operational interpretation and next steps\n\n- Replace demo observations with a versioned real series and document missing dates, revisions, and outliers.\n- Compare against stronger seasonal baselines and use rolling-origin backtesting across several horizons.\n- Add forecast intervals, holiday/event features, drift alerts, and cost-weighted service metrics.\n- Never use random train/test splits for this time-ordered problem."),
    ]


def project_readme(cfg: dict, kind: str) -> str:
    method = {
        "text": "TF-IDF, Naive Bayes, and logistic regression",
        "classification": "logistic regression and random forests",
        "regression": "ridge regression and random forests",
        "forecast": "time-aware ridge and random-forest forecasting",
    }[kind]
    metric = "macro F1 and class-level diagnostics" if kind in {"text", "classification"} else "MAE, RMSE, and R²"
    slug = cfg["slug"] + ".ipynb"
    return f"""# {cfg['title']}

{cfg['summary']}

## Why this project matters

This is a portfolio-ready supervised-learning workflow built around a current business use case. It shows how to move from a documented data contract to a baseline, a validated model, honest holdout evaluation, and responsible interpretation.

## Problem framing

- **Learning type:** Supervised {kind.replace('_', ' ')}
- **Primary methods:** {method}
- **Evaluation:** {metric}
- **Decision boundary:** Predictions support prioritization and review; they do not replace domain judgment.

## Data

The notebook creates a deterministic, domain-shaped demonstration dataset locally. This keeps the project executable and avoids publishing private or questionably licensed data. The schema, target, caveats, and migration path to real data are documented in the notebook.

## Workflow

1. Reproducible environment and seed
2. Data contract and quality checks
3. Exploratory analysis
4. Leakage-safe or chronological split
5. Baseline and candidate-model comparison
6. Holdout metrics and diagnostics
7. Explainability or operational interpretation
8. Limitations, monitoring, and next steps

## Results

The notebook is committed with executed outputs. Open [{slug}]({slug}) to inspect the actual model comparison, plots, holdout metrics, diagnostics, and sample predictions generated from the reproducible demo data.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r ../requirements.txt
jupyter lab "{slug}"
```

Run cells from top to bottom. Use the recorded package versions and replace the demo data only after matching the documented schema.

## Technologies

- Python
- pandas and NumPy
- scikit-learn
- Matplotlib and Seaborn
- Jupyter Notebook

## Limitations and next steps

- Demo metrics are not production benchmarks.
- Validate on licensed, representative, time-appropriate data.
- Audit leakage, calibration, subgroup behavior, drift, and business error costs.
- Add human-review, monitoring, retraining, and rollback policies before deployment.

## Author

**Tajamul Khan**

[GitHub](https://github.com/tajamulkhann) · [LinkedIn](https://www.linkedin.com/in/tajamulkhann/) · Instagram: `@tajamul.codes`

{CONNECT}"""


def write_project(cfg: dict, kind: str, cells: list[dict]) -> None:
    folder = SUPERVISED / cfg["title"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{cfg['slug']}.ipynb").write_text(json.dumps(notebook(cells), indent=1) + "\n", encoding="utf-8")
    (folder / "README.md").write_text(project_readme(cfg, kind), encoding="utf-8")


KEPT = [
    "Airline Satisfaction Prediction using Classification Algorithms",
    "Airlines Delay Prediction using Classification Algorithms",
    "Banknote Authentication Using Classification Algorithms",
    "Breast Cancer Prediction using Classification Algorithms",
    "Chronic Kidney Disease Prediction Using Classifiation Algorithms",
    "Credit Score Prediction using Classification Algorithm",
    "Diabetes Prediction using Classification and Boosting Algorithm",
    "Diamond Price Prediction using Regressor Algorithms",
    "Drug Classification Using Classification Algorithms",
    "E-Commerce Shipping Prediction using Classification Algorithm",
    "Heart Disease Prediction using Classification Algorithms",
    "Hotel Reservation Booking Status Prediction using Classification Algorithm",
    "Kidney Stone Prediction using Classification Algorithm",
    "Laptop Price Prediction using Regression Algorithms",
    "Salary Prediction for Data Science Jobs using Regression Algorithms",
    "Stroke Prediction using Machine Learning Classification Algorithm",
    "Used Vehicle Price Prediction using Regression Algorithm",
    "Vehicle Insurance Claim Fraud Detection using Classification Algorithms",
]


REFURBISHED = [
    "Airbnb Stock Price Prediction",
    "Customer Churn Analysis using Classification Algorithms",
    "Customer Churn Analysis using Logistic Regression",
    "Customer Satisfaction Analysis using Classification Algorithms",
    "Housing Cost Prediction using Regression Algorithms",
    "IPL Winner Prediction using Classification Algorithms",
    "Insurance Premium Prediction using Regression Algorithms",
    "Loan Approval Prediction using Classification Algorithms",
    "Rain Prediction in Australia using Classification Algorithms",
    "Rainfall Amount Prediction using Regression Algorithms",
    "Telemarketing Campaign Response using Classification Algorithms",
]


def replace_connect_blocks() -> None:
    for readme in ROOT.rglob("*"):
        if not readme.is_file() or readme.name.lower() != "readme.md":
            continue
        text = readme.read_text(encoding="utf-8", errors="replace")
        marker_match = re.search(r"^## Let['’]?s Connect.*$", text, flags=re.MULTILINE)
        if marker_match:
            text = text[: marker_match.start()].rstrip() + "\n\n" + CONNECT
        else:
            text = text.rstrip() + "\n\n" + CONNECT
        readme.write_text(text, encoding="utf-8")


def build_index(all_new: list[dict]) -> None:
    rows = []
    for title in KEPT:
        rows.append((title, "Maintained", "Original data/notebook", "Existing executed output retained"))
    for title in REFURBISHED:
        rows.append((title, "Refurbished", "Committed data or reproducible demo", "Corrected workflow; output re-executed"))
    for cfg in all_new:
        rows.append((cfg["title"], "New", "Reproducible domain demo", "Executed output committed"))
    rows.sort(key=lambda item: item[0].lower())
    table = "\n".join(
        f"| [{title}]({title.replace(' ', '%20')}/) | {status} | {data} | {output} |"
        for title, status, data, output in rows
    )
    index = f"""# Supervised Machine Learning Projects

This collection contains **50 supervised-learning projects** spanning classification, regression, NLP, forecasting, healthcare, finance, operations, risk, and customer analytics.

The original collection was audited project by project:

- **18 maintained projects** kept their existing code and saved outputs.
- **11 refurbished projects** received targeted repairs for broken paths, duplicate work, missing data/docs, or incorrect problem framing.
- **21 new projects** add current, portfolio-ready use cases with reproducible data and executed outputs.

Read the [selective audit report](AUDIT.md) for the keep/refurbish decisions and project-level findings.

## Portfolio standards

- Saved notebook outputs remain visible for reviewers.
- Every project includes a baseline, validation strategy, holdout evaluation, and limitations.
- Time-series projects use chronological splits; classification projects report class-aware metrics.
- New demo datasets are deterministic and clearly identified—no synthetic result is presented as a real-world benchmark.
- Relative paths, reproducible seeds, dependency guidance, and the locked creator branding are preserved.

## Project index

| Project | Status | Data | Notebook evidence |
|---|---|---|---|
{table}

## Run the portfolio

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r "Supervised Learning Projects/requirements.txt"
```

Open any project notebook and run cells from top to bottom. Existing projects with external dataset links retain their recorded outputs; new projects run without external downloads.

## Author

**Tajamul Khan**

{CONNECT}"""
    (SUPERVISED / "README.md").write_text(index, encoding="utf-8")


def refresh_root_readme() -> None:
    intro = """# Machine Learning Projects

A practical portfolio of supervised and unsupervised machine-learning projects with notebooks, documentation, reproducible workflows, and visible execution evidence.

| Collection | Projects | Explore |
|---|---:|---|
| Supervised Learning | 50 | [Browse projects](Supervised%20Learning%20Projects/) |
| Unsupervised Learning | 5 | [Browse projects](Unsupervised%20Learning%20Projects/) |

<img width="1280" height="720" alt="Machine learning projects" src="https://github.com/user-attachments/assets/12905a9b-ac44-4115-8faa-473a666c9651" />

"""
    (ROOT / "README.md").write_text(intro + CONNECT, encoding="utf-8")


def main() -> None:
    all_new = TEXT_PROJECTS + CLASSIFICATION_PROJECTS + REGRESSION_PROJECTS + FORECAST_PROJECTS
    if len(all_new) != 21:
        raise RuntimeError(f"Expected 21 new projects, found {len(all_new)}")
    for cfg in TEXT_PROJECTS:
        write_project(cfg, "text", text_cells(cfg))
    for cfg in CLASSIFICATION_PROJECTS:
        write_project(cfg, "classification", tabular_cells(cfg, classification=True))
    for cfg in REGRESSION_PROJECTS:
        write_project(cfg, "regression", tabular_cells(cfg, classification=False))
    for cfg in FORECAST_PROJECTS:
        write_project(cfg, "forecast", forecast_cells(cfg))
    for cfg in REPAIRED_DEMO_PROJECTS["text"]:
        write_project(cfg, "text", text_cells(cfg))
    for cfg in REPAIRED_DEMO_PROJECTS["classification"]:
        write_project(cfg, "classification", tabular_cells(cfg, classification=True))
    for cfg in REPAIRED_DEMO_PROJECTS["regression"]:
        write_project(cfg, "regression", tabular_cells(cfg, classification=False))
    refresh_root_readme()
    replace_connect_blocks()
    build_index(all_new)
    print(f"Built {len(all_new)} new supervised-learning projects.")


if __name__ == "__main__":
    main()
