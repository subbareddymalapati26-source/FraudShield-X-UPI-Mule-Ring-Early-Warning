-- ============================================================
-- FraudShield X: SQL Analytics Layer
-- File: create_tables.sql
-- Purpose: Create tables for fraud analytics summary datasets
-- ============================================================

-- 1. Project metrics summary
CREATE TABLE project_metrics_summary (
    metric VARCHAR(100),
    value VARCHAR(100)
);

-- 2. Risk layer summary
CREATE TABLE risk_layer_summary (
    risk_layer VARCHAR(100),
    output_file VARCHAR(150),
    purpose TEXT
);

-- 3. Model comparison results
CREATE TABLE model_comparison_results (
    model VARCHAR(100),
    accuracy DECIMAL(10,4),
    precision_score DECIMAL(10,4),
    recall DECIMAL(10,4),
    f1_score DECIMAL(10,4),
    roc_auc DECIMAL(10,4)
);

-- 4. Final hybrid risk summary
CREATE TABLE final_hybrid_risk_summary (
    final_risk_level VARCHAR(100),
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 5. Network risk fraud summary
CREATE TABLE network_risk_fraud_summary (
    network_risk_level VARCHAR(100),
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 6. Temporal risk fraud summary
CREATE TABLE temporal_risk_fraud_summary (
    temporal_risk_level VARCHAR(100),
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 7. Transaction risk level summary
CREATE TABLE transaction_risk_level_summary (
    transaction_risk_level VARCHAR(100),
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 8. Transaction type fraud summary
CREATE TABLE transaction_type_fraud_summary (
    transaction_type VARCHAR(50),
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 9. Hour fraud summary
CREATE TABLE hour_fraud_summary (
    hour_of_day INT,
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 10. Day fraud summary
CREATE TABLE day_fraud_summary (
    transaction_day INT,
    genuine_count INT,
    fraud_count INT,
    total_transactions INT,
    fraud_percentage DECIMAL(10,4)
);

-- 11. Top feature importance
CREATE TABLE top_10_feature_importance (
    feature VARCHAR(150),
    importance DECIMAL(10,6)
);

-- ============================================================
-- Note:
-- CSV files can be imported into these tables using MySQL Workbench,
-- PostgreSQL COPY command, or database import tools.
-- ============================================================