# Unsupervised Learning Projects

A portfolio-ready collection of **21 unsupervised machine learning projects** by
**Tajamul Khan**. The projects span clustering, recommendation systems, anomaly detection,
topic modelling, semantic similarity, pattern mining, computer vision, geospatial analysis,
financial regimes and dimensionality reduction.

## Project directory

| Project | Category | Core methods | Data status |
|---|---|---|---|
| [Movie Recommendation System](Movie%20Recommendation%20System/) | Recommendation | User-item filtering, cosine similarity and popularity-aware candidate filtering | Committed dataset |
| [Book Recommendation Engine](Book%20Recommendation%20Engine/) | Recommendation | Interaction filtering, item cosine similarity and popularity-aware recommendations | Verified demo mode |
| [Customer Segmentation Using Clustering](Customer%20Segmentation%20Using%20Clustering/) | Clustering | Robust feature scaling, K-Means selection, PCA visualisation and segment profiling | Verified demo mode |
| [Fraud Detection Using Anomaly Detection](Fraud%20Detection%20Using%20Anomaly%20Detection/) | Anomaly detection | Isolation Forest, Local Outlier Factor and anomaly-score diagnostics | Verified demo mode |
| [Market Basket Analysis](Market%20Basket%20Analysis/) | Pattern mining | Frequent singleton and pair mining with support, confidence and lift | Verified demo mode |
| [Spotify Song Clustering and Playlist Discovery](Spotify%20Song%20Clustering%20and%20Playlist%20Discovery/) | Clustering | Feature scaling, K-Means selection, PCA projection and cluster profiling | Verified demo mode |
| [Netflix Content Clustering and Similarity](Netflix%20Content%20Clustering%20and%20Similarity/) | Recommendation | TF-IDF, K-Means, nearest neighbours and metadata-aware similarity | Verified demo mode |
| [News Article Topic Modeling](News%20Article%20Topic%20Modeling/) | NLP and topic modelling | TF-IDF, non-negative matrix factorisation and topic assignment | Verified demo mode |
| [Customer Review Topic Modeling](Customer%20Review%20Topic%20Modeling/) | NLP and topic modelling | TF-IDF, NMF topic extraction and topic-level review inspection | Verified demo mode |
| [Resume and Job Description Semantic Matching](Resume%20and%20Job%20Description%20Semantic%20Matching/) | NLP similarity | TF-IDF, latent semantic analysis and cosine similarity | Verified demo mode |
| [Document Similarity Search Using LSA](Document%20Similarity%20Search%20Using%20LSA/) | NLP similarity | TF-IDF, truncated SVD, vector normalisation and nearest-neighbour retrieval | Verified demo mode |
| [Image Compression Using K-Means](Image%20Compression%20Using%20K-Means/) | Computer vision | Pixel sampling, MiniBatch K-Means quantisation and image reconstruction | Verified demo mode |
| [Brand Color Palette Extraction](Brand%20Color%20Palette%20Extraction/) | Computer vision | RGB pixel clustering, palette ordering, colour proportions and HEX conversion | Verified demo mode |
| [Handwritten Digit Clustering](Handwritten%20Digit%20Clustering/) | Clustering | Standardisation, PCA, K-Means and cluster-to-label diagnostics | Built-in dataset |
| [Geospatial Delivery Hotspot Clustering](Geospatial%20Delivery%20Hotspot%20Clustering/) | Geospatial clustering | Haversine DBSCAN, hotspot ranking and noise analysis | Verified demo mode |
| [Cryptocurrency Market Regime Detection](Cryptocurrency%20Market%20Regime%20Detection/) | Financial clustering | Rolling feature engineering, scaling, K-Means and chronological regime profiles | Verified demo mode |
| [Stock Portfolio Diversification Using Asset Clustering](Stock%20Portfolio%20Diversification%20Using%20Asset%20Clustering/) | Financial clustering | Return statistics, correlation features, hierarchical clustering and representative selection | Verified demo mode |
| [Network Intrusion Anomaly Detection](Network%20Intrusion%20Anomaly%20Detection/) | Anomaly detection | Isolation Forest, Local Outlier Factor and score-distribution analysis | Verified demo mode |
| [Predictive Maintenance Sensor Anomaly Detection](Predictive%20Maintenance%20Sensor%20Anomaly%20Detection/) | Anomaly detection | Isolation Forest, Local Outlier Factor and sensor-level error inspection | Verified demo mode |
| [Time Series Anomaly Detection](Time%20Series%20Anomaly%20Detection/) | Anomaly detection | Rolling residual features, robust z-scores and Isolation Forest | Verified demo mode |
| [PCA and Manifold Learning Visual Lab](PCA%20and%20Manifold%20Learning%20Visual%20Lab/) | Dimensionality reduction | Standardisation, PCA, t-SNE and neighbourhood visualisation | Built-in dataset |

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

On Windows, activate the environment with <code>.venv\Scripts\activate</code>.

## Evaluation philosophy

Clustering projects use structure and stability diagnostics. Recommenders use similarity,
coverage and diversity checks. Anomaly projects evaluate rankings only after fitting.
Topic models use reconstruction and topic-diversity diagnostics. Every notebook explains
what its metrics can and cannot prove.

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
