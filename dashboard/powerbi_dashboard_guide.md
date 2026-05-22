# FraudShield X - Power BI Dashboard Guide

This document explains the Power BI dashboard design for the FraudShield X project.

## Dashboard Objective

The Power BI dashboard is designed to monitor UPI fraud patterns, mule-account risk indicators, risk-layer performance, and machine learning model results.

## Dashboard Pages

### Page 1: Executive Summary

Purpose: Give a quick overview of the full fraud detection project.

Recommended visuals:

- KPI Card: Total Transactions
- KPI Card: Total Genuine Transactions
- KPI Card: Total Fraud Transactions
- KPI Card: Fraud Percentage
- KPI Card: Best Model
- KPI Card: Recall
- KPI Card: F1 Score
- KPI Card: ROC-AUC
- Bar Chart: Model Comparison by F1 Score
- Bar Chart: Top 10 Feature Importance

Data files:

- `project_metrics_summary.csv`
- `model_comparison_results.csv`
- `top_10_feature_importance.csv`

---

### Page 2: Fraud Pattern Analysis

Purpose: Analyze when and where fraud is happening.

Recommended visuals:

- Bar Chart: Fraud Percentage by Transaction Type
- Line Chart: Fraud Count by Hour of Day
- Bar Chart: Fraud Percentage by Transaction Day
- Bar Chart: Fraud Percentage by Amount Bucket
- Donut Chart: Fraud vs Genuine Transactions

Data files:

- `transaction_type_fraud_summary.csv`
- `hour_fraud_summary.csv`
- `day_fraud_summary.csv`
- `amount_bucket_fraud_summary.csv`
- `fraud_imbalance_summary.csv`

---

### Page 3: Risk Layer Analysis

Purpose: Compare transaction, temporal, network, and final hybrid risk layers.

Recommended visuals:

- Bar Chart: Fraud Percentage by Transaction Risk Level
- Bar Chart: Fraud Percentage by Temporal Risk Level
- Bar Chart: Fraud Percentage by Network Risk Level
- Bar Chart: Fraud Percentage by Final Hybrid Risk Level
- Matrix: Risk Layer Summary

Data files:

- `transaction_risk_level_summary.csv`
- `temporal_risk_fraud_summary.csv`
- `network_risk_fraud_summary.csv`
- `final_hybrid_risk_summary.csv`
- `risk_layer_summary.csv`

---

### Page 4: Mule Account Risk Analysis

Purpose: Identify high-risk sender and receiver accounts.

Recommended visuals:

- Table: Top Fraud Senders
- Table: Top Fraud Receivers
- Table: Top Mule Risk Accounts
- Bar Chart: Top Accounts by Fraud Count
- Bar Chart: Top Accounts by Total Fraud Amount

Data files:

- `top_fraud_senders.csv`
- `top_fraud_receivers.csv`
- `top_mule_risk_accounts.csv`

---

### Page 5: Model Performance and Explainability

Purpose: Explain how the machine learning model performed and which features were most important.

Recommended visuals:

- Bar Chart: Model Comparison by Recall
- Bar Chart: Model Comparison by F1 Score
- Bar Chart: Model Comparison by ROC-AUC
- Bar Chart: Top 10 Feature Importance
- Table: Model Metrics Summary

Data files:

- `model_comparison_results.csv`
- `top_10_feature_importance.csv`
- `random_forest_feature_importance.csv`

---

## Recommended Slicers

Use slicers for:

- Transaction Type
- Risk Level
- Hour of Day
- Transaction Day
- Model Name

## Key Business Questions Answered

This dashboard helps answer:

1. What percentage of transactions are fraudulent?
2. Which transaction types have the highest fraud rate?
3. Which time periods show higher fraud activity?
4. Which risk layer detects fraud most effectively?
5. Which accounts show mule-risk behavior?
6. Which machine learning model performs best?
7. Which features are most important for fraud prediction?

## Skills Demonstrated

- Power BI dashboard planning
- KPI design
- Fraud analytics reporting
- Business intelligence storytelling
- Risk-layer visualization
- Model performance visualization
- Feature importance visualization