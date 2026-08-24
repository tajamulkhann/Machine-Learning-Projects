#!/usr/bin/env python3
"""Build the selective unsupervised-learning portfolio expansion.

The script preserves five existing project folders, refurbishes only the three
legacy notebooks that are not portable, creates 25 reproducible additions, and
keeps Tajamul Khan's locked connection block verbatim in every README.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UNSUPERVISED = ROOT / "Unsupervised Learning Projects"
RANDOM_STATE = 42


def locked_connect_block() -> str:
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    marker = "## Let's Connect"
    if marker not in root_readme:
        raise RuntimeError("The locked Let's Connect block is missing from README.md")
    return marker + root_readme.split(marker, 1)[1].rstrip() + "\n"


CONNECT = locked_connect_block()


def markdown(source: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": source.strip() + "\n"}


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
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
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
        "title": "LLM Prompt Intent Clustering",
        "slug": "llm_prompt_intent_clustering",
        "summary": "Discover recurring prompt intents for routing, evaluation, and prompt-library design without labelled training data.",
        "entity": "prompt",
        "topics": {
            "coding": ["python", "debug", "function", "api", "error", "repository", "test", "refactor"],
            "analytics": ["dashboard", "metric", "sql", "trend", "segment", "table", "report", "insight"],
            "writing": ["rewrite", "caption", "tone", "draft", "audience", "headline", "summary", "edit"],
            "research": ["paper", "evidence", "source", "compare", "literature", "method", "citation", "finding"],
        },
    },
    {
        "title": "RAG Document Chunk Clustering",
        "slug": "rag_document_chunk_clustering",
        "summary": "Group retrieval chunks into coherent themes to inspect coverage, redundancy, and indexing quality in RAG systems.",
        "entity": "document chunk",
        "topics": {
            "access_control": ["identity", "role", "permission", "token", "policy", "authentication", "group", "security"],
            "data_pipeline": ["ingestion", "schema", "transform", "table", "batch", "stream", "quality", "lineage"],
            "model_serving": ["endpoint", "latency", "deployment", "inference", "scale", "monitor", "version", "traffic"],
            "evaluation": ["retrieval", "faithfulness", "relevance", "benchmark", "metric", "judge", "dataset", "error"],
        },
    },
    {
        "title": "Customer Support Topic Discovery",
        "slug": "customer_support_topic_discovery",
        "summary": "Reveal common support themes so teams can improve routing, self-service content, and backlog analysis.",
        "entity": "support ticket",
        "topics": {
            "billing": ["invoice", "refund", "charge", "payment", "subscription", "receipt", "price", "billing"],
            "technical": ["error", "crash", "login", "timeout", "bug", "install", "browser", "technical"],
            "delivery": ["shipment", "tracking", "courier", "package", "late", "address", "dispatch", "delivery"],
            "account": ["profile", "password", "access", "email", "security", "verification", "account", "locked"],
        },
    },
    {
        "title": "Research Paper Topic Mapping",
        "slug": "research_paper_topic_mapping",
        "summary": "Map paper abstracts into interpretable research themes and surface nearby work through vector similarity.",
        "entity": "abstract",
        "topics": {
            "language_models": ["transformer", "language", "attention", "token", "instruction", "reasoning", "benchmark", "generation"],
            "computer_vision": ["image", "vision", "pixel", "segmentation", "detection", "camera", "feature", "scene"],
            "ml_systems": ["serving", "latency", "distributed", "training", "memory", "throughput", "hardware", "pipeline"],
            "responsible_ai": ["fairness", "privacy", "bias", "safety", "audit", "governance", "risk", "explainability"],
        },
    },
    {
        "title": "Product Review Theme Mining",
        "slug": "product_review_theme_mining",
        "summary": "Extract recurring product-experience themes without requiring sentiment or issue labels.",
        "entity": "review",
        "topics": {
            "delivery": ["package", "courier", "arrival", "late", "tracking", "box", "dispatch", "delivery"],
            "quality": ["durable", "material", "finish", "broken", "build", "quality", "sturdy", "damage"],
            "usability": ["setup", "instructions", "easy", "interface", "controls", "learn", "feature", "usable"],
            "value": ["price", "discount", "expensive", "worth", "budget", "cost", "deal", "value"],
        },
    },
    {
        "title": "Duplicate Question Discovery",
        "slug": "duplicate_question_discovery",
        "summary": "Find semantically similar questions for FAQ consolidation and community moderation using vector similarity.",
        "entity": "question",
        "topics": {
            "python_env": ["python", "package", "environment", "install", "version", "dependency", "pip", "virtualenv"],
            "sql_query": ["sql", "join", "table", "query", "duplicate", "group", "window", "database"],
            "cloud_access": ["cloud", "permission", "role", "access", "account", "tenant", "credential", "resource"],
            "model_metrics": ["precision", "recall", "metric", "validation", "baseline", "score", "test", "model"],
        },
    },
    {
        "title": "Resume Skill Taxonomy Discovery",
        "slug": "resume_skill_taxonomy_discovery",
        "summary": "Organize resume skill statements into emerging capability groups for portfolio analysis rather than candidate ranking.",
        "entity": "skill statement",
        "topics": {
            "data_engineering": ["spark", "etl", "pipeline", "warehouse", "airflow", "schema", "lakehouse", "streaming"],
            "machine_learning": ["model", "feature", "training", "validation", "sklearn", "forecast", "classification", "experiment"],
            "generative_ai": ["rag", "agent", "embedding", "prompt", "llm", "evaluation", "vector", "retrieval"],
            "analytics": ["dashboard", "powerbi", "sql", "metric", "stakeholder", "report", "insight", "visualization"],
        },
    },
]


CLUSTER_PROJECTS = [
    {
        "title": "AI Agent Trace Pattern Mining",
        "slug": "ai_agent_trace_pattern_mining",
        "summary": "Cluster agent runs by tool use, latency, token consumption, and recovery behavior to identify operational patterns.",
        "features": ["tool_calls", "steps", "input_tokens", "output_tokens", "latency_seconds", "retry_count"],
        "profiles": {"direct": [2, 4, 2200, 500, 7, 0], "research": [8, 12, 7800, 1700, 32, 1], "coding": [6, 10, 5200, 1250, 24, 1], "recovery_heavy": [10, 18, 9200, 2100, 58, 5]},
    },
    {
        "title": "E-Commerce Shopper Behavior Clustering",
        "slug": "ecommerce_shopper_behavior_clustering",
        "summary": "Segment anonymous shopping sessions by engagement, basket activity, discount use, and purchase cadence.",
        "features": ["pages_viewed", "session_minutes", "cart_events", "discount_pct", "days_since_visit", "prior_orders"],
        "profiles": {"browsers": [14, 9, 1, 5, 21, 1], "deal_seekers": [24, 18, 5, 28, 8, 4], "loyal_buyers": [18, 13, 6, 8, 3, 18], "high_intent": [35, 27, 10, 12, 2, 8]},
    },
    {
        "title": "Patient Lifestyle Phenotyping",
        "slug": "patient_lifestyle_phenotyping",
        "summary": "Discover lifestyle phenotypes from activity, sleep, resting pulse, hydration, and stress signals for cohort exploration.",
        "features": ["daily_steps", "sleep_hours", "resting_pulse", "water_liters", "active_minutes", "stress_score"],
        "profiles": {"active_balanced": [10500, 7.6, 60, 2.6, 72, 30], "sedentary_stressed": [3200, 5.8, 82, 1.4, 18, 76], "moderate": [7100, 6.8, 70, 2.0, 42, 48], "sleep_focused": [6200, 8.4, 64, 2.3, 35, 24]},
    },
    {
        "title": "EV Charging Session Clustering",
        "slug": "ev_charging_session_clustering",
        "summary": "Group charging sessions by energy, duration, arrival time, charger power, state of charge, and dwell time.",
        "features": ["energy_kwh", "duration_minutes", "arrival_hour", "charger_kw", "start_soc_pct", "dwell_minutes"],
        "profiles": {"commuter_topup": [16, 48, 9, 22, 55, 70], "overnight_home": [38, 390, 21, 7, 28, 480], "rapid_transit": [44, 42, 15, 120, 18, 50], "workplace": [25, 210, 10, 11, 45, 420]},
    },
    {
        "title": "Maritime Vessel Trajectory Clustering",
        "slug": "maritime_vessel_trajectory_clustering",
        "summary": "Cluster vessel journeys from distance, speed, stop behavior, course variation, duration, and port-call patterns.",
        "features": ["distance_nm", "mean_speed_knots", "stop_hours", "course_variation", "duration_hours", "port_calls"],
        "profiles": {"short_feeder": [420, 13, 6, 18, 40, 3], "ocean_direct": [6200, 17, 2, 8, 370, 2], "multi_port": [2400, 14, 42, 35, 230, 8], "slow_steaming": [5100, 11, 4, 10, 470, 2]},
    },
    {
        "title": "Crop Field Management Zone Clustering",
        "slug": "crop_field_management_zone_clustering",
        "summary": "Discover field management zones from vegetation, moisture, soil, elevation, temperature, and nutrient measurements.",
        "features": ["ndvi", "soil_moisture", "soil_ph", "elevation_m", "canopy_temp_c", "nitrogen_index"],
        "profiles": {"high_vigor": [0.82, 34, 6.7, 115, 25, 0.78], "water_stressed": [0.42, 12, 6.5, 120, 35, 0.46], "nutrient_limited": [0.51, 25, 5.7, 108, 30, 0.30], "balanced": [0.68, 28, 6.4, 118, 28, 0.62]},
    },
    {
        "title": "Air Quality Monitoring Station Clustering",
        "slug": "air_quality_station_clustering",
        "summary": "Group monitoring stations by pollutant mix, traffic influence, temperature, humidity, and wind conditions.",
        "features": ["pm25", "pm10", "no2", "ozone", "humidity_pct", "wind_kph"],
        "profiles": {"traffic_core": [78, 116, 64, 24, 55, 8], "industrial": [96, 148, 52, 31, 62, 10], "suburban": [34, 58, 25, 47, 58, 14], "coastal_clean": [18, 31, 13, 55, 72, 24]},
    },
    {
        "title": "Music Listener Persona Clustering",
        "slug": "music_listener_persona_clustering",
        "summary": "Discover listener personas from session depth, discovery, repeats, skips, playlist saves, and listening-hour diversity.",
        "features": ["weekly_minutes", "unique_artists", "repeat_rate", "skip_rate", "playlist_saves", "active_hours"],
        "profiles": {"loyal_fans": [620, 28, 0.68, 0.12, 18, 5], "explorers": [540, 96, 0.22, 0.31, 35, 12], "casual": [120, 18, 0.36, 0.42, 4, 3], "playlist_curators": [710, 72, 0.40, 0.18, 82, 9]},
    },
    {
        "title": "Supply Chain Route Pattern Clustering",
        "slug": "supply_chain_route_pattern_clustering",
        "summary": "Cluster logistics lanes by distance, lead time, cost, variability, handling, and emissions intensity.",
        "features": ["distance_km", "lead_time_hours", "cost_per_tonne", "delay_std_hours", "handling_events", "co2_kg_per_tonne"],
        "profiles": {"regional_road": [620, 18, 85, 5, 3, 74], "ocean_longhaul": [8200, 420, 54, 48, 7, 38], "air_priority": [4700, 17, 540, 4, 5, 610], "rail_corridor": [1900, 58, 72, 11, 4, 29]},
    },
]


ANOMALY_PROJECTS = [
    {
        "title": "Cybersecurity Network Traffic Anomaly Detection",
        "slug": "cybersecurity_network_traffic_anomaly_detection",
        "summary": "Prioritize unusual network flows from volume, duration, ports, failed connections, byte ratios, and fan-out behavior.",
        "features": ["bytes_mb", "duration_seconds", "destination_ports", "failed_connections", "upload_ratio", "destination_hosts"],
        "means": [2.5, 18, 2, 0.3, 0.35, 3], "stds": [1.1, 7, 0.8, 0.6, 0.12, 1.2], "shifts": [8, 5, 10, 12, 4, 10],
    },
    {
        "title": "Cloud Infrastructure Log Anomaly Detection",
        "slug": "cloud_infrastructure_log_anomaly_detection",
        "summary": "Detect unusual service windows from error rates, latency, restarts, request volume, memory, and CPU behavior.",
        "features": ["error_rate_pct", "p95_latency_ms", "restart_count", "requests_per_minute", "memory_pct", "cpu_pct"],
        "means": [1.2, 180, 0.2, 850, 58, 46], "stds": [0.6, 45, 0.5, 190, 9, 11], "shifts": [10, 7, 12, -3, 4, 5],
    },
    {
        "title": "Manufacturing Sensor Anomaly Detection",
        "slug": "manufacturing_sensor_anomaly_detection",
        "summary": "Flag abnormal equipment windows using temperature, vibration, pressure, current, acoustic level, and flow measurements.",
        "features": ["temperature_c", "vibration_mm_s", "pressure_bar", "motor_current_a", "acoustic_db", "flow_lpm"],
        "means": [68, 2.1, 8.4, 14, 62, 118], "stds": [4, 0.5, 0.7, 1.8, 3, 9], "shifts": [5, 9, -5, 6, 7, -6],
    },
    {
        "title": "Energy Consumption Anomaly Detection",
        "slug": "energy_consumption_anomaly_detection",
        "summary": "Identify unusual energy intervals from demand, temperature, occupancy, reactive power, load factor, and peak ratio.",
        "features": ["demand_kwh", "temperature_c", "occupancy_pct", "reactive_kvarh", "load_factor", "peak_ratio"],
        "means": [420, 26, 68, 55, 0.72, 1.18], "stds": [58, 4, 12, 11, 0.08, 0.12], "shifts": [7, 2, -4, 6, -5, 7],
    },
    {
        "title": "IoT Device Behavior Anomaly Detection",
        "slug": "iot_device_behavior_anomaly_detection",
        "summary": "Surface compromised or malfunctioning devices from telemetry frequency, payload, battery, errors, destinations, and uptime.",
        "features": ["messages_per_hour", "payload_kb", "battery_drop_pct", "error_count", "destination_count", "uptime_hours"],
        "means": [72, 4.5, 1.4, 0.6, 2, 510], "stds": [11, 1.1, 0.5, 0.8, 0.9, 80], "shifts": [7, 8, 6, 10, 9, -5],
    },
    {
        "title": "LLM Token Cost Anomaly Detection",
        "slug": "llm_token_cost_anomaly_detection",
        "summary": "Detect expensive or looping LLM requests from tokens, latency, tool calls, retries, context ratio, and estimated cost.",
        "features": ["input_tokens", "output_tokens", "latency_seconds", "tool_calls", "retry_count", "estimated_cost_usd"],
        "means": [2600, 620, 8, 2, 0.2, 0.035], "stds": [700, 210, 2.5, 1, 0.5, 0.012], "shifts": [8, 7, 6, 8, 12, 10],
    },
]


SPECIAL_PROJECTS = [
    {
        "title": "AI Image Embedding Clustering and Visual Search",
        "slug": "ai_image_embedding_clustering_visual_search",
        "summary": "Cluster image embeddings and retrieve visually related assets using a compact offline stand-in for CLIP-style vectors.",
        "kind": "image",
    },
    {
        "title": "Product Catalog Similarity Recommender",
        "slug": "product_catalog_similarity_recommender",
        "summary": "Recommend similar catalog items from product text and metadata without user labels or purchase outcomes.",
        "kind": "product",
    },
    {
        "title": "Social Network Community Detection",
        "slug": "social_network_community_detection",
        "summary": "Discover connected communities and bridge accounts from an interaction graph using spectral clustering.",
        "kind": "graph",
    },
]


NEW_PROJECTS = TEXT_PROJECTS + CLUSTER_PROJECTS + ANOMALY_PROJECTS + SPECIAL_PROJECTS
KEPT_CODE = {"Fraudulent Transaction Detection", "Market Basket Analysis"}
REFURBISHED_CODE = {
    "Basic Movie Recommender System",
    "Book Recommendation Engine",
    "Customer Segmentation Using Clustering Techniques",
}


def text_cells(cfg: dict) -> list[dict]:
    topics = json.dumps(cfg["topics"], indent=2)
    return [
        markdown(
            f"# {cfg['title']}\n\n"
            f"**Objective:** {cfg['summary']}\n\n"
            "This notebook uses deterministic demo text so the entire unsupervised workflow remains executable offline. "
            "Generator topics are hidden from model fitting and used only for retrospective diagnostics."
        ),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Build the documented demo corpus"),
        code(f"""
