# FraudShield X - SQL Analytics Layer

This folder contains the SQL analytics layer for the FraudShield X project.

## Purpose

The SQL layer is used to analyze fraud patterns, risk-layer performance, model results, and feature importance from dashboard-ready summary datasets.

## Files

| File | Purpose |
|---|---|
| `create_tables.sql` | Creates SQL tables for fraud analytics summary CSV files |
| `fraud_analysis_queries.sql` | Contains SQL queries for fraud pattern analysis and risk-layer comparison |
| `README_SQL.md` | Explains the SQL layer |

## Datasets Used

The SQL layer is designed for the following summary CSV files:

- `project_metrics_summary.csv`
- `risk_layer_summary.csv`
- `model_comparison_results.csv`
- `final_hybrid_risk_summary.csv`
- `network_risk_fraud_summary.csv`
- `temporal_risk_fraud_summary.csv`
- `transaction_risk_level_summary.csv`
- `transaction_type_fraud_summary.csv`
- `hour_fraud_summary.csv`
- `day_fraud_summary.csv`
- `top_10_feature_importance.csv`

## SQL Analysis Performed

The SQL queries analyze:

- Overall project metrics
- Model comparison results
- Fraud percentage by final risk level
- Fraud percentage by network risk level
- Fraud percentage by temporal risk level
- Fraud percentage by transaction risk level
- Fraud by transaction type
- Fraud by hour and day
- Top predictive features
- Risk layer effectiveness

## Skills Demonstrated

- SQL table design
- Aggregate analysis
- Filtering and sorting
- Fraud pattern analysis
- Risk segmentation
- Model result interpretation
- Business insight generation