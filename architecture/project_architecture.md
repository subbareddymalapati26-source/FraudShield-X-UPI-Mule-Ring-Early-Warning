# FraudShield X - Project Architecture

## End-to-End Architecture

```text
Raw UPI-Style Transaction Data
        |
        v
Data Cleaning & EDA
        |
        v
Feature Engineering
        |
        |-- Transaction Risk Features
        |-- Account Mule-Risk Features
        |-- Temporal Burst-Risk Features
        |-- Graph / Network Risk Features
        |
        v
Final Hybrid Risk Scoring
        |
        v
Strict No-Leakage ML Training
        |
        |-- Logistic Regression
        |-- Random Forest
        |
        v
Model Evaluation & Feature Importance
        |
        v
SQL Fraud Analytics Layer
        |
        v
Power BI Dashboard Planning
        |
        v
Streamlit Fraud Risk Web App
        |
        v
FastAPI Prediction Service
        |
        v
Docker Containerization
        |
        v
Cloud Deployment Documentation