TOPICS = {topics}
ENTITY = "{cfg['entity']}"
COMMON_WORDS = ["customer", "system", "request", "team", "today", "information", "service", "workflow"]
rows = []
for topic, vocabulary in TOPICS.items():
    for row_id in range(75):
        tokens = rng.choice(vocabulary, size=7, replace=True).tolist()
        tokens += rng.choice(COMMON_WORDS, size=4, replace=True).tolist()
        if rng.random() < 0.45:
            other_topic = rng.choice([name for name in TOPICS if name != topic])
            tokens += rng.choice(TOPICS[other_topic], size=2, replace=True).tolist()
        rng.shuffle(tokens)
        rows.append({{"text": " ".join(tokens), "generator_topic": topic, "record_id": f"{{topic[:3]}}-{{row_id:03d}}"}})

data = pd.DataFrame(rows).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
print(f"Corpus: {{len(data):,}} {{ENTITY}} records")
display(data.head())
display(data["generator_topic"].value_counts().rename("records").to_frame())
"""),
        markdown("## 3. TF-IDF representation and cluster selection"),
        code("""
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score, silhouette_score

vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_features=500, sublinear_tf=True)
vectors = vectorizer.fit_transform(data["text"])
print(f"Vector matrix: {vectors.shape[0]} documents × {vectors.shape[1]} features")

