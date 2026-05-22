# FraudShield X: UPI Mule Ring Early-Warning System Using Temporal Graph Risk Signals

## Project Overview

FraudShield X is an advanced fraud detection and mule-risk intelligence project designed to identify suspicious UPI-style transaction behavior using multi-layer risk signals.

The project combines:

- Transaction-level fraud indicators
- Account-level mule-risk features
- Temporal burst-risk signals
- Graph/network relationship features
- Final hybrid risk scoring
- Machine learning fraud classification
- Model interpretation and feature importance

The goal is to build an early-warning system that can detect high-risk transactions and mule-ring behavior before large-scale fraud escalation.

---

## Dataset

- 508,213 final sampled transactions
- 500,000 genuine transactions
- 8,213 fraud transactions
- 1.6161% fraud rate
- 31 strict no-leakage ML features
- 66 final dataset columns

---

## Key Risk Layers

### 1. Transaction Risk Layer

Detects suspicious transaction behavior using transaction amount, sender/receiver balance changes, zero-balance flags, risky transaction type indicators, and amount-to-balance ratios.

### 2. Account Mule-Risk Layer

Creates sender and receiver account-level risk signals such as total transaction count, fraud involvement indicators, pass-through behavior, in-out transaction ratio, and mule-risk score.

### 3. Temporal Burst-Risk Layer

Detects sudden high-frequency or high-value activity using sender/receiver hourly transaction counts, hourly amounts, and velocity-risk flags.

### 4. Graph / Network Risk Layer

Uses sender-receiver relationship features such as sender network out-degree, receiver network in-degree, edge transaction count, edge total amount, edge average amount, and network risk score.

### 5. Final Hybrid Risk Layer

Combines transaction, temporal, network, and account-level risk signals into one final hybrid score for transaction-level early warning.

---

## Machine Learning Models

Two strict no-leakage models were trained using only transaction-time features:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Strict Logistic Regression | 0.9719 | 0.3622 | 0.9738 | 0.5280 | 0.9959 |
| Strict Random Forest | 1.0000 | 1.0000 | 0.9970 | 0.9985 | 0.9997 |

The Random Forest model achieved the best overall performance.

---

## Best Model

**Strict Random Forest Classifier**

- Accuracy: 1.0000
- Precision: 1.0000
- Recall: 0.9970
- F1 Score: 0.9985
- ROC-AUC: 0.9997

---

## Top Feature Importances

1. Sender_Balance_Error
2. Amount_To_Sender_Balance_Ratio
3. Risky_Transaction_Type_Flag
4. Sender_Zero_Balance_After_Flag
5. Sender_Old_Balance
6. Sender_New_Balance
7. Amount_To_Receiver_Balance_Ratio
8. Edge_Total_Amount
9. Transaction_Amount
10. Edge_Avg_Amount

These features show that fraud behavior is strongly linked to sender balance anomalies, high-risk transaction types, account-draining behavior, and network edge amount patterns.

---

## Leakage Control

To avoid target leakage, fraud-label-derived features and final rule-based risk-score features were excluded from strict ML training.

The project separates rule-based risk intelligence features from strict no-leakage machine learning features.

---

## Saved Artifacts

### Data Outputs

- project_metrics_summary.csv
- risk_layer_summary.csv
- model_comparison_results.csv
- random_forest_feature_importance.csv
- top_10_feature_importance.csv
- final_hybrid_risk_summary.csv
- network_risk_fraud_summary.csv

### Model Outputs

- fraudshield_random_forest_model.pkl
- strict_ml_features.pkl
- model_metadata.json

---

## Project Structure

```text
FraudShield-X-UPI-Mule-Ring-Early-Warning/
|-- data/
|-- models/
|-- notebooks/
|-- reports/
|-- images/
|-- dashboard/
|-- src/
```

---

## Business Impact

FraudShield X can help financial platforms detect high-risk transactions early, identify mule-account behavior, reduce fraud losses, improve investigation workflows, prioritize suspicious transaction networks, and support real-time fraud-risk scoring.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Jupyter Notebook

---

## Final Outcome

FraudShield X successfully combines behavioral analytics, temporal signals, network intelligence, and machine learning to create a strong fraud-risk detection system for UPI-style digital transactions.