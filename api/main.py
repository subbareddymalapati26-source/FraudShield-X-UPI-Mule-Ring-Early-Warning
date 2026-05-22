from fastapi import FastAPI
from api.schemas import TransactionInput, PredictionOutput
from api.model_loader import predict_transaction_risk

app = FastAPI(
    title="FraudShield X API",
    description="FastAPI service for UPI fraud risk prediction and mule-account risk scoring.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "FraudShield X",
        "message": "UPI Fraud Risk Prediction API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "FraudShield X API"
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(transaction: TransactionInput):
    result = predict_transaction_risk(transaction)
    return result