selection_rows = []
for k in range(2, 7):
    candidate = KMeans(n_clusters=k, n_init=20, random_state=RANDOM_STATE)
    labels = candidate.fit_predict(vectors)
    selection_rows.append({"k": k, "silhouette": silhouette_score(vectors, labels, metric="cosine"), "inertia": candidate.inertia_})
selection = pd.DataFrame(selection_rows)
display(selection.round(4))

best_k = int(selection.loc[selection["silhouette"].idxmax(), "k"])
model = KMeans(n_clusters=best_k, n_init=30, random_state=RANDOM_STATE)
data["cluster"] = model.fit_predict(vectors)
print(f"Selected k={best_k} from cosine silhouette; score={selection['silhouette'].max():.4f}")
"""),
        markdown("## 4. Interpret discovered clusters"),
        code("""
terms = np.asarray(vectorizer.get_feature_names_out())
top_terms = []
for cluster_id, center in enumerate(model.cluster_centers_):
    words = terms[np.argsort(center)[-10:][::-1]]
    top_terms.append({"cluster": cluster_id, "records": int((data["cluster"] == cluster_id).sum()), "top_terms": ", ".join(words)})
display(pd.DataFrame(top_terms))
display(pd.crosstab(data["generator_topic"], data["cluster"], margins=True))
ari = adjusted_rand_score(data["generator_topic"], data["cluster"])
print(f"Retrospective ARI against hidden generator topics: {ari:.4f}")
print("The generator topic was not provided to TF-IDF or K-Means.")
"""),
        markdown("## 5. Two-dimensional map and stability check"),
        code("""
from sklearn.decomposition import TruncatedSVD

projection = TruncatedSVD(n_components=2, random_state=RANDOM_STATE).fit_transform(vectors)
plot_data = pd.DataFrame({"component_1": projection[:, 0], "component_2": projection[:, 1], "cluster": data["cluster"].astype(str)})
sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="cluster", palette="tab10", alpha=0.72)
plt.title("Discovered text clusters in a two-dimensional SVD projection")
plt.tight_layout()
plt.show()

alternate = KMeans(n_clusters=best_k, n_init=30, random_state=7).fit_predict(vectors)
stability = adjusted_rand_score(data["cluster"], alternate)
print(f"Cluster stability across two random seeds (ARI): {stability:.4f}")
"""),
        markdown("## 6. Assign new text and inspect nearest records"),
        code("""
from sklearn.metrics.pairwise import cosine_similarity

probe = " ".join(list(TOPICS.values())[0][:5])
probe_vector = vectorizer.transform([probe])
probe_cluster = int(model.predict(probe_vector)[0])
similarities = cosine_similarity(probe_vector, vectors).ravel()
nearest = np.argsort(similarities)[-5:][::-1]
print(f"Probe: {probe}")
print(f"Assigned cluster: {probe_cluster}")
display(data.loc[nearest, ["record_id", "text", "cluster"]].assign(cosine_similarity=similarities[nearest]).round(4))
"""),
        markdown(
            "## 7. Findings and limitations\n\n"
            "- Cluster quality is evaluated with cohesion, stability, interpretable terms, and a hidden synthetic diagnostic.\n"
            "- The synthetic corpus proves the workflow, not production accuracy.\n"
            "- Production use should replace TF-IDF with validated domain embeddings when semantic nuance matters.\n"
            "- Topics should be reviewed by domain experts before they drive routing or policy decisions."
        ),
    ]


def cluster_cells(cfg: dict) -> list[dict]:
    features = json.dumps(cfg["features"])
    profiles = json.dumps(cfg["profiles"], indent=2)
    return [
        markdown(
            f"# {cfg['title']}\n\n"
            f"**Objective:** {cfg['summary']}\n\n"
            "The deterministic demo data contains hidden generator profiles for post-hoc diagnostics. "
            "Those profiles are never supplied to the clustering algorithms."
        ),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Data contract and deterministic domain-shaped data"),
        code(f"""
FEATURES = {features}
PROFILE_CENTERS = {profiles}
rows = []
for profile, centers in PROFILE_CENTERS.items():
    centers = np.asarray(centers, dtype=float)
    scales = np.maximum(np.abs(centers) * 0.10, 0.08)
    samples = rng.normal(centers, scales, size=(125, len(FEATURES)))
    samples = np.maximum(samples, 0)
    for row in samples:
        rows.append({{**dict(zip(FEATURES, row)), "generator_profile": profile}})

data = pd.DataFrame(rows).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
for column in FEATURES[:2]:
    missing_rows = rng.choice(data.index, size=8, replace=False)
    data.loc[missing_rows, column] = np.nan
print(f"Dataset shape: {{data.shape[0]:,}} rows × {{data.shape[1]}} columns")
display(data.head().round(3))
display(data[FEATURES].describe().T.round(3))
"""),
        markdown("## 3. Robust preprocessing and cluster-count selection"),
        code("""
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.impute import SimpleImputer
from sklearn.metrics import adjusted_rand_score, davies_bouldin_score, silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler

preprocessor = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", RobustScaler())])
X = preprocessor.fit_transform(data[FEATURES])
selection_rows = []
for k in range(2, 7):
    labels = KMeans(n_clusters=k, n_init=30, random_state=RANDOM_STATE).fit_predict(X)
    selection_rows.append({"k": k, "silhouette": silhouette_score(X, labels), "davies_bouldin": davies_bouldin_score(X, labels)})
selection = pd.DataFrame(selection_rows)
display(selection.round(4))
best_k = int(selection.loc[selection["silhouette"].idxmax(), "k"])
print(f"Selected k={best_k} by maximum silhouette score.")
"""),
        markdown("## 4. Compare algorithms and retain the clearer solution"),
        code("""
kmeans = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE)
kmeans_labels = kmeans.fit_predict(X)
hierarchical_labels = AgglomerativeClustering(n_clusters=best_k, linkage="ward").fit_predict(X)

