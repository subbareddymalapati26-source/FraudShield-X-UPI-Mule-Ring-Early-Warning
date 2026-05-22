from pydantic import BaseModel


class TransactionInput(BaseModel):
    Transaction_Amount: float
    Hour_Of_Day: int
    Sender_Old_Balance: float
    Sender_New_Balance: float
    Receiver_Old_Balance: float
    Receiver_New_Balance: float
    Sender_Network_Txn_Count: int
    Receiver_Network_Txn_Count: int
    Edge_Txn_Count: int
    Transaction_Type: str


class PredictionOutput(BaseModel):
    prediction: int
    fraud_probability: float
    risk_status: str
    risk_score: int