# FraudShield X: UPI Mule Ring Early-Warning System Using Temporal Graph Risk Signals

## Project Overview

FraudShield X is an end-to-end fraud detection and mule-risk intelligence project designed to identify suspicious UPI-style transaction behavior using multi-layer risk signals, machine learning, SQL analytics, web application development, API serving, Docker containerization, and cloud deployment documentation.

The project combines:

- Transaction-level fraud indicators
- Account-level mule-risk features
- Temporal burst-risk signals
- Graph and network relationship features
- Hybrid risk scoring techniques
- Machine learning fraud classification
- Model interpretation and feature importance
- SQL fraud analytics layer
- Power BI dashboard planning
- Streamlit fraud-risk web application
- FastAPI prediction service
- Docker containerization
- Cloud deployment documentation

The goal of the system is to identify high-risk transactions and detect mule-ring behavior before large-scale fraud escalation.

---

## Live Demo

- Streamlit Application: https://fraudshield-x-upi.streamlit.app/

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fraudshield-x-upi.streamlit.app/)

---

## Business Problem

Digital payment fraud is increasing rapidly in instant payment ecosystems. Fraudsters often use mule accounts, repeated sender-receiver relationships, high-value transfers, night transactions, account-draining behavior, and burst activity patterns to hide fraudulent movement of funds.

FraudShield X is designed to help financial platforms:

- Detect suspicious transactions early
- Identify high-risk sender and receiver accounts
- Monitor mule-account behavior
- Analyze temporal and network-based fraud patterns
- Provide explainable risk scoring
- Support real-time fraud-risk prediction
- Enable dashboard-based fraud monitoring

---

## Dataset

- 508,213 final sampled transactions
- 500,000 genuine transactions
- 8,213 fraud transactions
- 1.6161% fraud rate
- 31 strict no-leakage ML features
- 66 final dataset columns

---

## Risk Feature Categories

- Transaction Risk Features
- Account Risk Features
- Temporal Burst Features
- Network Graph Features
- Hybrid Risk Signals

---

## Model Explainability

The project includes feature importance analysis and model interpretation techniques to identify the most influential fraud-risk indicators contributing to prediction outcomes.

---

## Deployment

- Streamlit Cloud Deployment
- FastAPI Prediction Service
- Docker Containerization

---

## Project Architecture

```text
Raw UPI-Style Transaction Data
        |
        v
Data Cleaning and EDA
        |
        v
Feature Engineering
(Transaction + Account + Temporal + Network Features)
        |
        v
Risk Layer Creation
(Transaction Risk + Mule Risk + Temporal Risk + Network Risk + Hybrid Risk)
        |
        v
Strict No-Leakage ML Training
(Logistic Regression + Random Forest)
        |
        v
Model Evaluation and Feature Importance
        |
        v
SQL Fraud Analytics Layer
        |
        v
Power BI Dashboard Planning
        |
        v
Streamlit Fraud Risk Web Application
        |
        v
FastAPI Prediction Service
        |
        v
Docker Containerization
        |
        v
Cloud Deployment Documentation
```

---

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Project Structure

```text
FraudShield-X-UPI-Mule-Ring-Early-Warning/
│
├── data/
├── notebooks/
├── screenshots/
├── models/
├── app.py
├── requirements.txt
├── README.md
└── main.py
```