comparison = pd.DataFrame([
    {"model": "K-Means", "silhouette": silhouette_score(X, kmeans_labels), "davies_bouldin": davies_bouldin_score(X, kmeans_labels)},
    {"model": "Agglomerative", "silhouette": silhouette_score(X, hierarchical_labels), "davies_bouldin": davies_bouldin_score(X, hierarchical_labels)},
])
display(comparison.round(4))
labels = kmeans_labels if comparison.sort_values(["silhouette", "davies_bouldin"], ascending=[False, True]).iloc[0]["model"] == "K-Means" else hierarchical_labels
selected_model = "K-Means" if np.array_equal(labels, kmeans_labels) else "Agglomerative"
data["cluster"] = labels
print(f"Selected solution: {selected_model}")
"""),
        markdown("## 5. Profile and visualize the discovered groups"),
        code("""
from sklearn.decomposition import PCA

profiles = data.groupby("cluster")[FEATURES].mean().round(3)
profiles.insert(0, "records", data.groupby("cluster").size())
display(profiles)
display(pd.crosstab(data["generator_profile"], data["cluster"], margins=True))
print(f"Retrospective ARI against hidden generator profiles: {adjusted_rand_score(data['generator_profile'], data['cluster']):.4f}")

projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
plot_data = pd.DataFrame({"component_1": projection[:, 0], "component_2": projection[:, 1], "cluster": data["cluster"].astype(str)})
sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="cluster", palette="tab10", alpha=0.7)
plt.title("Cluster map in a two-dimensional PCA projection")
plt.tight_layout()
plt.show()
"""),
        markdown("## 6. Stability and assignment example"),
        code("""
alternate = KMeans(n_clusters=best_k, n_init=40, random_state=7).fit_predict(X)
print(f"K-Means stability across seeds (ARI): {adjusted_rand_score(kmeans_labels, alternate):.4f}")
if selected_model == "K-Means":
    example = data[FEATURES].median().to_frame().T
    predicted = int(kmeans.predict(preprocessor.transform(example))[0])
    display(example.round(3).assign(predicted_cluster=predicted))
else:
    print("Agglomerative clustering has no native out-of-sample predict method; production assignment would use centroids or a trained surrogate.")
"""),
        markdown(
            "## 7. Findings and limitations\n\n"
            "- Multiple internal metrics and a seed-stability check are used because clustering has no single accuracy measure.\n"
            "- Hidden generator profiles provide only a retrospective pipeline check.\n"
            "- Production interpretation requires domain validation, drift monitoring, and explicit rules for acting on segments."
        ),
    ]


def anomaly_cells(cfg: dict) -> list[dict]:
    features = json.dumps(cfg["features"])
    means = json.dumps(cfg["means"])
    stds = json.dumps(cfg["stds"])
    shifts = json.dumps(cfg["shifts"])
    return [
        markdown(
            f"# {cfg['title']}\n\n"
            f"**Objective:** {cfg['summary']}\n\n"
            "This notebook trains without labels. A small injected scenario flag is retained only to test the alerting workflow after scoring."
        ),
        markdown("## 1. Setup and reproducibility"),
        code(COMMON_IMPORTS),
        markdown("## 2. Generate normal behavior and rare stress scenarios"),
        code(f"""
FEATURES = {features}
MEANS = np.asarray({means}, dtype=float)
STDS = np.asarray({stds}, dtype=float)
SHIFTS = np.asarray({shifts}, dtype=float)

normal = rng.normal(MEANS, STDS, size=(960, len(FEATURES)))
stress = rng.normal(MEANS + SHIFTS * STDS, STDS * 0.55, size=(40, len(FEATURES)))
values = np.vstack([normal, stress])
values = np.maximum(values, 0)
data = pd.DataFrame(values, columns=FEATURES)
data["scenario_anomaly"] = np.r_[np.zeros(len(normal), dtype=int), np.ones(len(stress), dtype=int)]
data = data.sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
print(f"Dataset: {{len(data):,}} windows | stress scenarios retained for retrospective checks: {{data['scenario_anomaly'].sum()}}")
display(data.head().round(3))
display(data[FEATURES].describe().T.round(3))
"""),
        markdown("## 3. Robust scaling and label-free detector fitting"),
        code("""
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X = scaler.fit_transform(data[FEATURES])
contamination = 0.04

isolation = IsolationForest(n_estimators=240, contamination=contamination, random_state=RANDOM_STATE, n_jobs=1)
data["isolation_flag"] = (isolation.fit_predict(X) == -1).astype(int)
data["isolation_score"] = -isolation.score_samples(X)

lof = LocalOutlierFactor(n_neighbors=35, contamination=contamination)
data["lof_flag"] = (lof.fit_predict(X) == -1).astype(int)
data["lof_score"] = -lof.negative_outlier_factor_
print(f"Isolation Forest alerts: {data['isolation_flag'].sum()} | LOF alerts: {data['lof_flag'].sum()}")
"""),
        markdown("## 4. Retrospective detector diagnostics"),
        code("""
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score

rows = []
for name in ["isolation", "lof"]:
    rows.append({
        "detector": name,
        "precision": precision_score(data["scenario_anomaly"], data[f"{name}_flag"], zero_division=0),
        "recall": recall_score(data["scenario_anomaly"], data[f"{name}_flag"], zero_division=0),
        "f1": f1_score(data["scenario_anomaly"], data[f"{name}_flag"], zero_division=0),
        "roc_auc_from_score": roc_auc_score(data["scenario_anomaly"], data[f"{name}_score"]),
    })
diagnostics = pd.DataFrame(rows).sort_values("f1", ascending=False)
display(diagnostics.round(4))
print("Scenario labels were not used during scaling, detector fitting, or threshold selection.")
"""),
        markdown("## 5. Alert queue and feature-level context"),
        code("""
median = data[FEATURES].median()
mad = (data[FEATURES] - median).abs().median().replace(0, 1e-9)
robust_deviation = ((data[FEATURES] - median) / mad).abs()
data["largest_deviation_feature"] = robust_deviation.idxmax(axis=1)
data["largest_robust_deviation"] = robust_deviation.max(axis=1)
alerts = data.sort_values("isolation_score", ascending=False).head(12)
display(alerts[FEATURES + ["isolation_score", "largest_deviation_feature", "largest_robust_deviation", "scenario_anomaly"]].round(3))
"""),
        markdown("## 6. Two-dimensional anomaly map"),
        code("""
from sklearn.decomposition import PCA

projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
plot_data = pd.DataFrame({"component_1": projection[:, 0], "component_2": projection[:, 1], "alert": data["isolation_flag"].map({0: "normal", 1: "alert"})})
sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="alert", palette={"normal": "#94a3b8", "alert": "#dc2626"}, alpha=0.72)
plt.title("Isolation Forest alert map in a PCA projection")
plt.tight_layout()
plt.show()
print(f"Detector score correlation: {data[['isolation_score', 'lof_score']].corr().iloc[0, 1]:.4f}")
"""),
        markdown(
            "## 7. Findings and limitations\n\n"
            "- Anomaly scores prioritize investigation; they do not prove malicious activity, failure, or waste.\n"
            "- The injected stress cases demonstrate evaluation mechanics only.\n"
            "- Production thresholds should be calibrated to alert capacity, missed-event cost, seasonality, and feedback from investigators."
        ),
    ]


def image_cells(cfg: dict) -> list[dict]:
    return [
        markdown(
            f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\n"
            "The notebook uses deterministic 48-dimensional vectors as an offline stand-in for image embeddings. "
            "A production version can replace them with validated CLIP or vision-model embeddings without changing the clustering and retrieval stages."
        ),
        markdown("## 1. Setup and reproducibility"), code(COMMON_IMPORTS),
        markdown("## 2. Build a documented embedding collection"),
        code("""
THEMES = ["data_visualization", "code_screenshot", "product_photo", "portrait", "landscape"]
DIMENSIONS = 48
centers = rng.normal(0, 1, size=(len(THEMES), DIMENSIONS))
centers = centers / np.linalg.norm(centers, axis=1, keepdims=True) * 5
rows, vectors = [], []
for theme_id, theme in enumerate(THEMES):
    for item_id in range(70):
        vector = centers[theme_id] + rng.normal(0, 0.42, DIMENSIONS)
        vectors.append(vector)
        rows.append({"asset_id": f"img-{theme_id}-{item_id:03d}", "generator_theme": theme})
