# FraudShield X - Architecture Diagram

```mermaid
flowchart TD

    A[Raw UPI-Style Transaction Data] --> B[Data Cleaning & EDA]

    B --> C[Feature Engineering]

    C --> C1[Transaction Risk Features]
    C --> C2[Account Mule-Risk Features]
    C --> C3[Temporal Burst-Risk Features]
    C --> C4[Graph / Network Risk Features]

    C1 --> D[Final Hybrid Risk Scoring]
    C2 --> D
    C3 --> D
    C4 --> D

    D --> E[Strict No-Leakage ML Training]

    E --> E1[Logistic Regression]
    E --> E2[Random Forest]

    E1 --> F[Model Evaluation]
    E2 --> F

    F --> G[Feature Importance Analysis]

    G --> H[SQL Fraud Analytics Layer]

    H --> I[Power BI Dashboard Planning]

    I --> J[Streamlit Fraud Risk Web App]

    J --> K[FastAPI Prediction Service]

    K --> L[Docker Containerization]

    L --> M[Cloud Deployment Documentation]

    M --> N[Portfolio-Ready GitHub Project]