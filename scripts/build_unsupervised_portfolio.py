#!/usr/bin/env python3
"""Build the canonical 21-project unsupervised-learning portfolio."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


REPO = Path(__file__).resolve().parents[1]
PORTFOLIO = REPO / "Unsupervised Learning Projects"


@dataclass(frozen=True)
class Project:
    slug: str
    title: str
    filename: str
    summary: str
    category: str
    dataset: str
    data_mode: str
    method: str
    metrics: str
    source: str
    kind: str


PROJECTS = [
    Project(
        "Movie Recommendation System",
        "Movie Recommendation System",
        "movie_recommendation_system.ipynb",
        "Build an item-to-item collaborative-filtering recommender from explicit movie ratings.",
        "Recommendation",
        "MovieLens-style ratings and movie-title tables committed with the project.",
        "Committed dataset",
        "User-item filtering, cosine similarity and popularity-aware candidate filtering",
        "Neighbour similarity, catalogue coverage and recommendation sanity checks",
        "https://grouplens.org/datasets/movielens/",
        "movie",
    ),
    Project(
        "Book Recommendation Engine",
        "Book Recommendation Engine",
        "book_recommendation_engine.ipynb",
        "Create a collaborative-filtering engine that recommends books from reader-rating behaviour.",
        "Recommendation",
        "Deterministic demonstration ratings; schema supports the Book-Crossing dataset.",
        "Verified demo mode",
        "Interaction filtering, item cosine similarity and popularity-aware recommendations",
        "Neighbour similarity, coverage and recommendation diversity",
        "https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset",
        "book",
    ),
    Project(
        "Customer Segmentation Using Clustering",
        "Customer Segmentation Using Clustering",
        "customer_segmentation_clustering.ipynb",
        "Discover actionable customer groups from recency, frequency, monetary and engagement behaviour.",
        "Clustering",
        "Deterministic RFM-style demonstration data; schema supports Online Retail transactions.",
        "Verified demo mode",
        "Robust feature scaling, K-Means selection, PCA visualisation and segment profiling",
        "Silhouette, Davies-Bouldin, Calinski-Harabasz and seed stability",
        "https://archive.ics.uci.edu/dataset/352/online+retail",
        "customer",
    ),
    Project(
        "Fraud Detection Using Anomaly Detection",
        "Fraud Detection Using Anomaly Detection",
        "fraud_anomaly_detection.ipynb",
        "Rank suspicious transactions without using fraud labels during model fitting.",
        "Anomaly detection",
        "Deterministic transaction demonstration data with hidden labels used only for evaluation.",
        "Verified demo mode",
        "Isolation Forest, Local Outlier Factor and anomaly-score diagnostics",
        "ROC-AUC, average precision, precision at k and alert-rate analysis",
        "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud",
        "anomaly_fraud",
    ),
    Project(
        "Market Basket Analysis",
        "Market Basket Analysis",
        "market_basket_analysis.ipynb",
        "Mine interpretable product affinities and cross-sell rules from transaction baskets.",
        "Pattern mining",
        "Deterministic retail basket generator with realistic product bundles.",
        "Verified demo mode",
        "Frequent singleton and pair mining with support, confidence and lift",
        "Rule support, confidence, lift and catalogue coverage",
        "https://archive.ics.uci.edu/dataset/352/online+retail",
        "basket",
    ),
    Project(
        "Spotify Song Clustering and Playlist Discovery",
        "Spotify Song Clustering and Playlist Discovery",
        "spotify_song_clustering.ipynb",
        "Group tracks by audio characteristics and turn clusters into coherent playlist seeds.",
        "Clustering",
        "Deterministic Spotify-style audio-feature data with hidden genres for evaluation only.",
        "Verified demo mode",
        "Feature scaling, K-Means selection, PCA projection and cluster profiling",
        "Silhouette, Davies-Bouldin, adjusted Rand index and cluster balance",
        "https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset",
        "audio",
    ),
    Project(
        "Netflix Content Clustering and Similarity",
        "Netflix Content Clustering and Similarity",
        "netflix_content_clustering.ipynb",
        "Cluster streaming titles and retrieve similar content from metadata and descriptions.",
        "Recommendation",
        "Deterministic Netflix-style catalogue covering five content themes.",
        "Verified demo mode",
        "TF-IDF, K-Means, nearest neighbours and metadata-aware similarity",
        "Silhouette, neighbour relevance and cluster profile inspection",
        "https://www.kaggle.com/datasets/shivamb/netflix-shows",
        "netflix",
    ),
    Project(
        "News Article Topic Modeling",
        "News Article Topic Modeling",
        "news_article_topic_modeling.ipynb",
        "Discover recurring themes in an unlabeled news corpus and explain them with top terms.",
        "NLP and topic modelling",
        "Deterministic demonstration corpus spanning AI, finance, health, climate and sport.",
        "Verified demo mode",
        "TF-IDF, non-negative matrix factorisation and topic assignment",
        "Reconstruction error, topic diversity and document-topic concentration",
        "https://www.kaggle.com/datasets/rmisra/news-category-dataset",
        "topic_news",
    ),
    Project(
        "Customer Review Topic Modeling",
        "Customer Review Topic Modeling",
        "customer_review_topic_modeling.ipynb",
        "Turn unstructured customer feedback into interpretable product and service themes.",
        "NLP and topic modelling",
        "Deterministic review corpus covering delivery, quality, pricing, support and usability.",
        "Verified demo mode",
        "TF-IDF, NMF topic extraction and topic-level review inspection",
        "Reconstruction error, topic diversity and topic prevalence",
        "https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews",
        "topic_reviews",
    ),
    Project(
        "Resume and Job Description Semantic Matching",
        "Resume and Job Description Semantic Matching",
        "resume_job_semantic_matching.ipynb",
        "Rank job descriptions for each resume without labels or external embedding APIs.",
        "NLP similarity",
        "Curated demonstration resumes and role descriptions across data and engineering careers.",
        "Verified demo mode",
        "TF-IDF, latent semantic analysis and cosine similarity",
        "Top-match relevance, score margin and ranking inspection",
        "Replace the demonstration corpus with consented, de-identified documents.",
        "semantic_resume",
    ),
    Project(
        "Document Similarity Search Using LSA",
        "Document Similarity Search Using LSA",
        "document_similarity_search_lsa.ipynb",
        "Build a lightweight semantic search engine over technical documents.",
        "NLP similarity",
        "Curated technical document snippets covering data, cloud and machine learning.",
        "Verified demo mode",
        "TF-IDF, truncated SVD, vector normalisation and nearest-neighbour retrieval",
        "Explained variance, score separation and retrieval sanity checks",
        "Replace with an owned document collection for production use.",
        "semantic_search",
    ),
    Project(
        "Image Compression Using K-Means",
        "Image Compression Using K-Means",
        "image_compression_kmeans.ipynb",
        "Compress an image by replacing millions of possible colours with a learned palette.",
        "Computer vision",
        "Deterministic generated image with gradients, objects and texture.",
        "Verified demo mode",
        "Pixel sampling, MiniBatch K-Means quantisation and image reconstruction",
        "MSE, PSNR, palette size and approximate storage reduction",
        "Replace the generated image with an owned RGB image.",
        "image_compression",
    ),
    Project(
        "Brand Color Palette Extraction",
        "Brand Color Palette Extraction",
        "brand_color_palette_extraction.ipynb",
        "Extract dominant brand colours and their visual share from a design asset.",
        "Computer vision",
        "Deterministic generated brand board with six dominant colour regions.",
        "Verified demo mode",
        "RGB pixel clustering, palette ordering, colour proportions and HEX conversion",
        "Quantisation error, palette coverage and colour share",
        "Replace the generated board with an owned brand image.",
        "palette",
    ),
    Project(
        "Handwritten Digit Clustering",
        "Handwritten Digit Clustering",
        "handwritten_digit_clustering.ipynb",
        "Test how well unsupervised clusters recover digit structure from raw pixel intensities.",
        "Clustering",
        "Scikit-learn handwritten digits dataset.",
        "Built-in dataset",
        "Standardisation, PCA, K-Means and cluster-to-label diagnostics",
        "Silhouette, adjusted Rand index, normalized mutual information and purity",
        "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html",
        "digits",
    ),
    Project(
        "Geospatial Delivery Hotspot Clustering",
        "Geospatial Delivery Hotspot Clustering",
        "geospatial_delivery_hotspots.ipynb",
        "Detect dense delivery zones and geographic noise from latitude-longitude events.",
        "Geospatial clustering",
        "Deterministic delivery events around Hyderabad-style commercial hubs.",
        "Verified demo mode",
        "Haversine DBSCAN, hotspot ranking and noise analysis",
        "Cluster count, noise rate, hotspot density and non-noise silhouette",
        "Replace with privacy-safe delivery coordinates.",
        "geo",
    ),
    Project(
        "Cryptocurrency Market Regime Detection",
        "Cryptocurrency Market Regime Detection",
        "cryptocurrency_market_regimes.ipynb",
        "Identify calm, trending and stressed crypto regimes from rolling market behaviour.",
        "Financial clustering",
        "Deterministic synthetic daily crypto market with hidden regimes for evaluation only.",
        "Verified demo mode",
        "Rolling feature engineering, scaling, K-Means and chronological regime profiles",
        "Silhouette, stability, adjusted Rand index and transition analysis",
        "Replace with licensed OHLCV market data.",
        "regimes",
    ),
    Project(
        "Stock Portfolio Diversification Using Asset Clustering",
        "Stock Portfolio Diversification Using Asset Clustering",
        "stock_asset_clustering.ipynb",
        "Cluster assets by return behaviour to support more diversified portfolio selection.",
        "Financial clustering",
        "Deterministic multi-factor return simulation for 24 assets across six sectors.",
        "Verified demo mode",
        "Return statistics, correlation features, hierarchical clustering and representative selection",
        "Silhouette, within-cluster correlation and between-cluster correlation",
        "Replace with adjusted, licensed historical asset prices.",
        "assets",
    ),
    Project(
        "Network Intrusion Anomaly Detection",
        "Network Intrusion Anomaly Detection",
        "network_intrusion_anomaly_detection.ipynb",
        "Rank unusual network sessions while keeping attack labels out of model fitting.",
        "Anomaly detection",
        "Deterministic network-flow data with hidden attacks for evaluation only.",
        "Verified demo mode",
        "Isolation Forest, Local Outlier Factor and score-distribution analysis",
        "ROC-AUC, average precision, precision at k and alert rate",
        "https://www.unb.ca/cic/datasets/ids-2017.html",
        "anomaly_network",
    ),
    Project(
        "Predictive Maintenance Sensor Anomaly Detection",
        "Predictive Maintenance Sensor Anomaly Detection",
        "predictive_maintenance_anomalies.ipynb",
        "Detect abnormal equipment states from multivariate sensor readings.",
        "Anomaly detection",
        "Deterministic industrial sensor data with hidden failure windows for evaluation only.",
        "Verified demo mode",
        "Isolation Forest, Local Outlier Factor and sensor-level error inspection",
        "ROC-AUC, average precision, precision at k and alert-rate analysis",
        "https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification",
        "anomaly_sensor",
    ),
    Project(
        "Time Series Anomaly Detection",
        "Time Series Anomaly Detection",
        "time_series_anomaly_detection.ipynb",
        "Find spikes, drops and level shifts in a seasonal signal without supervised training.",
        "Anomaly detection",
        "Deterministic seasonal time series with hidden anomalies for evaluation only.",
        "Verified demo mode",
        "Rolling residual features, robust z-scores and Isolation Forest",
        "ROC-AUC, average precision, precision at k and event coverage",
        "Replace with a timestamped operational metric.",
        "anomaly_timeseries",
    ),
    Project(
        "PCA and Manifold Learning Visual Lab",
        "PCA and Manifold Learning Visual Lab",
        "pca_manifold_learning_lab.ipynb",
        "Compare linear and nonlinear low-dimensional views of high-dimensional observations.",
        "Dimensionality reduction",
        "Scikit-learn handwritten digits dataset.",
        "Built-in dataset",
        "Standardisation, PCA, t-SNE and neighbourhood visualisation",
        "Explained variance, trustworthiness and downstream clustering quality",
        "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html",
        "dimension",
    ),
]


def clean(text: str) -> str:
    return dedent(text).strip()


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": clean(text).splitlines(keepends=True)}


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": clean(text).splitlines(keepends=True),
    }


def setup(imports: str) -> dict:
    imports = clean(imports)
    common = clean(
        """
        from pathlib import Path
        import warnings

        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
        import seaborn as sns
        """
    )
    configuration = clean(
        """
        warnings.filterwarnings("ignore")
        RANDOM_STATE = 42
        rng = np.random.default_rng(RANDOM_STATE)
        sns.set_theme(style="whitegrid", context="notebook")
        pd.set_option("display.max_columns", 50)
        """
    )
    return code(f"{common}\n{imports}\n\n{configuration}")


def ending(project: Project) -> list[dict]:
    return [
        md(
            f"""
            ## 10. Interpretation and responsible use

            Treat the output as exploratory evidence, not ground truth. For {project.title.lower()},
            validate stability on newer data, inspect edge cases, and review domain risks before
            turning clusters, rankings or anomaly scores into decisions.
            """
        ),
        md(
            """
            ## 11. Next steps

            - Replace demonstration data with a versioned, licensed dataset.
            - Track data quality, drift and stability across repeated runs.
            - Add domain-specific review before deployment.
            - Package inference only after reproducibility and privacy checks pass.

            All numeric results are generated at execution time; none are hard-coded.
            """
        ),
    ]


def movie_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup\n\nUse only portable paths and keep ratings separate from evaluation logic."),
        setup("from sklearn.metrics.pairwise import cosine_similarity\nfrom sklearn.decomposition import TruncatedSVD"),
        md("## 2. Data loading\n\nThe committed tables follow a compact MovieLens-style schema."),
        code(
            """
            project_dir = Path.cwd()
            if not (project_dir / "ratings.tsv").exists():
                project_dir = Path("Unsupervised Learning Projects/Movie Recommendation System")

            ratings = pd.read_csv(
                project_dir / "ratings.tsv",
                sep="\\t",
                names=["user_id", "item_id", "rating", "timestamp"],
            )
            titles = pd.read_csv(project_dir / "movie_titles.csv")
            interactions = ratings.merge(titles, on="item_id", how="inner")
            interactions.head()
            """
        ),
        md("## 3. Data quality and behaviour checks"),
        code(
            """
            quality = pd.Series({
                "ratings": len(interactions),
                "users": interactions["user_id"].nunique(),
                "movies": interactions["item_id"].nunique(),
                "missing_cells": int(interactions.isna().sum().sum()),
                "duplicate_user_movie": int(interactions.duplicated(["user_id", "item_id"]).sum()),
            })
            display(quality.to_frame("value"))
            display(interactions["rating"].describe().to_frame().T)
            """
        ),
        md("## 4. Exploratory analysis"),
        code(
            """
            movie_stats = interactions.groupby("title").agg(
                rating_count=("rating", "size"),
                mean_rating=("rating", "mean"),
            ).sort_values("rating_count", ascending=False)
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            sns.histplot(interactions["rating"], discrete=True, ax=axes[0])
            movie_stats.head(15).sort_values("rating_count").plot.barh(
                y="rating_count", legend=False, ax=axes[1], color="#2563eb"
            )
            axes[0].set_title("Rating distribution")
            axes[1].set_title("Most-rated movies")
            plt.tight_layout()
            """
        ),
        md("## 5. Interaction filtering and similarity model"),
        code(
            """
            min_movie_ratings = max(20, int(movie_stats["rating_count"].quantile(0.65)))
            active_movies = movie_stats.query("rating_count >= @min_movie_ratings").index
            filtered = interactions[interactions["title"].isin(active_movies)]
            user_movie = filtered.pivot_table(index="user_id", columns="title", values="rating")
            movie_user = user_movie.T.fillna(0)
            similarity = pd.DataFrame(
                cosine_similarity(movie_user),
                index=movie_user.index,
                columns=movie_user.index,
            )
            np.fill_diagonal(similarity.values, 0)

            def recommend(title, n=8):
                neighbours = similarity.loc[title].nlargest(n)
                return pd.DataFrame({"title": neighbours.index, "similarity": neighbours.values})

            seed_title = movie_stats.loc[active_movies].sort_values("rating_count", ascending=False).index[0]
            recommendations = recommend(seed_title)
            print(f"Seed movie: {seed_title}")
            display(recommendations)
            """
        ),
        md("## 6. Evaluation without pretending similarity is accuracy"),
        code(
            """
            sample_titles = similarity.index[: min(100, len(similarity))]
            top_neighbours = {
                title: set(similarity.loc[title].nlargest(5).index)
                for title in sample_titles
            }
            recommended_catalogue = set().union(*top_neighbours.values())
            coverage = len(recommended_catalogue) / len(similarity)
            mean_top_similarity = np.mean([
                similarity.loc[title].nlargest(5).mean() for title in sample_titles
            ])
            display(pd.DataFrame({
                "metric": ["catalogue coverage", "mean top-5 similarity"],
                "value": [coverage, mean_top_similarity],
            }))
            """
        ),
        md("## 7. Latent-space diagnostic"),
        code(
            """
            n_components = min(12, movie_user.shape[1] - 1, movie_user.shape[0] - 1)
            embedding = TruncatedSVD(n_components=n_components, random_state=RANDOM_STATE).fit_transform(movie_user)
            sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], alpha=0.6)
            plt.title("Movies in a latent interaction space")
            plt.xlabel("Component 1")
            plt.ylabel("Component 2")
            plt.tight_layout()
            """
        ),
        md("## 8. Recommendation inspection"),
        code(
            """
            inspection = recommendations.merge(movie_stats, left_on="title", right_index=True)
            display(inspection.round(3))
            """
        ),
        md("## 9. Key findings\n\nPopularity filtering reduces noisy similarities; catalogue coverage reveals whether recommendations collapse onto a few titles."),
        *ending(project),
    ]


def demo_recommender_cells(project: Project, book: bool) -> list[dict]:
    item_word = "book" if book else "title"
    return [
        md("## 1. Project setup"),
        setup("from sklearn.metrics.pairwise import cosine_similarity"),
        md("## 2. Transparent demonstration data"),
        code(
            f"""
            categories = ["data", "fiction", "history", "business", "science"]
            items = pd.DataFrame({{
                "item_id": np.arange(30),
                "title": [f"{item_word.title()} {{i + 1:02d}}" for i in range(30)],
                "category": np.repeat(categories, 6),
            }})
            user_preferences = rng.dirichlet(np.ones(len(categories)) * 0.8, size=90)
            rows = []
            for user_id, preferences in enumerate(user_preferences):
                chosen = rng.choice(items["item_id"], size=rng.integers(8, 18), replace=False)
                for item_id in chosen:
                    category_index = categories.index(items.loc[item_id, "category"])
                    latent = 1 + 4 * preferences[category_index]
                    rating = int(np.clip(np.rint(latent + rng.normal(0, 0.7)), 1, 5))
                    rows.append((user_id, item_id, rating))
            ratings = pd.DataFrame(rows, columns=["user_id", "item_id", "rating"])
            interactions = ratings.merge(items, on="item_id")
            display(interactions.head())
            """
        ),
        md("## 3. Data quality and interaction density"),
        code(
            """
            density = len(ratings) / (ratings["user_id"].nunique() * ratings["item_id"].nunique())
            display(pd.Series({
                "ratings": len(ratings),
                "users": ratings["user_id"].nunique(),
                "items": ratings["item_id"].nunique(),
                "interaction_density": density,
                "duplicate_pairs": ratings.duplicated(["user_id", "item_id"]).sum(),
            }).to_frame("value"))
            """
        ),
        md("## 4. Exploratory analysis"),
        code(
            """
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            sns.countplot(data=interactions, x="rating", ax=axes[0], color="#2563eb")
            interactions.groupby("category")["rating"].mean().sort_values().plot.barh(
                ax=axes[1], color="#10b981"
            )
            axes[0].set_title("Rating distribution")
            axes[1].set_title("Average rating by category")
            plt.tight_layout()
            """
        ),
        md("## 5. Item-to-item collaborative filtering"),
        code(
            """
            popularity = ratings.groupby("item_id").size()
            eligible = popularity[popularity >= popularity.quantile(0.25)].index
            matrix = ratings[ratings["item_id"].isin(eligible)].pivot_table(
                index="item_id", columns="user_id", values="rating"
            ).fillna(0)
            similarity = pd.DataFrame(
                cosine_similarity(matrix), index=matrix.index, columns=matrix.index
            )
            np.fill_diagonal(similarity.values, 0)

            def recommend(item_id, n=6):
                scores = similarity.loc[item_id].nlargest(n)
                result = items.set_index("item_id").loc[scores.index].copy()
                result["similarity"] = scores.values
                return result.reset_index()

            seed_item = int(popularity.idxmax())
            recommendations = recommend(seed_item)
            display(items.query("item_id == @seed_item"))
            display(recommendations)
            """
        ),
        md("## 6. Coverage and diversity checks"),
        code(
            """
            sample_items = list(similarity.index[:20])
            recs = pd.concat([recommend(item_id, 5).assign(seed=item_id) for item_id in sample_items])
            coverage = recs["item_id"].nunique() / len(items)
            diversity = recs.groupby("seed")["category"].nunique().mean()
            display(pd.DataFrame({
                "metric": ["catalogue coverage", "mean category diversity"],
                "value": [coverage, diversity],
            }))
            """
        ),
        md("## 7. Similarity diagnostics"),
        code(
            """
            subset = similarity.iloc[:12, :12]
            sns.heatmap(subset, cmap="Blues")
            plt.title("Item similarity sample")
            plt.tight_layout()
            """
        ),
        md("## 8. Recommendation explanation"),
        code(
            """
            seed_category = items.set_index("item_id").loc[seed_item, "category"]
            recommendations["same_category_as_seed"] = recommendations["category"].eq(seed_category)
            display(recommendations)
            """
        ),
        md("## 9. Key findings\n\nEvaluate relevance, coverage and diversity together; a high similarity score alone does not prove a useful recommender."),
        *ending(project),
    ]


def customer_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.decomposition import PCA\n"
            "from sklearn.metrics import adjusted_rand_score, calinski_harabasz_score, davies_bouldin_score, silhouette_score\n"
            "from sklearn.preprocessing import RobustScaler"
        ),
        md("## 2. RFM-style customer data"),
        code(
            """
            segment_sizes = [310, 250, 240, 200]
            prototypes = [
                [15, 18, 1800, 24, 0.02],
                [65, 9, 850, 14, 0.05],
                [150, 3, 260, 5, 0.12],
                [35, 26, 3200, 32, 0.03],
            ]
            rows = []
            for segment, (size, proto) in enumerate(zip(segment_sizes, prototypes)):
                recency, frequency, monetary, engagement, return_rate = proto
                rows.append(pd.DataFrame({
                    "recency_days": np.clip(rng.normal(recency, recency * 0.25 + 3, size), 1, None),
                    "purchase_frequency": np.clip(rng.normal(frequency, 3, size), 1, None),
                    "monetary_value": np.clip(rng.lognormal(np.log(monetary), 0.28, size), 20, None),
                    "digital_engagement": np.clip(rng.normal(engagement, 4, size), 0, 40),
                    "return_rate": np.clip(rng.normal(return_rate, 0.02, size), 0, 0.4),
                    "hidden_segment": segment,
                }))
            customers = pd.concat(rows, ignore_index=True).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
            feature_names = ["recency_days", "purchase_frequency", "monetary_value", "digital_engagement", "return_rate"]
            display(customers.head())
            """
        ),
        md("## 3. Data quality and distributions"),
        code(
            """
            display(customers[feature_names].describe().T)
            print("Missing cells:", int(customers[feature_names].isna().sum().sum()))
            customers[feature_names].hist(figsize=(12, 7), bins=25)
            plt.tight_layout()
            """
        ),
        md("## 4. Robust feature preparation"),
        code(
            """
            scaler = RobustScaler()
            X = scaler.fit_transform(customers[feature_names])
            """
        ),
        md("## 5. Choose the number of clusters with multiple metrics"),
        code(
            """
            rows = []
            for k in range(2, 9):
                candidate = KMeans(n_clusters=k, n_init=25, random_state=RANDOM_STATE)
                candidate_labels = candidate.fit_predict(X)
                rows.append({
                    "k": k,
                    "silhouette": silhouette_score(X, candidate_labels),
                    "davies_bouldin": davies_bouldin_score(X, candidate_labels),
                    "calinski_harabasz": calinski_harabasz_score(X, candidate_labels),
                })
            scores = pd.DataFrame(rows)
            display(scores.round(3))
            best_k = int(scores.sort_values(["silhouette", "davies_bouldin"], ascending=[False, True]).iloc[0]["k"])
            model = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE)
            customers["cluster"] = model.fit_predict(X)
            print("Selected clusters:", best_k)
            """
        ),
        md("## 6. Stability check"),
        code(
            """
            stability = []
            for seed in [7, 19, 31, 43, 71]:
                alternative = KMeans(n_clusters=best_k, n_init=20, random_state=seed).fit_predict(X)
                stability.append(adjusted_rand_score(customers["cluster"], alternative))
            display(pd.Series(stability, name="adjusted_rand_vs_reference").describe().to_frame())
            """
        ),
        md("## 7. Segment profiles"),
        code(
            """
            profile = customers.groupby("cluster")[feature_names].mean()
            profile["customers"] = customers.groupby("cluster").size()
            display(profile.round(2))
            sns.heatmap(profile[feature_names].apply(lambda col: (col - col.mean()) / col.std()), cmap="vlag", center=0)
            plt.title("Standardised segment profiles")
            plt.tight_layout()
            """
        ),
        md("## 8. Two-dimensional projection"),
        code(
            """
            projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
            sns.scatterplot(x=projection[:, 0], y=projection[:, 1], hue=customers["cluster"], palette="tab10", s=35)
            plt.title("Customer segments in PCA space")
            plt.tight_layout()
            """
        ),
        md("## 9. Key findings\n\nName segments only after reading their profiles. Cluster IDs are arbitrary and should never be treated as ordered customer value."),
        *ending(project),
    ]


def anomaly_cells(project: Project, variant: str) -> list[dict]:
    generators = {
        "fraud": """
            n_normal, n_anomaly = 2850, 150
            normal = pd.DataFrame({
                "amount": rng.lognormal(3.2, 0.7, n_normal),
                "velocity_1h": rng.poisson(2.0, n_normal),
                "distance_from_home": rng.gamma(2.0, 4.0, n_normal),
                "merchant_risk": rng.beta(2, 8, n_normal),
                "night_transaction": rng.binomial(1, 0.18, n_normal),
            })
            anomalies = pd.DataFrame({
                "amount": rng.lognormal(5.0, 0.9, n_anomaly),
                "velocity_1h": rng.poisson(8.0, n_anomaly),
                "distance_from_home": rng.gamma(5.0, 10.0, n_anomaly),
                "merchant_risk": rng.beta(7, 2, n_anomaly),
                "night_transaction": rng.binomial(1, 0.72, n_anomaly),
            })
        """,
        "network": """
            n_normal, n_anomaly = 2850, 150
            normal = pd.DataFrame({
                "duration": rng.exponential(2.5, n_normal),
                "bytes_out": rng.lognormal(7.0, 0.7, n_normal),
                "packet_rate": rng.lognormal(3.0, 0.5, n_normal),
                "failed_logins": rng.poisson(0.08, n_normal),
                "unique_ports": rng.poisson(2.0, n_normal) + 1,
            })
            anomalies = pd.DataFrame({
                "duration": rng.exponential(12.0, n_anomaly),
                "bytes_out": rng.lognormal(9.0, 1.0, n_anomaly),
                "packet_rate": rng.lognormal(5.2, 0.8, n_anomaly),
                "failed_logins": rng.poisson(4.0, n_anomaly),
                "unique_ports": rng.poisson(18.0, n_anomaly) + 1,
            })
        """,
        "sensor": """
            n_normal, n_anomaly = 2850, 150
            normal = pd.DataFrame({
                "vibration": rng.normal(2.0, 0.25, n_normal),
                "temperature": rng.normal(68, 4, n_normal),
                "pressure": rng.normal(31, 1.8, n_normal),
                "rotation_speed": rng.normal(1450, 65, n_normal),
                "current": rng.normal(11.5, 0.8, n_normal),
            })
            anomalies = pd.DataFrame({
                "vibration": rng.normal(4.8, 0.8, n_anomaly),
                "temperature": rng.normal(91, 8, n_anomaly),
                "pressure": rng.normal(24, 4, n_anomaly),
                "rotation_speed": rng.normal(1180, 180, n_anomaly),
                "current": rng.normal(16.5, 2.1, n_anomaly),
            })
        """,
    }
    if variant == "timeseries":
        data_code = """
            n = 1600
            timestamp = pd.date_range("2024-01-01", periods=n, freq="h")
            baseline = 40 + 6 * np.sin(np.arange(n) * 2 * np.pi / 24) + 2 * np.sin(np.arange(n) * 2 * np.pi / (24 * 7))
            value = baseline + rng.normal(0, 1.4, n)
            hidden_label = np.zeros(n, dtype=int)
            anomaly_points = rng.choice(np.arange(80, n - 80), size=45, replace=False)
            value[anomaly_points] += rng.choice([-1, 1], size=len(anomaly_points)) * rng.uniform(9, 18, len(anomaly_points))
            hidden_label[anomaly_points] = 1
            value[1100:1125] += 11
            hidden_label[1100:1125] = 1
            data = pd.DataFrame({"timestamp": timestamp, "value": value, "hidden_label": hidden_label})
            data["rolling_mean"] = data["value"].rolling(48, center=True, min_periods=12).mean()
            data["rolling_std"] = data["value"].rolling(48, center=True, min_periods=12).std()
            data["residual"] = data["value"] - data["rolling_mean"]
            data["change"] = data["value"].diff()
            data = data.dropna().reset_index(drop=True)
            feature_names = ["value", "rolling_mean", "rolling_std", "residual", "change"]
            display(data.head())
        """
    else:
        data_code = (
            generators[variant]
            + """
            normal["hidden_label"] = 0
            anomalies["hidden_label"] = 1
            data = pd.concat([normal, anomalies], ignore_index=True).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
            feature_names = [column for column in data.columns if column != "hidden_label"]
            display(data.head())
            """
        )
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.ensemble import IsolationForest\n"
            "from sklearn.metrics import average_precision_score, roc_auc_score\n"
            "from sklearn.neighbors import LocalOutlierFactor\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Demonstration data with labels hidden from fitting"),
        code(data_code),
        md("## 3. Data quality and baseline prevalence"),
        code(
            """
            display(data[feature_names].describe().T)
            print("Missing cells:", int(data[feature_names].isna().sum().sum()))
            hidden_prevalence = data["hidden_label"].mean()
            print(f"Hidden evaluation prevalence: {hidden_prevalence:.3%}")
            """
        ),
        md("## 4. Feature distributions"),
        code(
            """
            data[feature_names].hist(figsize=(12, 7), bins=30)
            plt.suptitle("Feature distributions", y=1.02)
            plt.tight_layout()
            """
        ),
        md("## 5. Fit unsupervised detectors"),
        code(
            """
            X = StandardScaler().fit_transform(data[feature_names])
            contamination = max(0.01, min(0.15, hidden_prevalence))
            isolation = IsolationForest(
                n_estimators=300,
                contamination=contamination,
                random_state=RANDOM_STATE,
                n_jobs=-1,
            )
            isolation.fit(X)
            isolation_score = -isolation.decision_function(X)

            lof = LocalOutlierFactor(n_neighbors=35, contamination=contamination)
            lof.fit_predict(X)
            lof_score = -lof.negative_outlier_factor_
            """
        ),
        md("## 6. Evaluate rankings after fitting"),
        code(
            """
            y = data["hidden_label"].to_numpy()
            k = max(1, int(y.sum()))
            rows = []
            for name, scores in {"Isolation Forest": isolation_score, "Local Outlier Factor": lof_score}.items():
                top_k = np.argsort(scores)[-k:]
                rows.append({
                    "model": name,
                    "roc_auc": roc_auc_score(y, scores),
                    "average_precision": average_precision_score(y, scores),
                    "precision_at_k": y[top_k].mean(),
                    "alert_rate": k / len(y),
                })
            evaluation = pd.DataFrame(rows).sort_values("average_precision", ascending=False)
            display(evaluation.round(4))
            best_name = evaluation.iloc[0]["model"]
            best_score = isolation_score if best_name == "Isolation Forest" else lof_score
            data["anomaly_score"] = best_score
            data["flagged"] = False
            data.loc[np.argsort(best_score)[-k:], "flagged"] = True
            """
        ),
        md("## 7. Score diagnostics"),
        code(
            """
            sns.histplot(data=data, x="anomaly_score", hue="hidden_label", bins=45, element="step", stat="density", common_norm=False)
            plt.title("Anomaly score distribution; labels shown only for evaluation")
            plt.tight_layout()
            """
        ),
        md("## 8. Inspect the highest-risk observations"),
        code(
            """
            display(data.sort_values("anomaly_score", ascending=False).head(15).round(3))
            """
        ),
        md("## 9. Key findings\n\nPrecision at k is often more operationally useful than a default anomaly threshold because review teams have finite capacity."),
        *ending(project),
    ]


def basket_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup("from collections import Counter\nfrom itertools import combinations"),
        md("## 2. Generate transparent transaction baskets"),
        code(
            """
            bundles = [
                ["coffee", "milk", "sugar"],
                ["bread", "butter", "jam"],
                ["pasta", "tomato_sauce", "cheese"],
                ["diapers", "wipes", "baby_lotion"],
                ["chips", "salsa", "soft_drink"],
            ]
            catalogue = sorted(set(item for bundle in bundles for item in bundle) | {"eggs", "tea", "rice", "soap"})
            transactions = []
            for _ in range(650):
                basket = set(bundles[rng.integers(0, len(bundles))])
                basket = {item for item in basket if rng.random() > 0.12}
                if rng.random() < 0.45:
                    basket.add(rng.choice(catalogue))
                transactions.append(sorted(basket))
            display(pd.DataFrame({"transaction": transactions}).head())
            """
        ),
        md("## 3. Basket quality and size"),
        code(
            """
            basket_sizes = pd.Series([len(basket) for basket in transactions])
            display(basket_sizes.describe().to_frame("basket_size"))
            sns.histplot(basket_sizes, discrete=True)
            plt.title("Basket-size distribution")
            plt.tight_layout()
            """
        ),
        md("## 4. Frequent item support"),
        code(
            """
            n_transactions = len(transactions)
            item_counts = Counter(item for basket in transactions for item in set(basket))
            item_support = pd.Series({item: count / n_transactions for item, count in item_counts.items()}).sort_values(ascending=False)
            display(item_support.head(15).to_frame("support"))
            """
        ),
        md("## 5. Pair support and association rules"),
        code(
            """
            pair_counts = Counter(
                pair
                for basket in transactions
                for pair in combinations(sorted(set(basket)), 2)
            )
            rules = []
            for (left, right), count in pair_counts.items():
                pair_support = count / n_transactions
                for antecedent, consequent in [(left, right), (right, left)]:
                    confidence = pair_support / item_support[antecedent]
                    lift = confidence / item_support[consequent]
                    rules.append({
                        "antecedent": antecedent,
                        "consequent": consequent,
                        "support": pair_support,
                        "confidence": confidence,
                        "lift": lift,
                    })
            rules = pd.DataFrame(rules)
            useful_rules = rules.query("support >= 0.04 and confidence >= 0.25 and lift > 1.05").sort_values(
                ["lift", "confidence"], ascending=False
            )
            display(useful_rules.head(20).round(3))
            """
        ),
        md("## 6. Rule quality checks"),
        code(
            """
            coverage = useful_rules["antecedent"].nunique() / len(catalogue)
            display(pd.Series({
                "candidate_rules": len(rules),
                "useful_rules": len(useful_rules),
                "antecedent_catalogue_coverage": coverage,
                "median_useful_lift": useful_rules["lift"].median(),
            }).to_frame("value"))
            """
        ),
        md("## 7. Visualise the strongest rules"),
        code(
            """
            plot_rules = useful_rules.head(15).copy()
            plot_rules["rule"] = plot_rules["antecedent"] + " → " + plot_rules["consequent"]
            sns.barplot(data=plot_rules, x="lift", y="rule", hue="confidence", palette="Blues", legend=False)
            plt.title("Strongest association rules")
            plt.tight_layout()
            """
        ),
        md("## 8. Business-ready rule table"),
        code(
            """
            display(useful_rules.assign(
                recommendation=lambda frame: "Place " + frame["consequent"] + " near " + frame["antecedent"]
            ).head(12))
            """
        ),
        md("## 9. Key findings\n\nLift guards against recommending an already-popular item solely because it appears in many baskets."),
        *ending(project),
    ]


def audio_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.decomposition import PCA\n"
            "from sklearn.metrics import adjusted_rand_score, davies_bouldin_score, silhouette_score\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Spotify-style audio features"),
        code(
            """
            features = ["danceability", "energy", "acousticness", "instrumentalness", "valence", "tempo"]
            genre_profiles = {
                "acoustic": [0.42, 0.30, 0.82, 0.25, 0.48, 92],
                "dance": [0.83, 0.82, 0.10, 0.05, 0.72, 126],
                "hip_hop": [0.76, 0.70, 0.16, 0.03, 0.58, 101],
                "rock": [0.52, 0.88, 0.08, 0.08, 0.55, 134],
                "ambient": [0.28, 0.25, 0.68, 0.86, 0.34, 78],
            }
            rows = []
            for genre, profile in genre_profiles.items():
                values = rng.normal(profile, [0.08, 0.08, 0.09, 0.08, 0.10, 8], size=(150, 6))
                frame = pd.DataFrame(values, columns=features)
                frame[features[:-1]] = frame[features[:-1]].clip(0, 1)
                frame["tempo"] = frame["tempo"].clip(50, 210)
                frame["hidden_genre"] = genre
                rows.append(frame)
            tracks = pd.concat(rows, ignore_index=True).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
            tracks["track_name"] = [f"Track {i + 1:04d}" for i in range(len(tracks))]
            display(tracks.head())
            """
        ),
        md("## 3. Feature quality and distribution"),
        code(
            """
            display(tracks[features].describe().T)
            tracks[features].hist(figsize=(12, 7), bins=25)
            plt.tight_layout()
            """
        ),
        md("## 4. Scale features and select k"),
        code(
            """
            X = StandardScaler().fit_transform(tracks[features])
            rows = []
            for k in range(2, 9):
                labels = KMeans(n_clusters=k, n_init=25, random_state=RANDOM_STATE).fit_predict(X)
                rows.append({
                    "k": k,
                    "silhouette": silhouette_score(X, labels),
                    "davies_bouldin": davies_bouldin_score(X, labels),
                })
            scores = pd.DataFrame(rows)
            display(scores.round(3))
            best_k = int(scores.sort_values(["silhouette", "davies_bouldin"], ascending=[False, True]).iloc[0]["k"])
            model = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE)
            tracks["cluster"] = model.fit_predict(X)
            """
        ),
        md("## 5. Evaluate cluster structure"),
        code(
            """
            genre_codes = tracks["hidden_genre"].astype("category").cat.codes
            display(pd.Series({
                "selected_k": best_k,
                "silhouette": silhouette_score(X, tracks["cluster"]),
                "davies_bouldin": davies_bouldin_score(X, tracks["cluster"]),
                "adjusted_rand_vs_hidden_genre": adjusted_rand_score(genre_codes, tracks["cluster"]),
            }).to_frame("value"))
            """
        ),
        md("## 6. Cluster profiles"),
        code(
            """
            profile = tracks.groupby("cluster")[features].mean()
            display(profile.round(3))
            sns.heatmap(profile[features[:-1]], cmap="vlag", center=0.5)
            plt.title("Audio feature profiles")
            plt.tight_layout()
            """
        ),
        md("## 7. Playlist discovery view"),
        code(
            """
            projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
            sns.scatterplot(x=projection[:, 0], y=projection[:, 1], hue=tracks["cluster"], palette="tab10", alpha=0.65)
            plt.title("Track clusters in PCA space")
            plt.tight_layout()
            """
        ),
        md("## 8. Sample playlist seeds"),
        code(
            """
            playlist_seeds = tracks.groupby("cluster", group_keys=False).apply(
                lambda frame: frame.sample(min(5, len(frame)), random_state=RANDOM_STATE)
            )[["cluster", "track_name", "hidden_genre", *features]]
            display(playlist_seeds)
            """
        ),
        md("## 9. Key findings\n\nProfile clusters by audio features before assigning playlist names; hidden genres are used only to audit the demonstration."),
        *ending(project),
    ]


def netflix_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.feature_extraction.text import TfidfVectorizer\n"
            "from sklearn.metrics import silhouette_score\n"
            "from sklearn.neighbors import NearestNeighbors"
        ),
        md("## 2. Streaming catalogue"),
        code(
            """
            themes = {
                "crime": ["detective investigates a hidden criminal network", "forensic team solves a city mystery", "heist crew faces an impossible case"],
                "science_fiction": ["space crew explores an unknown planet", "engineer builds an artificial intelligence", "time travel changes a future colony"],
                "romance": ["two strangers build a relationship in the city", "family expectations challenge a young couple", "friends discover love during a journey"],
                "documentary": ["researchers explain climate and natural systems", "true story follows technology and society", "experts examine history through archives"],
                "comedy": ["friends navigate work and chaotic daily life", "family trip creates a chain of comic mistakes", "unlikely roommates start a ridiculous business"],
            }
            rows = []
            for theme, descriptions in themes.items():
                for i in range(24):
                    rows.append({
                        "title": f"{theme.replace('_', ' ').title()} {i + 1:02d}",
                        "description": rng.choice(descriptions),
                        "genre": theme,
                        "type": rng.choice(["Movie", "TV Show"]),
                        "release_year": int(rng.integers(2000, 2026)),
                    })
            catalogue = pd.DataFrame(rows)
            catalogue["text"] = catalogue["genre"].str.replace("_", " ") + " " + catalogue["description"]
            display(catalogue.head())
            """
        ),
        md("## 3. Catalogue quality and coverage"),
        code(
            """
            display(pd.Series({
                "titles": len(catalogue),
                "genres": catalogue["genre"].nunique(),
                "duplicate_titles": catalogue["title"].duplicated().sum(),
                "missing_descriptions": catalogue["description"].isna().sum(),
            }).to_frame("value"))
            """
        ),
        md("## 4. TF-IDF representation"),
        code(
            """
            vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=2)
            X = vectorizer.fit_transform(catalogue["text"])
            """
        ),
        md("## 5. Content clustering"),
        code(
            """
            rows = []
            for k in range(3, 9):
                labels = KMeans(n_clusters=k, n_init=25, random_state=RANDOM_STATE).fit_predict(X)
                rows.append({"k": k, "silhouette": silhouette_score(X, labels)})
            scores = pd.DataFrame(rows)
            best_k = int(scores.loc[scores["silhouette"].idxmax(), "k"])
            model = KMeans(n_clusters=best_k, n_init=40, random_state=RANDOM_STATE)
            catalogue["cluster"] = model.fit_predict(X)
            display(scores.round(3))
            """
        ),
        md("## 6. Similar-title retrieval"),
        code(
            """
            neighbours = NearestNeighbors(metric="cosine", n_neighbors=7).fit(X)

            def similar_titles(title, n=6):
                index = catalogue.index[catalogue["title"].eq(title)][0]
                distances, indices = neighbours.kneighbors(X[index], n_neighbors=n + 1)
                result = catalogue.loc[indices[0][1:], ["title", "genre", "type", "cluster"]].copy()
                result["similarity"] = 1 - distances[0][1:]
                return result

            seed_title = catalogue.iloc[0]["title"]
            recommendations = similar_titles(seed_title)
            print("Seed:", seed_title)
            display(recommendations)
            """
        ),
        md("## 7. Evaluate neighbour relevance"),
        code(
            """
            seed_genre = catalogue.iloc[0]["genre"]
            same_genre_rate = recommendations["genre"].eq(seed_genre).mean()
            display(pd.Series({
                "cluster_silhouette": silhouette_score(X, catalogue["cluster"]),
                "top_6_same_genre_rate": same_genre_rate,
                "mean_top_6_similarity": recommendations["similarity"].mean(),
            }).to_frame("value"))
            """
        ),
        md("## 8. Cluster profiles"),
        code(
            """
            profile = pd.crosstab(catalogue["cluster"], catalogue["genre"], normalize="index")
            sns.heatmap(profile, cmap="Blues", annot=True, fmt=".2f")
            plt.title("Genre composition by content cluster")
            plt.tight_layout()
            """
        ),
        md("## 9. Key findings\n\nContent similarity is explainable and cold-start friendly, but it should be combined with behavioural feedback for production ranking."),
        *ending(project),
    ]


def topic_cells(project: Project, reviews: bool) -> list[dict]:
    if reviews:
        themes = {
            "delivery": ["package arrived late", "delivery tracking was unclear", "courier arrived early", "shipping box was damaged"],
            "quality": ["material feels durable", "product stopped working", "build quality is excellent", "item looks cheaper than expected"],
            "pricing": ["price is fair for value", "discount made the purchase worthwhile", "cost is too high", "better value exists elsewhere"],
            "support": ["support solved the issue quickly", "agent did not understand the problem", "refund process was smooth", "response took several days"],
            "usability": ["setup was simple", "interface is confusing", "instructions were clear", "daily use feels intuitive"],
        }
    else:
        themes = {
            "artificial_intelligence": ["new model improves reasoning", "researchers evaluate machine learning safety", "companies adopt generative AI tools", "chip demand grows for data centres"],
            "finance": ["central bank discusses interest rates", "markets react to inflation data", "investors review quarterly earnings", "currency volatility affects trade"],
            "health": ["clinical study tests a new treatment", "public health team tracks disease patterns", "hospital adopts digital diagnostics", "research links sleep and wellbeing"],
            "climate": ["cities prepare for extreme heat", "renewable energy capacity expands", "scientists monitor ocean temperatures", "policy targets industrial emissions"],
            "sport": ["team wins after a late comeback", "coach changes the starting lineup", "tournament reaches the final round", "athlete breaks a national record"],
        }
    return [
        md("## 1. Project setup"),
        setup("from sklearn.decomposition import NMF\nfrom sklearn.feature_extraction.text import TfidfVectorizer"),
        md("## 2. Build an auditable demonstration corpus"),
        code(
            f"""
            themes = {themes!r}
            documents = []
            hidden_theme = []
            for theme, phrases in themes.items():
                for _ in range(28):
                    selected = rng.choice(phrases, size=3, replace=True)
                    documents.append(". ".join(selected))
                    hidden_theme.append(theme)
            corpus = pd.DataFrame({{"document": documents, "hidden_theme": hidden_theme}}).sample(
                frac=1, random_state=RANDOM_STATE
            ).reset_index(drop=True)
            display(corpus.head())
            """
        ),
        md("## 3. Corpus quality"),
        code(
            """
            corpus["word_count"] = corpus["document"].str.split().str.len()
            display(corpus["word_count"].describe().to_frame())
            print("Duplicate documents:", int(corpus["document"].duplicated().sum()))
            """
        ),
        md("## 4. TF-IDF features"),
        code(
            """
            vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=3, max_df=0.95)
            X = vectorizer.fit_transform(corpus["document"])
            print("Document-term matrix:", X.shape)
            """
        ),
        md("## 5. Fit NMF topics"),
        code(
            """
            n_topics = 5
            model = NMF(n_components=n_topics, init="nndsvda", random_state=RANDOM_STATE, max_iter=600)
            document_topics = model.fit_transform(X)
            terms = np.array(vectorizer.get_feature_names_out())
            topic_terms = {}
            for topic_id, weights in enumerate(model.components_):
                topic_terms[topic_id] = list(terms[np.argsort(weights)[-8:][::-1]])
            display(pd.DataFrame.from_dict(topic_terms, orient="index"))
            corpus["topic"] = document_topics.argmax(axis=1)
            corpus["topic_strength"] = document_topics.max(axis=1)
            """
        ),
        md("## 6. Topic quality diagnostics"),
        code(
            """
            flattened_terms = [term for words in topic_terms.values() for term in words]
            topic_diversity = len(set(flattened_terms)) / len(flattened_terms)
            concentration = corpus["topic_strength"].mean()
            display(pd.Series({
                "reconstruction_error": model.reconstruction_err_,
                "topic_diversity": topic_diversity,
                "mean_topic_strength": concentration,
            }).to_frame("value"))
            """
        ),
        md("## 7. Topic prevalence"),
        code(
            """
            prevalence = corpus["topic"].value_counts(normalize=True).sort_index()
            prevalence.plot.bar(color="#2563eb")
            plt.title("Topic prevalence")
            plt.ylabel("Share of documents")
            plt.tight_layout()
            """
        ),
        md("## 8. Inspect representative documents"),
        code(
            """
            representatives = corpus.sort_values("topic_strength", ascending=False).groupby("topic").head(3)
            display(representatives[["topic", "topic_strength", "document", "hidden_theme"]])
            """
        ),
        md("## 9. Key findings\n\nTopic labels should be assigned from top terms and representative documents, not from arbitrary topic numbers."),
        *ending(project),
    ]


def semantic_cells(project: Project, resume: bool) -> list[dict]:
    if resume:
        corpus_code = """
            resumes = {
                "Data Scientist": "python machine learning statistics experimentation feature engineering model deployment",
                "Data Analyst": "sql power bi dashboards excel stakeholder reporting data visualisation",
                "Data Engineer": "spark databricks pipelines orchestration lakehouse sql cloud",
                "ML Engineer": "python mlops model serving docker kubernetes monitoring feature store",
                "NLP Engineer": "transformers text classification embeddings retrieval evaluation python",
                "Cloud Engineer": "azure networking infrastructure terraform security devops automation",
            }
            jobs = {
                "Senior Data Scientist": "machine learning experimentation python statistics forecasting deployment",
                "BI Data Analyst": "power bi sql dashboards stakeholder insights excel",
                "Databricks Data Engineer": "spark databricks lakehouse orchestration pipelines sql",
                "Production ML Engineer": "mlops kubernetes model serving monitoring python docker",
                "Search NLP Engineer": "text embeddings retrieval transformers evaluation python",
                "Azure Platform Engineer": "azure terraform networking security devops infrastructure",
            }
            source_names, source_texts = list(resumes), list(resumes.values())
            target_names, target_texts = list(jobs), list(jobs.values())
            query_label = "resume"
        """
    else:
        corpus_code = """
            documents = {
                "Lakehouse": "databricks lakehouse delta tables governance batch streaming",
                "Feature Store": "machine learning features reuse training serving consistency",
                "RAG Evaluation": "retrieval relevance faithfulness context precision evaluation",
                "Power BI": "semantic model dax dashboards visual analytics business",
                "Time Series": "forecasting seasonality trend lag rolling validation",
                "MLOps": "model registry deployment monitoring drift ci cd automation",
                "Vector Search": "embeddings nearest neighbour semantic retrieval index",
                "Data Quality": "schema validation completeness duplicates lineage observability",
                "Experimentation": "ab testing hypothesis power sample significance metrics",
                "Clustering": "unsupervised segmentation similarity silhouette profiles",
                "Anomaly Detection": "outlier isolation forest rare events ranking alerts",
                "SQL Analytics": "joins windows aggregations query optimisation warehouse",
            }
            source_names, source_texts = list(documents), list(documents.values())
            target_names, target_texts = source_names, source_texts
            query_label = "document"
        """
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.decomposition import TruncatedSVD\n"
            "from sklearn.feature_extraction.text import TfidfVectorizer\n"
            "from sklearn.metrics.pairwise import cosine_similarity\n"
            "from sklearn.preprocessing import Normalizer"
        ),
        md("## 2. Curated, privacy-safe text corpus"),
        code(corpus_code),
        md("## 3. Corpus quality"),
        code(
            """
            quality = pd.DataFrame({
                "name": source_names + target_names,
                "text": source_texts + target_texts,
            })
            quality["tokens"] = quality["text"].str.split().str.len()
            display(quality)
            """
        ),
        md("## 4. TF-IDF representation"),
        code(
            """
            all_texts = source_texts + target_texts
            vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
            X = vectorizer.fit_transform(all_texts)
            n_components = min(8, X.shape[0] - 1, X.shape[1] - 1)
            svd = TruncatedSVD(n_components=n_components, random_state=RANDOM_STATE)
            latent = Normalizer().fit_transform(svd.fit_transform(X))
            source_vectors = latent[: len(source_texts)]
            target_vectors = latent[len(source_texts):]
            similarity = cosine_similarity(source_vectors, target_vectors)
            """
        ),
        md("## 5. Rank semantic matches"),
        code(
            """
            rows = []
            for source_index, source_name in enumerate(source_names):
                order = np.argsort(similarity[source_index])[::-1]
                for rank, target_index in enumerate(order[:3], start=1):
                    rows.append({
                        query_label: source_name,
                        "rank": rank,
                        "match": target_names[target_index],
                        "score": similarity[source_index, target_index],
                    })
            ranking = pd.DataFrame(rows)
            display(ranking.round(3))
            """
        ),
        md("## 6. Ranking diagnostics"),
        code(
            """
            top_scores = ranking.query("rank == 1")["score"].to_numpy()
            second_scores = ranking.query("rank == 2")["score"].to_numpy()
            display(pd.Series({
                "explained_variance": svd.explained_variance_ratio_.sum(),
                "mean_top_score": top_scores.mean(),
                "mean_top_vs_second_margin": (top_scores - second_scores).mean(),
            }).to_frame("value"))
            """
        ),
        md("## 7. Similarity heatmap"),
        code(
            """
            sns.heatmap(
                pd.DataFrame(similarity, index=source_names, columns=target_names),
                cmap="Blues",
                annot=True,
                fmt=".2f",
            )
            plt.title("Latent semantic similarity")
            plt.tight_layout()
            """
        ),
        md("## 8. Explain a match with overlapping terms"),
        code(
            """
            source_index = 0
            target_index = int(np.argmax(similarity[source_index]))
            source_terms = set(source_texts[source_index].split())
            target_terms = set(target_texts[target_index].split())
            display(pd.Series({
                "query": source_names[source_index],
                "best_match": target_names[target_index],
                "shared_terms": ", ".join(sorted(source_terms & target_terms)),
            }).to_frame("value"))
            """
        ),
        md("## 9. Key findings\n\nSimilarity scores support ranking, not hiring or access decisions. Human review and bias checks remain essential."),
        *ending(project),
    ]


def image_cells(project: Project, palette: bool) -> list[dict]:
    if palette:
        data_code = """
            height, width = 120, 240
            image = np.ones((height, width, 3), dtype=float)
            colours = np.array([
                [0.03, 0.22, 0.45],
                [0.00, 0.55, 0.75],
                [0.98, 0.45, 0.12],
                [0.95, 0.80, 0.18],
                [0.12, 0.68, 0.42],
                [0.92, 0.94, 0.97],
            ])
            boundaries = [0, 55, 100, 145, 185, 215, 240]
            for colour, left, right in zip(colours, boundaries[:-1], boundaries[1:]):
                image[:, left:right] = colour
            image = np.clip(image + rng.normal(0, 0.018, image.shape), 0, 1)
            n_colours = 6
        """
    else:
        data_code = """
            height, width = 128, 128
            y, x = np.mgrid[0:height, 0:width]
            image = np.zeros((height, width, 3), dtype=float)
            image[..., 0] = x / width
            image[..., 1] = y / height
            image[..., 2] = 0.35 + 0.25 * np.sin(x / 10)
            circle = (x - 42) ** 2 + (y - 48) ** 2 < 24 ** 2
            image[circle] = [0.96, 0.38, 0.16]
            image[78:112, 68:116] = [0.08, 0.62, 0.78]
            image = np.clip(image + rng.normal(0, 0.025, image.shape), 0, 1)
            n_colours = 12
        """
    return [
        md("## 1. Project setup"),
        setup("from sklearn.cluster import MiniBatchKMeans\nfrom sklearn.metrics import mean_squared_error"),
        md("## 2. Generate an owned demonstration image"),
        code(clean(data_code) + "\n\nplt.imshow(image)\nplt.axis('off')\nplt.title('Original demonstration image')\nplt.tight_layout()"),
        md("## 3. Pixel quality checks"),
        code(
            """
            pixels = image.reshape(-1, 3)
            display(pd.DataFrame(pixels, columns=["red", "green", "blue"]).describe().T)
            print("Image shape:", image.shape)
            print("Pixel range:", float(pixels.min()), "to", float(pixels.max()))
            """
        ),
        md("## 4. Learn the colour palette"),
        code(
            """
            sample_size = min(12000, len(pixels))
            sample = pixels[rng.choice(len(pixels), size=sample_size, replace=False)]
            model = MiniBatchKMeans(
                n_clusters=n_colours,
                n_init=20,
                batch_size=2048,
                random_state=RANDOM_STATE,
            ).fit(sample)
            labels = model.predict(pixels)
            palette_values = np.clip(model.cluster_centers_, 0, 1)
            reconstructed = palette_values[labels].reshape(image.shape)
            """
        ),
        md("## 5. Quantisation quality"),
        code(
            """
            mse = mean_squared_error(pixels, reconstructed.reshape(-1, 3))
            psnr = 20 * np.log10(1.0 / np.sqrt(max(mse, 1e-12)))
            proportions = pd.Series(labels).value_counts(normalize=True).sort_index()
            display(pd.Series({
                "palette_colours": n_colours,
                "mse": mse,
                "psnr_db": psnr,
                "largest_colour_share": proportions.max(),
            }).to_frame("value"))
            """
        ),
        md("## 6. Compare original and quantised images"),
        code(
            """
            fig, axes = plt.subplots(1, 2, figsize=(12, 5))
            axes[0].imshow(image)
            axes[0].set_title("Original")
            axes[1].imshow(reconstructed)
            axes[1].set_title(f"Quantised to {n_colours} colours")
            for axis in axes:
                axis.axis("off")
            plt.tight_layout()
            """
        ),
        md("## 7. Palette with proportions"),
        code(
            """
            order = proportions.sort_values(ascending=False).index
            palette_table = pd.DataFrame(palette_values[order], columns=["red", "green", "blue"])
            palette_table["share"] = proportions.loc[order].to_numpy()
            palette_table["hex"] = [
                "#{:02X}{:02X}{:02X}".format(*(np.rint(rgb * 255).astype(int)))
                for rgb in palette_values[order]
            ]
            display(palette_table.round(3))
            fig, ax = plt.subplots(figsize=(10, 2))
            left = 0
            for rgb, share in zip(palette_values[order], proportions.loc[order]):
                ax.barh([0], [share], left=left, color=rgb, height=0.7)
                left += share
            ax.set_xlim(0, 1)
            ax.set_yticks([])
            ax.set_title("Learned palette and visual share")
            plt.tight_layout()
            """
        ),
        md("## 8. Storage interpretation"),
        code(
            """
            original_bits = image.size * 8
            label_bits = len(pixels) * np.ceil(np.log2(n_colours))
            palette_bits = n_colours * 3 * 8
            display(pd.Series({
                "original_rgb_bits": original_bits,
                "approx_quantised_bits": label_bits + palette_bits,
                "approx_compression_ratio": original_bits / (label_bits + palette_bits),
            }).to_frame("value"))
            """
        ),
        md("## 9. Key findings\n\nChoose palette size from the quality-storage trade-off and always evaluate on the actual asset type."),
        *ending(project),
    ]


def digits_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.datasets import load_digits\n"
            "from sklearn.decomposition import PCA\n"
            "from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Load handwritten digit pixels"),
        code(
            """
            digits = load_digits()
            X_raw = digits.data
            hidden_labels = digits.target
            print("Samples:", X_raw.shape[0], "Features:", X_raw.shape[1])
            """
        ),
        md("## 3. Pixel quality and examples"),
        code(
            """
            print("Missing values:", int(np.isnan(X_raw).sum()))
            fig, axes = plt.subplots(2, 6, figsize=(10, 4))
            for axis, image in zip(axes.flat, digits.images[:12]):
                axis.imshow(image, cmap="gray_r")
                axis.axis("off")
            plt.tight_layout()
            """
        ),
        md("## 4. Scale and reduce dimensions"),
        code(
            """
            X_scaled = StandardScaler().fit_transform(X_raw)
            pca = PCA(n_components=0.90, random_state=RANDOM_STATE)
            X = pca.fit_transform(X_scaled)
            print("Components retaining 90% variance:", X.shape[1])
            """
        ),
        md("## 5. Cluster the digits"),
        code(
            """
            model = KMeans(n_clusters=10, n_init=50, random_state=RANDOM_STATE)
            clusters = model.fit_predict(X)
            """
        ),
        md("## 6. Evaluate structure; labels were not used for fitting"),
        code(
            """
            contingency = pd.crosstab(pd.Series(clusters, name="cluster"), pd.Series(hidden_labels, name="digit"))
            purity = contingency.max(axis=1).sum() / contingency.to_numpy().sum()
            display(pd.Series({
                "silhouette": silhouette_score(X, clusters),
                "adjusted_rand_index": adjusted_rand_score(hidden_labels, clusters),
                "normalized_mutual_information": normalized_mutual_info_score(hidden_labels, clusters),
                "cluster_purity": purity,
            }).to_frame("value"))
            """
        ),
        md("## 7. Cluster-to-digit diagnostic"),
        code(
            """
            sns.heatmap(contingency, cmap="Blues")
            plt.title("Cluster composition by hidden digit label")
            plt.tight_layout()
            """
        ),
        md("## 8. PCA projection"),
        code(
            """
            projection = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X_scaled)
            sns.scatterplot(x=projection[:, 0], y=projection[:, 1], hue=clusters, palette="tab10", s=20, legend=False)
            plt.title("Digit clusters in two-dimensional PCA space")
            plt.tight_layout()
            """
        ),
        md("## 9. Key findings\n\nVisual similarity does not map perfectly to digit identity; confusion between similarly shaped digits is expected."),
        *ending(project),
    ]


def geo_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup("from sklearn.cluster import DBSCAN\nfrom sklearn.metrics import silhouette_score"),
        md("## 2. Privacy-safe delivery coordinates"),
        code(
            """
            centres = np.array([
                [17.3850, 78.4867],
                [17.4435, 78.3772],
                [17.4483, 78.3915],
                [17.4933, 78.3995],
            ])
            rows = []
            for centre_id, centre in enumerate(centres):
                points = rng.normal(centre, [0.006, 0.007], size=(180, 2))
                frame = pd.DataFrame(points, columns=["latitude", "longitude"])
                frame["hidden_centre"] = centre_id
                rows.append(frame)
            noise = pd.DataFrame({
                "latitude": rng.uniform(17.30, 17.56, 70),
                "longitude": rng.uniform(78.30, 78.58, 70),
                "hidden_centre": -1,
            })
            deliveries = pd.concat([*rows, noise], ignore_index=True).sample(frac=1, random_state=RANDOM_STATE).reset_index(drop=True)
            display(deliveries.head())
            """
        ),
        md("## 3. Coordinate quality"),
        code(
            """
            display(deliveries[["latitude", "longitude"]].describe().T)
            print("Duplicate coordinates:", int(deliveries.duplicated(["latitude", "longitude"]).sum()))
            """
        ),
        md("## 4. Haversine DBSCAN"),
        code(
            """
            earth_radius_km = 6371.0088
            coordinates_radians = np.radians(deliveries[["latitude", "longitude"]])
            epsilon_km = 1.6
            model = DBSCAN(
                eps=epsilon_km / earth_radius_km,
                min_samples=14,
                metric="haversine",
            )
            deliveries["cluster"] = model.fit_predict(coordinates_radians)
            """
        ),
        md("## 5. Hotspot quality"),
        code(
            """
            non_noise = deliveries["cluster"] >= 0
            cluster_count = deliveries.loc[non_noise, "cluster"].nunique()
            score = silhouette_score(
                deliveries.loc[non_noise, ["latitude", "longitude"]],
                deliveries.loc[non_noise, "cluster"],
            ) if cluster_count > 1 else np.nan
            display(pd.Series({
                "hotspots": cluster_count,
                "noise_rate": 1 - non_noise.mean(),
                "non_noise_silhouette": score,
            }).to_frame("value"))
            """
        ),
        md("## 6. Hotspot profiles"),
        code(
            """
            hotspots = deliveries.query("cluster >= 0").groupby("cluster").agg(
                deliveries=("cluster", "size"),
                centre_latitude=("latitude", "mean"),
                centre_longitude=("longitude", "mean"),
            ).sort_values("deliveries", ascending=False)
            display(hotspots.round(5))
            """
        ),
        md("## 7. Map-like scatter plot"),
        code(
            """
            sns.scatterplot(
                data=deliveries,
                x="longitude",
                y="latitude",
                hue="cluster",
                palette="tab10",
                s=28,
                alpha=0.75,
            )
            plt.title("Delivery hotspots; cluster -1 is noise")
            plt.tight_layout()
            """
        ),
        md("## 8. Operational prioritisation"),
        code(
            """
            hotspots["share_of_all_deliveries"] = hotspots["deliveries"] / len(deliveries)
            display(hotspots.head(10).round(4))
            """
        ),
        md("## 9. Key findings\n\nEpsilon is a business and geographic choice: calibrate it in kilometres and test stability across time windows."),
        *ending(project),
    ]


def regime_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.metrics import adjusted_rand_score, silhouette_score\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Generate chronological market regimes"),
        code(
            """
            n = 1500
            transition = np.array([[0.95, 0.04, 0.01], [0.05, 0.90, 0.05], [0.04, 0.10, 0.86]])
            regimes = np.zeros(n, dtype=int)
            for i in range(1, n):
                regimes[i] = rng.choice(3, p=transition[regimes[i - 1]])
            means = np.array([0.0003, 0.0015, -0.0020])
            volatilities = np.array([0.012, 0.025, 0.055])
            returns = rng.normal(means[regimes], volatilities[regimes])
            price = 25000 * np.exp(np.cumsum(returns))
            volume = rng.lognormal(12 + regimes * 0.35, 0.45)
            market = pd.DataFrame({
                "date": pd.date_range("2021-01-01", periods=n, freq="D"),
                "price": price,
                "return": returns,
                "volume": volume,
                "hidden_regime": regimes,
            })
            market["volatility_14d"] = market["return"].rolling(14).std()
            market["momentum_14d"] = market["price"].pct_change(14)
            market["volume_change"] = market["volume"].pct_change().clip(-5, 5)
            market = market.dropna().reset_index(drop=True)
            feature_names = ["return", "volatility_14d", "momentum_14d", "volume_change"]
            display(market.head())
            """
        ),
        md("## 3. Market feature quality"),
        code(
            """
            display(market[feature_names].describe().T)
            print("Missing cells:", int(market[feature_names].isna().sum().sum()))
            """
        ),
        md("## 4. Scale rolling features"),
        code(
            """
            X = StandardScaler().fit_transform(market[feature_names])
            """
        ),
        md("## 5. Select and fit market clusters"),
        code(
            """
            rows = []
            for k in range(2, 7):
                labels = KMeans(n_clusters=k, n_init=30, random_state=RANDOM_STATE).fit_predict(X)
                rows.append({"k": k, "silhouette": silhouette_score(X, labels)})
            scores = pd.DataFrame(rows)
            best_k = int(scores.loc[scores["silhouette"].idxmax(), "k"])
            market["cluster"] = KMeans(n_clusters=best_k, n_init=50, random_state=RANDOM_STATE).fit_predict(X)
            display(scores.round(3))
            """
        ),
        md("## 6. Regime diagnostics"),
        code(
            """
            display(pd.Series({
                "selected_k": best_k,
                "silhouette": silhouette_score(X, market["cluster"]),
                "adjusted_rand_vs_hidden_regime": adjusted_rand_score(market["hidden_regime"], market["cluster"]),
                "cluster_transitions": int(market["cluster"].diff().ne(0).sum() - 1),
            }).to_frame("value"))
            """
        ),
        md("## 7. Cluster profiles"),
        code(
            """
            profile = market.groupby("cluster")[feature_names].mean()
            profile["days"] = market.groupby("cluster").size()
            display(profile.round(4))
            """
        ),
        md("## 8. Chronological regime view"),
        code(
            """
            sns.scatterplot(data=market, x="date", y="price", hue="cluster", palette="tab10", s=18)
            plt.yscale("log")
            plt.title("Detected crypto market regimes")
            plt.tight_layout()
            """
        ),
        md("## 9. Key findings\n\nClusters describe recurring behaviour; they do not forecast returns and must not be treated as trading advice."),
        *ending(project),
    ]


def asset_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from scipy.cluster.hierarchy import dendrogram, linkage, fcluster\n"
            "from sklearn.metrics import silhouette_score\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Multi-factor asset-return simulation"),
        code(
            """
            sectors = ["technology", "finance", "health", "energy", "consumer", "industrial"]
            assets = [f"{sector[:3].upper()}_{i + 1}" for sector in sectors for i in range(4)]
            days = 756
            market_factor = rng.normal(0.0003, 0.009, days)
            sector_factors = {sector: rng.normal(0.0001, 0.011, days) for sector in sectors}
            returns = {}
            asset_sector = {}
            for asset, sector in zip(assets, np.repeat(sectors, 4)):
                beta = rng.uniform(0.7, 1.3)
                sector_loading = rng.uniform(0.7, 1.2)
                returns[asset] = beta * market_factor + sector_loading * sector_factors[sector] + rng.normal(0, 0.008, days)
                asset_sector[asset] = sector
            returns = pd.DataFrame(returns, index=pd.date_range("2023-01-01", periods=days, freq="B"))
            display(returns.head())
            """
        ),
        md("## 3. Return quality and summary"),
        code(
            """
            print("Missing cells:", int(returns.isna().sum().sum()))
            summary = pd.DataFrame({
                "annual_return": returns.mean() * 252,
                "annual_volatility": returns.std() * np.sqrt(252),
                "downside_volatility": returns.clip(upper=0).std() * np.sqrt(252),
                "market_correlation": returns.corrwith(pd.Series(market_factor, index=returns.index)),
            })
            summary["sharpe_proxy"] = summary["annual_return"] / summary["annual_volatility"]
            display(summary.round(3))
            """
        ),
        md("## 4. Correlation-aware asset features"),
        code(
            """
            correlation = returns.corr()
            correlation_features = correlation.add_prefix("corr_")
            features = summary.join(correlation_features)
            X = StandardScaler().fit_transform(features)
            """
        ),
        md("## 5. Hierarchical asset clustering"),
        code(
            """
            linkage_matrix = linkage(X, method="ward")
            candidate_rows = []
            for k in range(3, 9):
                labels = fcluster(linkage_matrix, t=k, criterion="maxclust")
                candidate_rows.append({"k": k, "silhouette": silhouette_score(X, labels)})
            scores = pd.DataFrame(candidate_rows)
            best_k = int(scores.loc[scores["silhouette"].idxmax(), "k"])
            summary["cluster"] = fcluster(linkage_matrix, t=best_k, criterion="maxclust")
            summary["sector"] = pd.Series(asset_sector)
            display(scores.round(3))
            """
        ),
        md("## 6. Diversification diagnostics"),
        code(
            """
            within = []
            between = []
            for left in assets:
                for right in assets:
                    if left >= right:
                        continue
                    target = within if summary.loc[left, "cluster"] == summary.loc[right, "cluster"] else between
                    target.append(correlation.loc[left, right])
            display(pd.Series({
                "selected_clusters": best_k,
                "mean_within_cluster_correlation": np.mean(within),
                "mean_between_cluster_correlation": np.mean(between),
            }).to_frame("value"))
            """
        ),
        md("## 7. Dendrogram"),
        code(
            """
            plt.figure(figsize=(12, 5))
            dendrogram(linkage_matrix, labels=assets, leaf_rotation=90)
            plt.title("Asset similarity dendrogram")
            plt.tight_layout()
            """
        ),
        md("## 8. Representative assets"),
        code(
            """
            representatives = summary.sort_values(["cluster", "sharpe_proxy"], ascending=[True, False]).groupby("cluster").head(1)
            display(representatives.round(3))
            """
        ),
        md("## 9. Key findings\n\nClustering can expose redundant exposures, but portfolio construction still requires risk limits, costs and investment review."),
        *ending(project),
    ]


def dimension_cells(project: Project) -> list[dict]:
    return [
        md("## 1. Project setup"),
        setup(
            "from sklearn.cluster import KMeans\n"
            "from sklearn.datasets import load_digits\n"
            "from sklearn.decomposition import PCA\n"
            "from sklearn.manifold import TSNE, trustworthiness\n"
            "from sklearn.metrics import silhouette_score\n"
            "from sklearn.preprocessing import StandardScaler"
        ),
        md("## 2. Load high-dimensional digit data"),
        code(
            """
            digits = load_digits()
            sample_index = rng.choice(len(digits.data), size=1100, replace=False)
            X_raw = digits.data[sample_index]
            hidden_labels = digits.target[sample_index]
            X = StandardScaler().fit_transform(X_raw)
            print("Working shape:", X.shape)
            """
        ),
        md("## 3. Data quality and pixel variance"),
        code(
            """
            pixel_variance = X_raw.var(axis=0)
            display(pd.Series(pixel_variance).describe().to_frame("pixel_variance"))
            print("Zero-variance pixels:", int((pixel_variance == 0).sum()))
            """
        ),
        md("## 4. PCA variance trade-off"),
        code(
            """
            full_pca = PCA(random_state=RANDOM_STATE).fit(X)
            cumulative = np.cumsum(full_pca.explained_variance_ratio_)
            components_90 = int(np.searchsorted(cumulative, 0.90) + 1)
            plt.plot(np.arange(1, len(cumulative) + 1), cumulative)
            plt.axhline(0.90, color="red", linestyle="--")
            plt.axvline(components_90, color="red", linestyle="--")
            plt.title("Cumulative explained variance")
            plt.xlabel("Components")
            plt.ylabel("Explained variance")
            plt.tight_layout()
            """
        ),
        md("## 5. Build PCA and t-SNE projections"),
        code(
            """
            pca_2d = PCA(n_components=2, random_state=RANDOM_STATE).fit_transform(X)
            tsne_2d = TSNE(
                n_components=2,
                perplexity=30,
                init="pca",
                learning_rate="auto",
                random_state=RANDOM_STATE,
            ).fit_transform(X)
            """
        ),
        md("## 6. Neighbourhood preservation"),
        code(
            """
            display(pd.Series({
                "pca_trustworthiness": trustworthiness(X, pca_2d, n_neighbors=10),
                "tsne_trustworthiness": trustworthiness(X, tsne_2d, n_neighbors=10),
                "pca_2d_explained_variance": PCA(n_components=2).fit(X).explained_variance_ratio_.sum(),
            }).to_frame("value"))
            """
        ),
        md("## 7. Visual comparison"),
        code(
            """
            fig, axes = plt.subplots(1, 2, figsize=(13, 5))
            axes[0].scatter(pca_2d[:, 0], pca_2d[:, 1], c=hidden_labels, cmap="tab10", s=12)
            axes[0].set_title("PCA")
            axes[1].scatter(tsne_2d[:, 0], tsne_2d[:, 1], c=hidden_labels, cmap="tab10", s=12)
            axes[1].set_title("t-SNE")
            plt.tight_layout()
            """
        ),
        md("## 8. Downstream clustering comparison"),
        code(
            """
            X_pca_90 = PCA(n_components=components_90, random_state=RANDOM_STATE).fit_transform(X)
            raw_clusters = KMeans(n_clusters=10, n_init=30, random_state=RANDOM_STATE).fit_predict(X)
            pca_clusters = KMeans(n_clusters=10, n_init=30, random_state=RANDOM_STATE).fit_predict(X_pca_90)
            display(pd.Series({
                "raw_space_silhouette": silhouette_score(X, raw_clusters),
                "pca_90_space_silhouette": silhouette_score(X_pca_90, pca_clusters),
            }).to_frame("value"))
            """
        ),
        md("## 9. Key findings\n\nPCA supports reproducible global structure; t-SNE is better for local visual exploration and should not be interpreted as cluster proof."),
        *ending(project),
    ]


def cells_for(project: Project) -> list[dict]:
    if project.kind == "movie":
        return movie_cells(project)
    if project.kind == "book":
        return demo_recommender_cells(project, book=True)
    if project.kind == "customer":
        return customer_cells(project)
    if project.kind == "basket":
        return basket_cells(project)
    if project.kind.startswith("anomaly_"):
        return anomaly_cells(project, project.kind.removeprefix("anomaly_"))
    if project.kind == "audio":
        return audio_cells(project)
    if project.kind == "netflix":
        return netflix_cells(project)
    if project.kind == "topic_news":
        return topic_cells(project, reviews=False)
    if project.kind == "topic_reviews":
        return topic_cells(project, reviews=True)
    if project.kind == "semantic_resume":
        return semantic_cells(project, resume=True)
    if project.kind == "semantic_search":
        return semantic_cells(project, resume=False)
    if project.kind == "image_compression":
        return image_cells(project, palette=False)
    if project.kind == "palette":
        return image_cells(project, palette=True)
    if project.kind == "digits":
        return digits_cells(project)
    if project.kind == "geo":
        return geo_cells(project)
    if project.kind == "regimes":
        return regime_cells(project)
    if project.kind == "assets":
        return asset_cells(project)
    if project.kind == "dimension":
        return dimension_cells(project)
    raise ValueError(f"Unknown project kind: {project.kind}")


def make_notebook(project: Project) -> dict:
    opening = md(
        f"""
        # {project.title}

        {project.summary}

        **Portfolio category:** {project.category}

        **Data mode:** {project.data_mode}

        This notebook keeps labels out of fitting wherever labels exist, uses deterministic seeds,
        reports unsupervised-specific diagnostics, and avoids hard-coded results.
        """
    )
    return {
        "cells": [opening, *cells_for(project)],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def connect_block() -> str:
    root_readme = (REPO / "README.md").read_text(encoding="utf-8")
    match = re.search(r"(?ms)^## Let's Connect .+?^</div>", root_readme)
    if not match:
        raise RuntimeError("Locked Let's Connect block not found in repository README")
    return match.group(0)


def make_readme(project: Project, branding: str) -> str:
    method_items = "\n".join(f"- {item.strip()}" for item in project.method.split(","))
    metric_items = "\n".join(f"- {item.strip()}" for item in project.metrics.split(","))
    if project.kind == "movie":
        structure = clean(
            f"""
            ~~~text
            ├── {project.filename}
            ├── movie_titles.csv
            ├── ratings.tsv
            └── README.md
            ~~~
            """
        )
    else:
        structure = clean(
            f"""
            ~~~text
            ├── {project.filename}
            └── README.md
            ~~~
            """
        )
    readme = clean(
        f"""
        # {project.title}

        {project.summary}

        ## Overview

        This portfolio project demonstrates a reproducible unsupervised-learning workflow with
        transparent data assumptions, exploratory checks, appropriate diagnostics, interpretation
        and responsible-use notes. The notebook is designed to run from top to bottom.

        ## Problem statement

        - **Category:** {project.category}
        - **Goal:** {project.summary}
        - **Data mode:** {project.data_mode}
        - **Primary evaluation:** {project.metrics}

        ## Dataset

        - **Dataset:** {project.dataset}
        - **Reference/source:** {project.source}
        - **Reproducibility:** The default notebook path is deterministic and uses a fixed seed.

        Demonstration labels, where present, are hidden from fitting and used only after modelling
        to audit whether the unsupervised output recovered meaningful structure.

        ## Project workflow

        1. Validate schema, missingness, duplicates and feature ranges.
        2. Explore the behaviour most relevant to the unsupervised objective.
        3. Build a leakage-safe feature representation.
        4. Compare or calibrate the unsupervised method.
        5. Evaluate structure, stability, ranking quality or anomaly usefulness.
        6. Profile and interpret outputs before proposing downstream use.

        ## Methodology

        __METHOD_ITEMS__

        ## Evaluation

        __METRIC_ITEMS__

        Unsupervised metrics are read together rather than reduced to a single accuracy claim.
        When hidden labels exist in demonstration data, they never influence model fitting.

        ## Verified results

        The canonical notebook has been verified end to end in **{project.data_mode.lower()}**.
        Results are generated at execution time and intentionally not hard-coded into this README.
        Replace demonstration data only with licensed, privacy-safe data matching the documented schema.

        ## Repository structure

        __STRUCTURE__

        ## How to run

        From this project directory:

        ~~~bash
        python -m venv .venv
        source .venv/bin/activate
        pip install -r ../requirements.txt
        jupyter lab "{project.filename}"
        ~~~

        On Windows, activate the environment with <code>.venv\\Scripts\\activate</code>.

        ## Technologies

        - Python 3.11+
        - Pandas and NumPy
        - Scikit-learn and SciPy
        - Matplotlib and Seaborn
        - Jupyter

        ## Learning outcomes

        - Frame an unsupervised objective without inventing a target.
        - Select diagnostics that match clustering, ranking, association or anomaly tasks.
        - Separate model fitting from any hidden-label audit.
        - Turn mathematical output into cautious, domain-readable findings.

        ## Future improvements

        - Validate with a larger, newer and independently collected dataset.
        - Add repeated-sample stability and drift monitoring.
        - Review privacy, fairness and downstream decision risk.
        - Package inference only after the evaluation contract is agreed.

        ## Author

        **Tajamul Khan**

        [GitHub](https://github.com/tajamulkhann) · [LinkedIn](https://www.linkedin.com/in/tajamulkhann/) · Instagram: <code>@tajamul.codes</code>

        __BRANDING__
        """
    )
    return (
        readme.replace("__METHOD_ITEMS__", method_items)
        .replace("__METRIC_ITEMS__", metric_items)
        .replace("__STRUCTURE__", structure)
        .replace("__BRANDING__", branding)
        + "\n"
    )


def make_index(branding: str) -> str:
    rows = []
    for project in PROJECTS:
        link = project.slug.replace(" ", "%20")
        rows.append(
            f"| [{project.title}]({link}/) | {project.category} | {project.method} | {project.data_mode} |"
        )
    index = clean(
        f"""
        # Unsupervised Learning Projects

        A portfolio-ready collection of **21 unsupervised machine learning projects** by
        **Tajamul Khan**. The projects span clustering, recommendation systems, anomaly detection,
        topic modelling, semantic similarity, pattern mining, computer vision, geospatial analysis,
        financial regimes and dimensionality reduction.

        ## Project directory

        | Project | Category | Core methods | Data status |
        |---|---|---|---|
        __PROJECT_ROWS__

        ## Portfolio standards

        - One canonical notebook and one detailed README per project
        - Portable paths, deterministic seeds and stripped notebook outputs
        - No labels used during unsupervised fitting
        - Multiple task-appropriate diagnostics instead of misleading accuracy claims
        - Clear data provenance, limitations and responsible-use notes
        - Exact creator branding preserved across every README

        ## Quick start

        ~~~bash
        git clone https://github.com/tajamulkhann/Machine-Learning-Projects.git
        cd "Machine-Learning-Projects/Unsupervised Learning Projects"
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        jupyter lab
        ~~~

        On Windows, activate the environment with <code>.venv\\Scripts\\activate</code>.

        ## Evaluation philosophy

        Clustering projects use structure and stability diagnostics. Recommenders use similarity,
        coverage and diversity checks. Anomaly projects evaluate rankings only after fitting.
        Topic models use reconstruction and topic-diversity diagnostics. Every notebook explains
        what its metrics can and cannot prove.

        ## Author

        **Tajamul Khan**

        __BRANDING__
        """
    )
    return (
        index.replace("__PROJECT_ROWS__", chr(10).join(rows))
        .replace("__BRANDING__", branding)
        + "\n"
    )


def main() -> None:
    PORTFOLIO.mkdir(exist_ok=True)
    branding = connect_block()

    for project in PROJECTS:
        project_dir = PORTFOLIO / project.slug
        project_dir.mkdir(parents=True, exist_ok=True)
        notebook_path = project_dir / project.filename
        notebook_path.write_text(
            json.dumps(make_notebook(project), indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (project_dir / "README.md").write_text(make_readme(project, branding), encoding="utf-8")

    requirements = clean(
        """
        jupyterlab>=4.2,<5
        matplotlib>=3.8,<4
        numpy>=1.26,<3
        pandas>=2.2,<3
        scikit-learn>=1.5,<2
        scipy>=1.12,<2
        seaborn>=0.13,<1
        """
    ) + "\n"
    (PORTFOLIO / "requirements.txt").write_text(requirements, encoding="utf-8")
    (PORTFOLIO / "README.md").write_text(make_index(branding), encoding="utf-8")

    root_readme_path = REPO / "README.md"
    root_readme = root_readme_path.read_text(encoding="utf-8")
    root_readme = re.sub(
        r"(\| \[Unsupervised Learning\]\(Unsupervised%20Learning%20Projects/\) \| )\d+( \|)",
        r"\g<1>21\2",
        root_readme,
    )
    root_readme_path.write_text(root_readme, encoding="utf-8")

    print(f"Built {len(PROJECTS)} unsupervised projects.")


if __name__ == "__main__":
    main()