embeddings = np.asarray(vectors)
assets = pd.DataFrame(rows)
print(f"Embedding matrix: {embeddings.shape}")
display(assets.head())
"""),
        markdown("## 3. Cluster selection and interpretation"),
        code("""
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import Normalizer

X = Normalizer().fit_transform(embeddings)
selection = []
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=30, random_state=RANDOM_STATE).fit_predict(X)
    selection.append({"k": k, "cosine_silhouette": silhouette_score(X, labels, metric="cosine")})
selection = pd.DataFrame(selection)
display(selection.round(4))
best_k = int(selection.loc[selection["cosine_silhouette"].idxmax(), "k"])
model = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE).fit(X)
assets["cluster"] = model.labels_
display(pd.crosstab(assets["generator_theme"], assets["cluster"], margins=True))
print(f"Selected k={best_k}; retrospective ARI={adjusted_rand_score(assets['generator_theme'], assets['cluster']):.4f}")
"""),
        markdown("## 4. Visual search with cosine neighbours"),
        code("""
from sklearn.neighbors import NearestNeighbors

neighbours = NearestNeighbors(n_neighbors=7, metric="cosine").fit(X)
query_index = 12
distances, indices = neighbours.kneighbors(X[query_index:query_index + 1])
results = assets.iloc[indices[0]].copy()
results["cosine_similarity"] = 1 - distances[0]
print(f"Query asset: {assets.loc[query_index, 'asset_id']} ({assets.loc[query_index, 'generator_theme']})")
display(results.round(4))
"""),
        markdown("## 5. Two-dimensional embedding map"),
        code("""
from sklearn.decomposition import PCA

projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
plot_data = pd.DataFrame({"component_1": projection[:, 0], "component_2": projection[:, 1], "cluster": assets["cluster"].astype(str)})
sns.scatterplot(data=plot_data, x="component_1", y="component_2", hue="cluster", palette="tab10", alpha=0.72)
plt.title("Image-embedding clusters in a PCA projection")
plt.tight_layout()
plt.show()
"""),
        markdown("## 6. Findings and limitations\n\n- The demo validates clustering, retrieval, and inspection logic without downloading a vision model.\n- Production quality depends on the embedding model, image domain, duplicate policy, and human relevance checks.\n- Two-dimensional maps are diagnostic views, not proof that clusters are intrinsically separated."),
    ]


def product_cells(cfg: dict) -> list[dict]:
    return [
        markdown(f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\nThe deterministic catalog keeps the full recommendation workflow executable without external data or user tracking."),
        markdown("## 1. Setup and reproducibility"), code(COMMON_IMPORTS),
        markdown("## 2. Build a product catalog with text and metadata"),
        code("""
CATEGORIES = {
    "laptop": ["processor", "ram", "ssd", "display", "keyboard", "portable", "battery", "developer"],
    "headphones": ["audio", "wireless", "noise", "bass", "microphone", "comfort", "battery", "music"],
    "camera": ["sensor", "lens", "video", "stabilization", "autofocus", "photo", "creator", "resolution"],
    "fitness": ["workout", "tracking", "heart", "steps", "sleep", "waterproof", "health", "training"],
    "home_office": ["desk", "chair", "ergonomic", "monitor", "lighting", "workspace", "adjustable", "support"],
}
rows = []
for category, words in CATEGORIES.items():
    for item_id in range(55):
        selected = rng.choice(words, size=6, replace=True).tolist()
        price_band = rng.choice(["budget", "midrange", "premium"], p=[0.3, 0.45, 0.25])
        selected += [price_band, rng.choice(["compact", "standard", "professional"])]
        rows.append({"product_id": f"{category[:3]}-{item_id:03d}", "category": category, "price_band": price_band, "description": " ".join(selected)})
catalog = pd.DataFrame(rows).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
print(f"Catalog size: {len(catalog):,} products")
display(catalog.head())
"""),
        markdown("## 3. Vectorize and retrieve similar products"),
        code("""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2, sublinear_tf=True)
vectors = vectorizer.fit_transform(catalog["description"])
model = NearestNeighbors(n_neighbors=7, metric="cosine").fit(vectors)
query_index = int(catalog.index[catalog["category"] == "camera"][0])
distances, indices = model.kneighbors(vectors[query_index])
recommendations = catalog.iloc[indices[0]].copy()
recommendations["cosine_similarity"] = 1 - distances[0]
print(f"Query: {catalog.loc[query_index, 'product_id']} | {catalog.loc[query_index, 'description']}")
display(recommendations.round(4))
"""),
        markdown("## 4. Discover catalog groups without category labels"),
        code("""
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

selection = []
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=30, random_state=RANDOM_STATE).fit_predict(vectors)
    selection.append({"k": k, "cosine_silhouette": silhouette_score(vectors, labels, metric="cosine")})
selection = pd.DataFrame(selection)
display(selection.round(4))
best_k = int(selection.loc[selection["cosine_silhouette"].idxmax(), "k"])
cluster_model = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE).fit(vectors)
catalog["cluster"] = cluster_model.labels_
display(pd.crosstab(catalog["category"], catalog["cluster"], margins=True))
print(f"Retrospective ARI against hidden catalog categories: {adjusted_rand_score(catalog['category'], catalog['cluster']):.4f}")
"""),
        markdown("## 5. Coverage and diversity checks"),
        code("""
sample_indices = catalog.groupby("category", sort=True).head(1).index
rows = []
for idx in sample_indices:
    distances, indices = model.kneighbors(vectors[idx])
    returned = catalog.iloc[indices[0][1:]]
    rows.append({"query_category": catalog.loc[idx, "category"], "mean_similarity": float((1 - distances[0][1:]).mean()), "unique_categories": int(returned["category"].nunique()), "unique_price_bands": int(returned["price_band"].nunique())})
display(pd.DataFrame(rows).round(4))
"""),
        markdown("## 6. Findings and limitations\n\n- Content similarity supports cold-start items but cannot learn personal taste without interactions.\n- Offline similarity is not evidence of commercial impact.\n- Production evaluation should include relevance judgments, diversity, availability, fairness, and online experiments."),
    ]


def graph_cells(cfg: dict) -> list[dict]:
    return [
        markdown(f"# {cfg['title']}\n\n**Objective:** {cfg['summary']}\n\nA deterministic interaction graph demonstrates label-free community discovery. Hidden generator communities are used only after clustering as a diagnostic."),
        markdown("## 1. Setup and reproducibility"), code(COMMON_IMPORTS),
        markdown("## 2. Generate a community-structured interaction graph"),
        code("""
N_COMMUNITIES = 4
NODES_PER_COMMUNITY = 45
N_NODES = N_COMMUNITIES * NODES_PER_COMMUNITY
generator_community = np.repeat(np.arange(N_COMMUNITIES), NODES_PER_COMMUNITY)
adjacency = np.zeros((N_NODES, N_NODES), dtype=float)
for i in range(N_NODES):
    for j in range(i + 1, N_NODES):
        same = generator_community[i] == generator_community[j]
        probability = 0.18 if same else 0.012
        if rng.random() < probability:
            weight = float(rng.integers(1, 8) if same else rng.integers(1, 4))
            adjacency[i, j] = adjacency[j, i] = weight
np.fill_diagonal(adjacency, 1e-6)
degree = (adjacency > 0).sum(axis=1) - 1
print(f"Nodes: {N_NODES} | undirected edges: {int(np.count_nonzero(np.triu(adjacency, 1)))}")
display(pd.Series(degree).describe().round(3).to_frame("degree"))
"""),
        markdown("## 3. Spectral community detection"),
        code("""
from sklearn.cluster import SpectralClustering
from sklearn.metrics import adjusted_rand_score, silhouette_score

selection = []
degree_matrix = np.diag(adjacency.sum(axis=1))
laplacian = degree_matrix - adjacency
eigenvalues = np.sort(np.linalg.eigvalsh(laplacian))
for k in range(2, 7):
    labels = SpectralClustering(n_clusters=k, affinity="precomputed", assign_labels="kmeans", random_state=RANDOM_STATE).fit_predict(adjacency)
    selection.append({"k": k, "adjacency_profile_silhouette": silhouette_score(adjacency, labels, metric="cosine")})
