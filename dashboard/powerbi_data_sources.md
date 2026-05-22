# FraudShield X - Power BI Data Sources

This document lists the datasets used for the Power BI dashboard layer.

## Main Data Sources

| CSV File | Purpose |
|---|---|
| `project_metrics_summary.csv` | Overall project metrics such as total transactions, fraud percentage, best model, recall, F1 score, and ROC-AUC |
| `model_comparison_results.csv` | Compares machine learning models using accuracy, precision, recall, F1 score, and ROC-AUC |
| `top_10_feature_importance.csv` | Shows the top 10 most important features from the Random Forest model |
| `random_forest_feature_importance.csv` | Full feature importance list from the Random Forest model |
| `fraud_imbalance_summary.csv` | Shows genuine vs fraud transaction distribution |
| `transaction_type_fraud_summary.csv` | Fraud analysis by transaction type |
| `hour_fraud_summary.csv` | Fraud analysis by hour of day |
| `day_fraud_summary.csv` | Fraud analysis by transaction day |
| `amount_bucket_fraud_summary.csv` | Fraud analysis by transaction amount bucket |
| `transaction_risk_level_summary.csv` | Fraud distribution by transaction risk level |
| `temporal_risk_fraud_summary.csv` | Fraud distribution by temporal burst risk level |
| `network_risk_fraud_summary.csv` | Fraud distribution by sender-receiver network risk level |
| `final_hybrid_risk_summary.csv` | Fraud distribution by final hybrid risk level |
| `risk_layer_summary.csv` | Explains each risk layer and its purpose |
| `top_fraud_senders.csv` | Lists sender accounts with high fraud activity |
| `top_fraud_receivers.csv` | Lists receiver accounts with high fraud activity |
| `top_mule_risk_accounts.csv` | Lists accounts with high mule-risk behavior |

## Suggested Power BI Pages

| Page | Data Sources |
|---|---|
| Executive Summary | `project_metrics_summary.csv`, `model_comparison_results.csv`, `top_10_feature_importance.csv` |
| Fraud Pattern Analysis | `transaction_type_fraud_summary.csv`, `hour_fraud_summary.csv`, `day_fraud_summary.csv`, `amount_bucket_fraud_summary.csv`, `fraud_imbalance_summary.csv` |
| Risk Layer Analysis | `transaction_risk_level_summary.csv`, `temporal_risk_fraud_summary.csv`, `network_risk_fraud_summary.csv`, `final_hybrid_risk_summary.csv`, `risk_layer_summary.csv` |
| Mule Account Risk Analysis | `top_fraud_senders.csv`, `top_fraud_receivers.csv`, `top_mule_risk_accounts.csv` |
| Model Performance | `model_comparison_results.csv`, `top_10_feature_importance.csv`, `random_forest_feature_importance.csv` |

## Power BI Import Steps

1. Open Power BI Desktop.
2. Click **Get Data**.
3. Select **Text/CSV**.
4. Import the required CSV files from the `data/` folder.
5. Check column data types.
6. Create KPI cards, bar charts, line charts, tables, and slicers.
7. Save the dashboard file as:

```text
FraudShield_X_PowerBI_Dashboard.pbix