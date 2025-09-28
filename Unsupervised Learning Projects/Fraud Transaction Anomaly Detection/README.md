# Anomaly Detection (Unsupervised)

## Objective
Detect unusual transactions that deviate from normal user behavior to surface potential fraud **without relying on labeled data**, supporting faster triage and investigation.

## Algorithms Used
- **Isolation Forest:** Tree-based method that isolates anomalies via shorter path lengths; outputs decision scores and anomaly labels.  
- **Local Outlier Factor (LOF):** Density-based method comparing local neighborhood density; more negative scores indicate stronger anomalies.

## Dataset
- Synthetic transactions with features: **amount, transaction hour, device age, geo-distance jump, merchant risk score, velocity proxy**.  
- **User-level rolling features** (7-event means/stds) for amount, velocity, and geo-distance to model personal baselines.  
- Small injected fraction of anomalies (spikes in amount/velocity, odd hours, large geo jumps, high-risk merchants) used as proxy labels.

## Key Findings
- Both models consistently flag **large spend spikes at odd hours with unusually long geo jumps**, especially when deviating from each user’s recent baseline.  
- A simple **OR-ensemble** (flag if any model alerts) improves recall on injected anomalies with a modest increase in false positives.

## Business Insights
- **Triage:** Prioritize investigations using anomaly scores and combine with business rules.  
- **Thresholds:** Calibrate to alert budgets and analyst capacity; revisit as behavior drifts.  
- **Feedback loops:** Use analyst outcomes to refine thresholds, features, and retraining cadence.

## Hyperparameter Guidelines
- **Isolation Forest:** `n_estimators=200–500`, `contamination=0.5%–3%`, `max_samples="auto"` or `256–1024`.  
- **LOF:** `n_neighbors=20–50`, `contamination=0.5%–3%`, `novelty=True` for scoring new data post-fit.  
- **Preprocessing:** `RobustScaler` and `log1p` on heavy-tailed features (amount, velocity, distance).

## Conclusion
Unsupervised detection with **Isolation Forest** and **LOF**, enriched by behavioral rollups, effectively surfaces atypical transactions without labels. With calibrated thresholds and periodic updates, it supports **real-time alerting and efficient fraud investigations**.