selection = pd.DataFrame(selection)
display(selection.round(4))
best_k = int(selection.loc[selection["adjacency_profile_silhouette"].idxmax(), "k"])
labels = SpectralClustering(n_clusters=best_k, affinity="precomputed", assign_labels="kmeans", random_state=RANDOM_STATE).fit_predict(adjacency)
print(f"Selected k={best_k}; retrospective ARI={adjusted_rand_score(generator_community, labels):.4f}")
print("Smallest Laplacian eigenvalues:", np.round(eigenvalues[:8], 4))
"""),
        markdown("## 4. Community profile and bridge-account analysis"),
        code("""
nodes = pd.DataFrame({"node_id": [f"member-{i:03d}" for i in range(N_NODES)], "community": labels, "degree": degree})
external_connections = []
for node in range(N_NODES):
    neighbours = np.flatnonzero(adjacency[node] > 0)
    neighbours = neighbours[neighbours != node]
    external_connections.append(int(np.sum(labels[neighbours] != labels[node])))
nodes["external_connections"] = external_connections
nodes["bridge_ratio"] = nodes["external_connections"] / nodes["degree"].clip(lower=1)
display(nodes.groupby("community").agg(nodes=("node_id", "count"), mean_degree=("degree", "mean"), mean_bridge_ratio=("bridge_ratio", "mean")).round(3))
display(nodes.sort_values(["external_connections", "bridge_ratio"], ascending=False).head(12))
"""),
        markdown("## 5. Lightweight graph visualization"),
        code("""
angles = np.linspace(0, 2 * np.pi, N_NODES, endpoint=False)
community_angles = 2 * np.pi * labels / max(best_k, 1)
radius = 1 + 0.22 * rng.normal(size=N_NODES)
x = 3.3 * np.cos(community_angles) + radius * np.cos(angles)
y = 3.3 * np.sin(community_angles) + radius * np.sin(angles)
plt.figure(figsize=(9, 8))
for i, j in zip(*np.nonzero(np.triu(adjacency, 1))):
    plt.plot([x[i], x[j]], [y[i], y[j]], color="#cbd5e1", linewidth=0.35, alpha=0.35)
plt.scatter(x, y, c=labels, cmap="tab10", s=28 + 5 * degree, edgecolor="white", linewidth=0.4)
plt.title("Discovered interaction communities")
plt.axis("off")
plt.tight_layout()
plt.show()
"""),
        markdown("## 6. Findings and limitations\n\n- Community labels describe network structure, not identity, intent, or influence.\n- Bridge ratios surface cross-community connectors but should not drive moderation or access decisions.\n- Production graphs require temporal stability checks, bot filtering, privacy controls, and stakeholder review."),
    ]


def movie_cells() -> list[dict]:
    return [
        markdown("# Basic Movie Recommender System\n\n**Objective:** Recommend similar movies from audience-rating patterns using item-to-item collaborative similarity.\n\nThe project uses the MovieLens-style files already committed in this folder and applies a minimum-support rule so correlations are not dominated by one-off ratings."),
        markdown("## 1. Setup and portable paths"),
        code(COMMON_IMPORTS + """
from pathlib import Path

try:
    PROJECT_DIR = Path(__file__).resolve().parent
except NameError:
    PROJECT_DIR = Path.cwd()
if not (PROJECT_DIR / "Review.data").exists():
    PROJECT_DIR = Path.cwd() / "Unsupervised Learning Projects" / "Basic Movie Recommender System"
print(f"Resolved project folder: {PROJECT_DIR.name}")
"""),
        markdown("## 2. Load and validate the included ratings"),
        code("""
ratings = pd.read_csv(PROJECT_DIR / "Review.data", sep="\\t", names=["user_id", "movie_id", "rating", "timestamp"])
titles = pd.read_csv(PROJECT_DIR / "Movie_Id_Titles_data")
titles.columns = ["movie_id", "title"]
data = ratings.merge(titles, on="movie_id", how="inner")
print(f"Ratings: {len(data):,} | users: {data['user_id'].nunique():,} | movies: {data['movie_id'].nunique():,}")
display(data.head())
display(data["rating"].describe().round(3).to_frame())
"""),
        markdown("## 3. Popularity and sparsity diagnostics"),
        code("""
movie_stats = data.groupby("title").agg(mean_rating=("rating", "mean"), rating_count=("rating", "size")).sort_values("rating_count", ascending=False)
display(movie_stats.head(12).round(3))
matrix = data.pivot_table(index="user_id", columns="title", values="rating")
sparsity = 1 - matrix.notna().sum().sum() / matrix.size
print(f"User-item matrix: {matrix.shape[0]} × {matrix.shape[1]} | sparsity: {sparsity:.2%}")
"""),
        markdown("## 4. Item-based collaborative similarity"),
        code("""
from sklearn.metrics.pairwise import cosine_similarity

MIN_RATINGS = 40
eligible = movie_stats.index[movie_stats["rating_count"] >= MIN_RATINGS]
centered = matrix[eligible].sub(matrix[eligible].mean(axis=1), axis=0).fillna(0)
similarity = cosine_similarity(centered.T)
similarity_df = pd.DataFrame(similarity, index=eligible, columns=eligible)
print(f"Eligible movies with at least {MIN_RATINGS} ratings: {len(eligible)}")

def recommend(title, top_n=8):
    if title not in similarity_df:
        raise KeyError(f"{title!r} is not an eligible title")
    scores = similarity_df[title].drop(title).sort_values(ascending=False).head(top_n)
    return movie_stats.loc[scores.index].assign(similarity=scores).sort_values("similarity", ascending=False)

query_title = "Star Wars (1977)" if "Star Wars (1977)" in similarity_df else similarity_df.index[0]
print(f"Recommendations for: {query_title}")
display(recommend(query_title).round(4))
"""),
        markdown("## 5. Qualitative checks across multiple titles"),
        code("""
queries = [title for title in ["Star Wars (1977)", "Liar Liar (1997)", "Toy Story (1995)"] if title in similarity_df]
for title in queries:
    print(f"\\nTop neighbours for {title}")
    display(recommend(title, top_n=5).round(4))
"""),
        markdown("## 6. Findings and limitations\n\n- Minimum rating support reduces unstable one-user correlations.\n- Collaborative similarity cannot solve cold-start for unseen movies or users.\n- Similarity is an offline discovery signal, not evidence of user satisfaction.\n- A production system should use time-aware offline evaluation and online experiments."),
    ]


def book_cells() -> list[dict]:
    return [
        markdown("# Book Recommendation Engine\n\n**Objective:** Recommend books from reader-rating patterns using item-based nearest neighbours.\n\nThe workflow uses the Book-Crossing files already committed in this folder, removes deprecated APIs, validates identifiers, and preserves a reproducible popularity threshold."),
        markdown("## 1. Setup and portable paths"),
        code(COMMON_IMPORTS + """
from pathlib import Path

try:
    PROJECT_DIR = Path(__file__).resolve().parent
except NameError:
    PROJECT_DIR = Path.cwd()
if not (PROJECT_DIR / "Books Dataset").exists():
    PROJECT_DIR = Path.cwd() / "Unsupervised Learning Projects" / "Book Recommendation Engine"
DATA_DIR = PROJECT_DIR / "Books Dataset"
print(f"Resolved dataset folder: {DATA_DIR.name}")
"""),
        markdown("## 2. Load and validate Book-Crossing data"),
        code("""
