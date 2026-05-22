-- ============================================================
-- FraudShield X: SQL Fraud Analytics Queries
-- File: fraud_analysis_queries.sql
-- Purpose: Analyze fraud patterns, risk layers, and model results
-- ============================================================

-- 1. View overall project metrics
SELECT *
FROM project_metrics_summary;

-- 2. Compare machine learning model performance
SELECT
    model,
    accuracy,
    precision_score,
    recall,
    f1_score,
    roc_auc
FROM model_comparison_results
ORDER BY f1_score DESC;

-- 3. Identify highest fraud percentage by final risk level
SELECT
    final_risk_level,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM final_hybrid_risk_summary
ORDER BY fraud_percentage DESC;

-- 4. Analyze fraud percentage by network risk level
SELECT
    network_risk_level,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM network_risk_fraud_summary
ORDER BY fraud_percentage DESC;

-- 5. Analyze fraud percentage by temporal risk level
SELECT
    temporal_risk_level,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM temporal_risk_fraud_summary
ORDER BY fraud_percentage DESC;

-- 6. Analyze fraud percentage by transaction risk level
SELECT
    transaction_risk_level,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM transaction_risk_level_summary
ORDER BY fraud_percentage DESC;

-- 7. Find transaction types with highest fraud percentage
SELECT
    transaction_type,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM transaction_type_fraud_summary
ORDER BY fraud_percentage DESC;

-- 8. Find high-risk hours based on fraud percentage
SELECT
    hour_of_day,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM hour_fraud_summary
WHERE fraud_count > 0
ORDER BY fraud_percentage DESC;

-- 9. Find high-risk transaction days
SELECT
    transaction_day,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM day_fraud_summary
WHERE fraud_count > 0
ORDER BY fraud_percentage DESC;

-- 10. Top predictive features from Random Forest
SELECT
    feature,
    importance
FROM top_10_feature_importance
ORDER BY importance DESC;

-- 11. Risk layer effectiveness comparison
SELECT
    'Final Hybrid Risk' AS risk_layer,
    final_risk_level AS risk_category,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM final_hybrid_risk_summary

UNION ALL

SELECT
    'Network Risk' AS risk_layer,
    network_risk_level AS risk_category,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM network_risk_fraud_summary

UNION ALL

SELECT
    'Temporal Risk' AS risk_layer,
    temporal_risk_level AS risk_category,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM temporal_risk_fraud_summary

UNION ALL

SELECT
    'Transaction Risk' AS risk_layer,
    transaction_risk_level AS risk_category,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM transaction_risk_level_summary

ORDER BY fraud_percentage DESC;

-- 12. Business insight: risk levels with more than 50% fraud rate
SELECT
    final_risk_level,
    total_transactions,
    fraud_count,
    fraud_percentage
FROM final_hybrid_risk_summary
WHERE fraud_percentage >= 50
ORDER BY fraud_percentage DESC;