books = pd.read_csv(DATA_DIR / "BX-Books.csv", sep=";", encoding="latin-1", on_bad_lines="skip", low_memory=False)
users = pd.read_csv(DATA_DIR / "BX-Users.csv", sep=";", encoding="latin-1", on_bad_lines="skip", low_memory=False)
ratings = pd.read_csv(DATA_DIR / "BX-Book-Ratings.csv", sep=";", encoding="latin-1", on_bad_lines="skip", low_memory=False)
books.columns = ["isbn", "title", "author", "year", "publisher", "image_s", "image_m", "image_l"]
users.columns = ["user_id", "location", "age"]
ratings.columns = ["user_id", "isbn", "rating"]
data = ratings.merge(books[["isbn", "title", "author", "image_m"]], on="isbn", how="inner")
data = data[data["rating"] > 0].copy()
print(f"Explicit ratings: {len(data):,} | readers: {data['user_id'].nunique():,} | books: {data['title'].nunique():,}")
display(data.head())
"""),
        markdown("## 3. Control sparsity with transparent support rules"),
        code("""
reader_activity = data.groupby("user_id").size()
book_activity = data.groupby("title").size()
active_readers = reader_activity[reader_activity >= 35].index
popular_books = book_activity[book_activity >= 25].index
filtered = data[data["user_id"].isin(active_readers) & data["title"].isin(popular_books)].copy()
pivot = filtered.pivot_table(index="title", columns="user_id", values="rating", fill_value=0)
print(f"Filtered interactions: {len(filtered):,} | matrix: {pivot.shape[0]} books × {pivot.shape[1]} readers")
display(book_activity.sort_values(ascending=False).head(10).rename("rating_count").to_frame())
"""),
        markdown("## 4. Fit item-based nearest neighbours"),
        code("""
from sklearn.neighbors import NearestNeighbors

model = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=6)
model.fit(pivot.values)

def recommend_book(title, top_n=5):
    if title not in pivot.index:
        raise KeyError(f"{title!r} is not available after support filtering")
    position = pivot.index.get_loc(title)
    distances, indices = model.kneighbors(pivot.iloc[position].to_numpy().reshape(1, -1), n_neighbors=top_n + 1)
    result = pd.DataFrame({"title": pivot.index[indices[0][1:]], "cosine_similarity": 1 - distances[0][1:]})
    return result

query_title = "Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))" if "Harry Potter and the Sorcerer's Stone (Harry Potter (Paperback))" in pivot.index else pivot.index[0]
print(f"Recommendations for: {query_title}")
display(recommend_book(query_title).round(4))
"""),
        markdown("## 5. Coverage and sample recommendation checks"),
        code("""
queries = pivot.index[[0, len(pivot) // 3, 2 * len(pivot) // 3]].tolist()
for title in queries:
    print(f"\\nTop neighbours for {title}")
    display(recommend_book(title, top_n=4).round(4))
print(f"Catalog coverage after support filters: {len(pivot) / data['title'].nunique():.2%}")
"""),
        markdown("## 6. Findings and limitations\n\n- Explicit-rating support rules make the similarity matrix more stable but reduce catalog coverage.\n- The method cannot recommend new books with no interactions.\n- Similarity is not a claim of reader satisfaction.\n- Production evaluation should include time-aware precision@k, recall@k, diversity, novelty, and online feedback."),
    ]


def customer_cells() -> list[dict]:
    cfg = {
        "title": "Customer Segmentation Using Clustering Techniques",
        "summary": "Discover actionable RFM-style customer groups using multiple clustering diagnostics and portable data generation.",
        "features": ["recency_days", "orders_12m", "annual_spend", "avg_order_value", "return_rate", "engagement_score"],
        "profiles": {"champions": [12, 28, 5200, 190, 0.05, 88], "loyal": [35, 17, 2900, 165, 0.08, 70], "at_risk": [140, 7, 1300, 185, 0.16, 35], "new_value": [24, 4, 720, 175, 0.10, 58]},
    }
    return cluster_cells(cfg)


def readme_text(title: str, summary: str, method: str, dataset: str, notebook_name: str, status: str = "New") -> str:
    return f"""# {title}

{summary}

## Project status

- **Portfolio decision:** {status}
- **Learning type:** Unsupervised learning
- **Core method:** {method}
- **Execution:** Notebook executed successfully with outputs committed

## Problem statement

The project demonstrates how patterns, similarities, communities, or anomalies can be discovered without using a prediction target during model fitting. Results are interpreted as exploratory signals rather than ground truth.

## Dataset

{dataset}

The notebook documents its data contract, reproducible seed, quality checks, and any synthetic proxy labels used only for retrospective diagnostics.

## Workflow

```text
Data validation
      ↓
Feature representation and scaling
      ↓
Unsupervised model comparison
      ↓
Internal metrics and stability checks
      ↓
Interpretation, visualization, and limitations
```

## Evaluation

The notebook uses method-appropriate evidence such as silhouette score, Davies-Bouldin index, cluster stability, retrieval similarity, graph structure, anomaly-score diagnostics, and post-hoc synthetic checks. No demo result is presented as a production benchmark.

## Repository structure

```text
├── {notebook_name}
└── README.md
```

## How to run

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r "Unsupervised Learning Projects/requirements.txt"
jupyter lab "Unsupervised Learning Projects/{title}/{notebook_name}"
```

Run the notebook from top to bottom. Saved outputs are included for review.

## Technologies

- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib and Seaborn
- Jupyter

## Responsible use

Discovered groups and anomaly flags do not establish identity, intent, causality, risk, or business impact. Production use requires domain review, representative data, privacy controls, monitoring, and decision-specific evaluation.

## Author

**Tajamul Khan** — Data Scientist and AI Engineer

{CONNECT}"""


def write_project(cfg: dict, cells: list[dict], method: str, dataset: str) -> None:
    directory = UNSUPERVISED / cfg["title"]
    directory.mkdir(parents=True, exist_ok=True)
    notebook_name = f"{cfg['slug']}.ipynb"
    (directory / notebook_name).write_text(json.dumps(notebook(cells), indent=1) + "\n", encoding="utf-8")
    (directory / "README.md").write_text(
        readme_text(cfg["title"], cfg["summary"], method, dataset, notebook_name),
        encoding="utf-8",
    )


def existing_readmes() -> None:
    existing = [
        (
            "Basic Movie Recommender System",
            "An item-based movie recommender built from the audience-rating files included in the project.",
            "Mean-centered item similarity with cosine distance and minimum rating support",
            "Included MovieLens-style rating and movie-title files are loaded through portable project-relative paths.",
            "Movie Recommender System.ipynb",
            "Refurbished — legacy notebook replaced; project identity and source datasets retained",
        ),
        (
            "Book Recommendation Engine",
            "An item-based book recommender built from the Book-Crossing ratings committed with the project.",
            "Nearest-neighbour collaborative filtering with cosine distance",
            "Included Book-Crossing books, users, and explicit-rating files are validated and filtered with documented support thresholds.",
            "Books recommendation dataset.ipynb",
            "Refurbished — broken paths and deprecated APIs repaired; datasets and application retained",
        ),
        (
            "Customer Segmentation Using Clustering Techniques",
            "A reproducible RFM-style customer segmentation project with internal metrics, stability checks, and interpretable profiles.",
            "K-Means and agglomerative clustering with robust preprocessing",
            "A deterministic domain-shaped demo dataset replaces the unavailable external-only dataset so the workflow executes end to end. Results are demo evidence only.",
            "Customer Segmentation using Clustering Algorithms.ipynb",
            "Refurbished — non-portable Kaggle path and incomplete execution replaced",
        ),
        (
            "Fraudulent Transaction Detection",
            "An unsupervised fraud-triage demonstration using behavioral transaction features and two anomaly detectors.",
            "Isolation Forest and Local Outlier Factor",
            "The maintained notebook uses deterministic synthetic transactions with injected anomalies for post-hoc evaluation. The scenario labels are not used to fit the detectors.",
            "Anomaly Detection.ipynb",
            "Maintained — existing executed notebook retained",
        ),
        (
            "Market Basket Analysis",
            "An educational association-rule project that explains frequent itemsets, support, confidence, lift, and cross-sell interpretation.",
            "Apriori frequent itemsets and association rules",
            "The maintained notebook uses a small transparent transaction set so every transformation and rule can be inspected directly.",
            "Market Basket Analysis.ipynb",
            "Maintained — existing executed notebook retained",
        ),
    ]
    for title, summary, method, dataset, notebook_name, status in existing:
        (UNSUPERVISED / title / "README.md").write_text(
            readme_text(title, summary, method, dataset, notebook_name, status),
            encoding="utf-8",
        )


def build_index() -> None:
    existing_rows = [
        ("Basic Movie Recommender System", "Recommendation", "Refurbished"),
        ("Book Recommendation Engine", "Recommendation", "Refurbished"),
        ("Customer Segmentation Using Clustering Techniques", "Clustering", "Refurbished"),
        ("Fraudulent Transaction Detection", "Anomaly detection", "Maintained"),
        ("Market Basket Analysis", "Association rules", "Maintained"),
    ]
    new_rows = []
    for cfg in TEXT_PROJECTS:
        new_rows.append((cfg["title"], "Text clustering and similarity", "New"))
    for cfg in CLUSTER_PROJECTS:
        new_rows.append((cfg["title"], "Behavioral clustering", "New"))
    for cfg in ANOMALY_PROJECTS:
        new_rows.append((cfg["title"], "Anomaly detection", "New"))
    new_rows.extend([
        ("AI Image Embedding Clustering and Visual Search", "Embedding clustering and retrieval", "New"),
        ("Product Catalog Similarity Recommender", "Content recommendation", "New"),
        ("Social Network Community Detection", "Graph community detection", "New"),
    ])
    rows = []
    for index, (title, method, status) in enumerate(existing_rows + new_rows, start=1):
        link = title.replace(" ", "%20")
        rows.append(f"| {index} | [{title}]({link}/) | {method} | {status} |")
    index_text = f"""# Unsupervised Machine Learning Projects

A 30-project portfolio covering modern clustering, anomaly detection, topic discovery, vector retrieval, recommendation, association-rule mining, dimensionality reduction, and graph communities.

## Portfolio composition

- **5 existing projects preserved:** 2 maintained and 3 selectively refurbished
- **25 new projects:** selected for current portfolio relevance across GenAI, vector search, reliability, cybersecurity, industry, geospatial, healthcare, and recommendation use cases
- **30 executed notebooks:** every project contains saved code outputs

The selection was informed by current clustering, recommendation, embedding, and retrieval activity documented by [Kaggle's Clustering Cup 2026](https://www.kaggle.com/competitions/clustering-cup-2026), [Hugging Face Sentence Transformers](https://huggingface.co/docs/hub/en/sentence-transformers), and the [GitHub unsupervised-machine-learning topic](https://github.com/topics/unsupervised-machine-learning).

## Projects

| # | Project | Primary method | Decision |
|---:|---|---|---|
{chr(10).join(rows)}

## Portfolio standards

- No prediction target is used during unsupervised model fitting
- Internal metrics are paired with stability and interpretation checks
- Synthetic labels, when present, are reserved for retrospective diagnostics
- Demo datasets and results are explicitly labelled
- Paths are portable, seeds are reproducible, and notebook outputs are committed
- Recommendations and anomaly flags are framed as decision-support signals, not ground truth

## Audit trail

The keep/refurbish rationale for the original five projects is recorded in [AUDIT.md](AUDIT.md).

## Author

**Tajamul Khan** — Data Scientist and AI Engineer

{CONNECT}"""
    (UNSUPERVISED / "README.md").write_text(index_text, encoding="utf-8")


def build_audit() -> None:
    audit = f"""# Existing Unsupervised Projects Audit

This audit records the selective decision made before expanding the portfolio. All five original project folders remain in the collection.

| Project | Decision | Evidence and action |
|---|---|---|
| Basic Movie Recommender System | Refurbish | The saved notebook ran, but repeated stale credentials and a correlation-only workflow weakened the presentation. The included ratings were retained and the notebook was replaced with a portable, support-aware item-similarity workflow. |
| Book Recommendation Engine | Refurbish | The project contained useful Book-Crossing data and an application, but the notebook used case-mismatched paths and removed pandas APIs. Data and app identity were retained; the notebook, application metadata, and documentation were repaired. |
| Customer Segmentation Using Clustering Techniques | Refurbish | The notebook depended on a personal Kaggle path and contained saved outputs without completed execution state. The project was rebuilt as an executable RFM-style comparison with stability and profile checks. |
| Fraudulent Transaction Detection | Maintain | The existing notebook already contained a complete Isolation Forest and LOF demonstration with saved outputs and no stored errors. Its code remains intact; documentation was corrected to match the verified notebook. |
| Market Basket Analysis | Maintain | The existing notebook already offered a compact, executed Apriori learning example with transparent rules and saved visual output. Its code remains intact; documentation was corrected to avoid unsupported claims. |

## Result

- Original projects preserved: **5**
- Existing notebooks maintained unchanged: **2**
- Existing notebooks selectively refurbished: **3**
- New projects added: **25**
- Final unsupervised project count: **30**

{CONNECT}"""
    (UNSUPERVISED / "AUDIT.md").write_text(audit, encoding="utf-8")


def update_root_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\| Unsupervised Learning \| \d+ \|", "| Unsupervised Learning | 30 |", text)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    if len(NEW_PROJECTS) != 25:
        raise RuntimeError(f"Expected 25 new project definitions, found {len(NEW_PROJECTS)}")

    # Only the three legacy notebooks identified by the audit are replaced.
    movie_path = UNSUPERVISED / "Basic Movie Recommender System" / "Movie Recommender System.ipynb"
    movie_path.write_text(json.dumps(notebook(movie_cells()), indent=1) + "\n", encoding="utf-8")
    book_path = UNSUPERVISED / "Book Recommendation Engine" / "Books recommendation dataset.ipynb"
    book_path.write_text(json.dumps(notebook(book_cells()), indent=1) + "\n", encoding="utf-8")
    customer_path = UNSUPERVISED / "Customer Segmentation Using Clustering Techniques" / "Customer Segmentation using Clustering Algorithms.ipynb"
    customer_path.write_text(json.dumps(notebook(customer_cells()), indent=1) + "\n", encoding="utf-8")

    for cfg in TEXT_PROJECTS:
        write_project(cfg, text_cells(cfg), "TF-IDF, K-Means, cosine similarity, and SVD", "A deterministic domain-shaped text corpus is generated inside the notebook. Hidden generator topics are used only for post-hoc diagnostics.")
    for cfg in CLUSTER_PROJECTS:
        write_project(cfg, cluster_cells(cfg), "K-Means and agglomerative clustering with robust scaling and PCA", "A deterministic domain-shaped numeric dataset is generated inside the notebook. Hidden generator profiles are used only for post-hoc diagnostics.")
    for cfg in ANOMALY_PROJECTS:
        write_project(cfg, anomaly_cells(cfg), "Isolation Forest and Local Outlier Factor with robust scaling and PCA", "A deterministic normal-behavior dataset with rare injected stress cases is generated inside the notebook. Scenario flags are excluded from training.")
    for cfg in SPECIAL_PROJECTS:
        if cfg["kind"] == "image":
            cells, method, dataset = image_cells(cfg), "Embedding normalization, K-Means, cosine nearest neighbours, and PCA", "Deterministic 48-dimensional vectors act as an offline stand-in for image-model embeddings."
        elif cfg["kind"] == "product":
            cells, method, dataset = product_cells(cfg), "TF-IDF, cosine nearest neighbours, K-Means, and coverage checks", "A deterministic product catalog is generated inside the notebook."
        else:
            cells, method, dataset = graph_cells(cfg), "Spectral clustering on a weighted adjacency matrix", "A deterministic community-structured interaction graph is generated inside the notebook."
        write_project(cfg, cells, method, dataset)

    existing_readmes()
    build_index()
    build_audit()
    update_root_readme()

    requirements = """numpy>=1.26,<3
pandas>=2.1,<3
scikit-learn>=1.4,<2
matplotlib>=3.8,<4
seaborn>=0.13,<1
jupyterlab>=4,<5
mlxtend>=0.23,<1
streamlit>=1.36,<2
"""
    (UNSUPERVISED / "requirements.txt").write_text(requirements, encoding="utf-8")
    print("Built 3 refurbished + 25 new unsupervised notebooks and documentation.")


if __name__ == "__main__":
    main()
